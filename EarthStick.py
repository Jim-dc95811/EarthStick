#!/usr/bin/env python3
"""EarthStick 1.3.1

1.3.1: larger, thicker crosshair (80 px, 5 px lines) for aiming at World Gates;
  nothing else changed

1.3 adds wormholes (flying, trigger-click, constants and recovery unchanged from 1.2):
  - gate files (KML/KMZ golden rings with gate data) in a "Gates" folder beside
    this program are read at startup
  - fly through a gate ring in its facing direction and the camera jumps:
    to just past the partner gate named in "to" (facing away from it), or to a
    fixed destination (one-way gate)
  - gates only fire when crossed forwards, and not again for GATE_COOLDOWN_S
  - a gate's "to" partner is looked up in its own file first, so two gate files
    may reuse names (TEST2); a name that is ambiguous across files is skipped
    with a message
  - no Gates folder or no gate files = flies exactly as 1.2

1.2 adds trigger-click (flying, constants and recovery unchanged from 1.1):
  - a red crosshair sits at the centre of the ArcGIS Earth window (click-through)
  - put an object under the crosshair, let go (hover) and pull the trigger
    (button 1): EarthStick clicks it for you, so its popup opens without the mouse
  - the click glides the pointer onto the target and rests before and after, which
    ArcGIS Earth needs to select an object (an instant click zooms instead)
  - if the crosshair cannot be shown, EarthStick still flies normally

1.1 hardening (controls, constants, movement, zoom and recovery unchanged):
  - if the joystick is not connected at startup, EarthStick waits for it
    instead of stopping
  - the local ArcGIS Earth API connection never goes through a system proxy
  - while waiting for ArcGIS Earth, the reason is shown when it first appears
    or changes
  - one "press Enter" prompt after an error instead of two

Thrustmaster T.A320 Pilot -> ArcGIS Earth camera bridge.

Controls:
  X axis       : strafe left/right
  Y axis       : move forward/back
  RZ axis      : heading left/right
  Slider0      : movement speed
  POV up/down  : camera tilt

Button 4 (red top button) zooms in / descends.
Button 3 (black thumb button) zooms out / climbs.
Button 1 (trigger) clicks the object under the crosshair.
Neutral controls stop and hover in place.

Standard-library only. Windows desktop ArcGIS Earth Automation API is expected
at http://localhost:8000.
"""

from __future__ import annotations

import ctypes
import json
import math
import os
import sys
import time
import urllib.error
import urllib.request
from ctypes import wintypes
from pathlib import Path
import xml.etree.ElementTree as ET
import zipfile

VERSION = "1.3.1"
BASE_URL = "http://localhost:8000"
CAMERA_URL = BASE_URL + "/arcgisearth/camera"
TARGET_NAME = "T.A320 Pilot"

POLL_HZ = 30.0
DEADZONE = 0.08
YAW_RATE_DPS = 55.0
TILT_RATE_DPS = 45.0
EARTH_RADIUS_M = 6378137.0
IDLE_RESYNC_SECONDS = 0.50
HTTP_TIMEOUT = 0.75

# Thrustmaster manual: RZ decreases toward right twist, so invert for
# intuitive right-twist = increasing/right heading.
INVERT_TWIST = False
# Thrustmaster manual: Slider0 is 0 at the forward/+ end, so invert so
# forward throttle = faster movement.
INVERT_THROTTLE = True

# Trigger-click (1.2)
TRIGGER_BUTTON = 1            # joystick button that clicks (joy.cpl numbering)
EARTH_EXE = "arcgisearth"     # matched against the window's program file name
CENTER_OFFSET_X = 0           # nudge the crosshair (screen pixels) if needed
CENTER_OFFSET_Y = 0
RETICLE_SIZE = 80              # crosshair size in pixels (1.3.1; was 48)
RETICLE_WIDTH = 5             # line thickness (1.3.1; was 3)
RETICLE_COLOR = "#ff2020"
CLICK_LOCKOUT_S = 0.8         # one click per pull, never two within a double-click time
ACTIVATE_PAUSE_S = 0.7        # pause between an activating click and the real click
HOVER_BEFORE_S = 0.25         # pointer rests on the object before the click
PRESS_S = 0.08                # how long the button is held down
HOVER_AFTER_S = 0.4           # pointer stays on the object after the click


# Wormholes (1.3)
GATES_FOLDER = "Gates"        # beside EarthStick.py
GATE_EXIT_M = 300.0           # arrive this far past the partner gate
GATE_COOLDOWN_S = 2.0         # no second jump within this time
GATE_MAX_RANGE_M = 50000.0    # gates farther away than this are not checked


class EarthAPIError(RuntimeError):
    pass


def clamp(v: float, lo: float, hi: float) -> float:
    return lo if v < lo else hi if v > hi else v


def deadzone(v: float, dz: float = DEADZONE) -> float:
    if abs(v) <= dz:
        return 0.0
    sign = 1.0 if v > 0 else -1.0
    return sign * (abs(v) - dz) / (1.0 - dz)


def norm_centered(raw: int, lo: int, hi: int) -> float:
    if hi <= lo:
        return 0.0
    unit = (float(raw) - float(lo)) / float(hi - lo)
    return clamp(unit * 2.0 - 1.0, -1.0, 1.0)


def norm_unit(raw: int, lo: int, hi: int) -> float:
    if hi <= lo:
        return 0.0
    return clamp((float(raw) - float(lo)) / float(hi - lo), 0.0, 1.0)


def speed_from_throttle(throttle: float, altitude_m: float) -> float:
    """Altitude-aware max speed with fine low-speed control."""
    throttle = clamp(throttle, 0.0, 1.0)
    max_speed = clamp(max(8.0, altitude_m * 0.020), 8.0, 12000.0) * 60.0
    min_speed = 0.50
    return min_speed + (max_speed - min_speed) * (throttle ** 2.0)


def move_lonlat(lon: float, lat: float, heading_deg: float,
                forward_m: float, right_m: float) -> tuple[float, float]:
    """Small-step heading-relative movement on WGS84-like sphere."""
    h = math.radians(heading_deg)
    north_m = forward_m * math.cos(h) - right_m * math.sin(h)
    east_m = forward_m * math.sin(h) + right_m * math.cos(h)

    lat_rad = math.radians(lat)
    dlat = north_m / EARTH_RADIUS_M
    coslat = max(0.001, abs(math.cos(lat_rad)))
    dlon = east_m / (EARTH_RADIUS_M * coslat)

    lat2 = clamp(lat + math.degrees(dlat), -89.9, 89.9)
    lon2 = lon + math.degrees(dlon)
    lon2 = ((lon2 + 180.0) % 360.0) - 180.0
    return lon2, lat2


# ArcGIS Earth runs on this computer, so its API must never be sent through a
# system or agency proxy (urllib would otherwise use the Windows proxy setting).
_LOCAL_OPENER = urllib.request.build_opener(urllib.request.ProxyHandler({}))


def http_json(method: str, url: str, body=None):
    data = None
    headers = {"Accept": "application/json"}
    if body is not None:
        data = json.dumps(body, separators=(",", ":")).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with _LOCAL_OPENER.open(req, timeout=HTTP_TIMEOUT) as resp:
            raw = resp.read()
            if not raw:
                return None
            return json.loads(raw.decode("utf-8"))
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError, json.JSONDecodeError) as exc:
        raise EarthAPIError(str(exc)) from exc


def get_camera():
    cam = http_json("GET", CAMERA_URL)
    if not isinstance(cam, dict) or not isinstance(cam.get("position"), dict):
        raise EarthAPIError("Unexpected camera response")

    pos = cam["position"]
    sr = pos.get("spatialReference") or {}
    if not isinstance(sr, dict):
        raise EarthAPIError("Unexpected camera spatial reference")
    wkid = sr.get("wkid")
    if wkid not in (4326, "4326", None):
        raise EarthAPIError(f"Camera spatial reference is {wkid}; EarthStick requires WKID 4326")

    try:
        x = float(pos["x"])
        y = float(pos["y"])
        z = float(pos["z"])
        heading = float(cam.get("heading", 0.0))
        tilt = float(cam.get("tilt", 0.0))
        roll = float(cam.get("roll", 0.0))
    except (KeyError, TypeError, ValueError, OverflowError) as exc:
        raise EarthAPIError(f"Invalid camera response: {exc}") from exc

    if not all(math.isfinite(v) for v in (x, y, z, heading, tilt, roll)):
        raise EarthAPIError("Camera response contains non-finite numeric values")

    # Preserve all documented camera properties.
    return {
        "position": {
            "x": x,
            "y": y,
            "z": z,
            "spatialReference": {"wkid": 4326},
        },
        "heading": heading,
        "tilt": tilt,
        "roll": roll,
    }


def put_camera(cam):
    http_json("PUT", CAMERA_URL, cam)


# --- Windows Multimedia Joystick API ---------------------------------------

MAXPNAMELEN = 32
MAX_JOYSTICKOEMVXDNAME = 260
JOY_RETURNX = 0x00000001
JOY_RETURNY = 0x00000002
JOY_RETURNZ = 0x00000004
JOY_RETURNR = 0x00000008
JOY_RETURNU = 0x00000010
JOY_RETURNV = 0x00000020
JOY_RETURNPOV = 0x00000040
JOY_RETURNBUTTONS = 0x00000080
JOY_RETURNALL = 0x000000FF
JOYERR_NOERROR = 0
JOY_POVCENTERED = 0xFFFF


class JOYCAPS(ctypes.Structure):
    _fields_ = [
        ("wMid", wintypes.WORD),
        ("wPid", wintypes.WORD),
        ("szPname", wintypes.WCHAR * MAXPNAMELEN),
        ("wXmin", wintypes.UINT), ("wXmax", wintypes.UINT),
        ("wYmin", wintypes.UINT), ("wYmax", wintypes.UINT),
        ("wZmin", wintypes.UINT), ("wZmax", wintypes.UINT),
        ("wNumButtons", wintypes.UINT),
        ("wPeriodMin", wintypes.UINT), ("wPeriodMax", wintypes.UINT),
        ("wRmin", wintypes.UINT), ("wRmax", wintypes.UINT),
        ("wUmin", wintypes.UINT), ("wUmax", wintypes.UINT),
        ("wVmin", wintypes.UINT), ("wVmax", wintypes.UINT),
        ("wCaps", wintypes.UINT),
        ("wMaxAxes", wintypes.UINT), ("wNumAxes", wintypes.UINT),
        ("wMaxButtons", wintypes.UINT),
        ("szRegKey", wintypes.WCHAR * MAXPNAMELEN),
        ("szOEMVxD", wintypes.WCHAR * MAX_JOYSTICKOEMVXDNAME),
    ]


class JOYINFOEX(ctypes.Structure):
    _fields_ = [
        ("dwSize", wintypes.DWORD), ("dwFlags", wintypes.DWORD),
        ("dwXpos", wintypes.DWORD), ("dwYpos", wintypes.DWORD),
        ("dwZpos", wintypes.DWORD), ("dwRpos", wintypes.DWORD),
        ("dwUpos", wintypes.DWORD), ("dwVpos", wintypes.DWORD),
        ("dwButtons", wintypes.DWORD), ("dwButtonNumber", wintypes.DWORD),
        ("dwPOV", wintypes.DWORD),
        ("dwReserved1", wintypes.DWORD), ("dwReserved2", wintypes.DWORD),
    ]


class WinJoystick:
    def __init__(self, preferred_name: str = TARGET_NAME):
        if os.name != "nt":
            raise RuntimeError("EarthStick requires Windows")
        self.winmm = ctypes.WinDLL("winmm")
        self.winmm.joyGetNumDevs.restype = wintypes.UINT
        self.winmm.joyGetDevCapsW.argtypes = [wintypes.UINT, ctypes.POINTER(JOYCAPS), wintypes.UINT]
        self.winmm.joyGetDevCapsW.restype = wintypes.UINT
        self.winmm.joyGetPosEx.argtypes = [wintypes.UINT, ctypes.POINTER(JOYINFOEX)]
        self.winmm.joyGetPosEx.restype = wintypes.UINT
        self.id, self.caps = self._find(preferred_name)
        self.slider_name, self.slider_field, self.slider_min, self.slider_max = self._detect_slider_axis()

    def _detect_slider_axis(self):
        # T.A320 exposes X, Y, RZ plus one Slider0 axis. WinMM can place
        # that slider on Z, U, or V depending on the driver mapping.
        # Use the axis capability flags instead of assuming U.
        JOYCAPS_HASZ = 0x0001
        JOYCAPS_HASU = 0x0004
        JOYCAPS_HASV = 0x0008
        candidates = [
            ("Z", "dwZpos", self.caps.wZmin, self.caps.wZmax, JOYCAPS_HASZ),
            ("U", "dwUpos", self.caps.wUmin, self.caps.wUmax, JOYCAPS_HASU),
            ("V", "dwVpos", self.caps.wVmin, self.caps.wVmax, JOYCAPS_HASV),
        ]
        present = [
            (name, field, lo, hi)
            for name, field, lo, hi, flag in candidates
            if (self.caps.wCaps & flag) and hi > lo
        ]
        if len(present) != 1:
            names = ", ".join(name for name, _, _, _ in present) or "none"
            raise RuntimeError(f"Could not identify Slider0 axis uniquely (Z/U/V present: {names})")
        return present[0]

    def _connected(self, joy_id: int) -> bool:
        ji = JOYINFOEX()
        ji.dwSize = ctypes.sizeof(JOYINFOEX)
        ji.dwFlags = JOY_RETURNALL
        return self.winmm.joyGetPosEx(joy_id, ctypes.byref(ji)) == JOYERR_NOERROR

    def _find(self, preferred_name: str):
        connected = []
        for joy_id in range(int(self.winmm.joyGetNumDevs())):
            caps = JOYCAPS()
            rc = self.winmm.joyGetDevCapsW(joy_id, ctypes.byref(caps), ctypes.sizeof(caps))
            if rc == JOYERR_NOERROR and self._connected(joy_id):
                connected.append((joy_id, caps))
        if not connected:
            raise RuntimeError("No Windows joystick is connected")
        preferred = preferred_name.casefold()
        for joy_id, caps in connected:
            if preferred in caps.szPname.casefold():
                return joy_id, caps

        # Some Windows/Thrustmaster installations expose only the generic
        # WinMM driver name ("Microsoft PC-joystick driver") even though
        # joy.cpl correctly shows "T.A320 Pilot". Fall back to the known
        # T.A320 control capabilities: 4 axes, 17 buttons, and a POV hat.
        JOYCAPS_HASPOV = 0x0010
        matches = [
            (joy_id, caps) for joy_id, caps in connected
            if caps.wNumAxes >= 4
            and caps.wNumButtons == 17
            and (caps.wCaps & JOYCAPS_HASPOV)
        ]
        if len(matches) == 1:
            return matches[0]

        names = ", ".join(c.szPname for _, c in connected)
        raise RuntimeError(f"{preferred_name!r} not found uniquely. Connected: {names}")

    def read(self):
        ji = JOYINFOEX()
        ji.dwSize = ctypes.sizeof(JOYINFOEX)
        ji.dwFlags = JOY_RETURNALL
        rc = self.winmm.joyGetPosEx(self.id, ctypes.byref(ji))
        if rc != JOYERR_NOERROR:
            raise RuntimeError(f"Joystick read failed ({rc})")

        x = deadzone(norm_centered(ji.dwXpos, self.caps.wXmin, self.caps.wXmax))
        y = deadzone(norm_centered(ji.dwYpos, self.caps.wYmin, self.caps.wYmax))
        rz = deadzone(norm_centered(ji.dwRpos, self.caps.wRmin, self.caps.wRmax))
        if INVERT_TWIST:
            rz = -rz

        throttle_raw = getattr(ji, self.slider_field)
        throttle = norm_unit(throttle_raw, self.slider_min, self.slider_max)
        if INVERT_THROTTLE:
            throttle = 1.0 - throttle

        pov = int(ji.dwPOV)
        tilt_axis = 0.0
        if pov != JOY_POVCENTERED:
            # hundredths of a degree: 0=up, 9000=right, 18000=down, 27000=left
            angle = pov % 36000
            if angle <= 4500 or angle >= 31500:
                tilt_axis = 1.0
            elif 13500 <= angle <= 22500:
                tilt_axis = -1.0

        return {
            "strafe": x,
            "forward": -y,
            "yaw": rz,
            "throttle": throttle,
            "tilt": tilt_axis,
            "buttons": int(ji.dwButtons),
        }


def wait_for_joystick_reconnect(factory=None, sleep_fn=None):
    """Wait for the configured joystick to become available again."""
    if factory is None:
        factory = WinJoystick
    if sleep_fn is None:
        sleep_fn = time.sleep

    while True:
        try:
            return factory()
        except RuntimeError:
            sleep_fn(1.0)


def print_status(name: str, state, cam, speed: float, active: bool):
    status = "FLY" if active else "IDLE"
    line = (
        f"{status:<4}  X {state['strafe']:+.2f}  Y {state['forward']:+.2f}  "
        f"RZ {state['yaw']:+.2f}  THR {state['throttle']:.2f}  "
        f"SPD {speed:7.1f} m/s  HDG {cam['heading']:6.1f}  TILT {cam['tilt']:5.1f}"
    )
    sys.stdout.write("\r" + line[:150].ljust(150))
    sys.stdout.flush()


# ---------------------------------------------------------------------------
# Trigger-click (1.2). Everything here is optional: if any part fails, EarthStick
# flies exactly as before. The crosshair window and the clicking run in their own
# thread so the flying loop never waits for them.

def window_center(rect, off_x=0, off_y=0):
    left, top, right, bottom = rect
    return (left + right) // 2 + off_x, (top + bottom) // 2 + off_y


def is_earth_exe(path, needle=EARTH_EXE):
    name = os.path.basename(path or "").lower()
    return name.endswith(".exe") and needle in name


class TriggerGate:
    """Fires once per trigger pull, and never twice within CLICK_LOCKOUT_S."""
    def __init__(self, lockout=CLICK_LOCKOUT_S):
        self.lockout = lockout
        self.was_down = False
        self.last = None

    def update(self, down, now):
        fire = down and not self.was_down
        self.was_down = down
        if not fire:
            return False
        if self.last is not None and now - self.last < self.lockout:
            return False
        self.last = now
        return True


class TriggerClick:
    """Crosshair overlay + simulated mouse click, run in a background thread."""

    def __init__(self):
        import queue
        import threading
        self.requests = queue.Queue()
        self.ready = threading.Event()
        self.error = None
        self.gate = TriggerGate()
        self.thread = threading.Thread(target=self._thread_main, name="TriggerClick", daemon=True)

    @classmethod
    def start(cls):
        """Start the crosshair; returns the TriggerClick, or None (with the reason printed)."""
        try:
            tc = cls()
            tc.thread.start()
            tc.ready.wait(5.0)
            if tc.error or not tc.ready.is_set():
                raise RuntimeError(tc.error or "crosshair did not start")
            print(f"Trigger-click: ready (button {TRIGGER_BUTTON} clicks the object under the red crosshair)")
            return tc
        except Exception as exc:
            print(f"Trigger-click: unavailable ({exc}); flying is not affected.")
            return None

    def on_buttons(self, buttons):
        """Called from the flying loop with the button mask; never blocks."""
        down = bool(buttons & (1 << (TRIGGER_BUTTON - 1)))
        if self.gate.update(down, time.perf_counter()):
            self.requests.put("click")

    # -- everything below runs in the TriggerClick thread ------------------
    def _thread_main(self):
        try:
            self._setup_windows()
            import tkinter as tk
            self.root = tk.Tk()
            self.root.withdraw()
            ov = tk.Toplevel(self.root)
            ov.overrideredirect(True)
            ov.attributes("-topmost", True)
            key = "#010203"
            ov.configure(bg=key)
            ov.attributes("-transparentcolor", key)
            s = RETICLE_SIZE
            c = tk.Canvas(ov, width=s, height=s, bg=key, highlightthickness=0)
            c.pack()
            m, gap = s // 2, 8
            for x0, y0, x1, y1 in ((0, m, m - gap, m), (m + gap, m, s, m), (m, 0, m, m - gap), (m, m + gap, m, s)):
                c.create_line(x0, y0, x1, y1, fill=RETICLE_COLOR, width=RETICLE_WIDTH)
            c.create_oval(m - 3, m - 3, m + 3, m + 3, outline=RETICLE_COLOR, fill=RETICLE_COLOR)
            ov.update_idletasks()
            self._click_through(ov)
            ov.withdraw()
            self.overlay = ov
            self.center = None
            self.ready.set()
            self.root.after(100, self._track)
            self.root.after(50, self._serve)
            self.root.mainloop()
        except Exception as exc:
            self.error = str(exc) or type(exc).__name__
            self.ready.set()

    def _setup_windows(self):
        self.user32 = ctypes.WinDLL("user32")
        self.kernel32 = ctypes.WinDLL("kernel32")
        self.user32.GetForegroundWindow.restype = wintypes.HWND
        try:
            self.user32.SetProcessDpiAwarenessContext(ctypes.c_void_p(-4))   # real screen pixels
        except Exception:
            try:
                ctypes.WinDLL("shcore").SetProcessDpiAwareness(2)
            except Exception:
                pass
        self.earth_hwnd = None

    def _click_through(self, tk_window):
        hwnd = self.user32.GetParent(tk_window.winfo_id()) or tk_window.winfo_id()
        style = self.user32.GetWindowLongW(hwnd, -20)                       # GWL_EXSTYLE
        style |= 0x00080000 | 0x00000020 | 0x00000080 | 0x08000000           # layered, transparent, toolwindow, noactivate
        self.user32.SetWindowLongW(hwnd, -20, style)

    def _exe_of(self, hwnd):
        pid = wintypes.DWORD()
        self.user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
        h = self.kernel32.OpenProcess(0x1000, False, pid.value)              # query limited information
        if not h:
            return ""
        try:
            buf = ctypes.create_unicode_buffer(1024)
            size = wintypes.DWORD(len(buf))
            return buf.value if self.kernel32.QueryFullProcessImageNameW(h, 0, buf, ctypes.byref(size)) else ""
        finally:
            self.kernel32.CloseHandle(h)

    def _earth_rect(self):
        found = []
        EnumProc = ctypes.WINFUNCTYPE(ctypes.c_bool, wintypes.HWND, wintypes.LPARAM)

        def callback(hwnd, _):
            if self.user32.IsWindowVisible(hwnd) and not self.user32.IsIconic(hwnd) and is_earth_exe(self._exe_of(hwnd)):
                r = wintypes.RECT()
                if self.user32.GetWindowRect(hwnd, ctypes.byref(r)):
                    w, h = r.right - r.left, r.bottom - r.top
                    if w > 200 and h > 200:
                        found.append((w * h, (r.left, r.top, r.right, r.bottom), hwnd))
            return True

        self.user32.EnumWindows(EnumProc(callback), 0)
        if not found:
            self.earth_hwnd = None
            return None
        best = max(found, key=lambda f: f[0])
        self.earth_hwnd = best[2]
        return best[1]

    def _track(self):
        try:
            rect = self._earth_rect()
            if rect is None:
                self.center = None
                self.overlay.withdraw()
            else:
                self.center = window_center(rect, CENTER_OFFSET_X, CENTER_OFFSET_Y)
                x, y = self.center
                half = RETICLE_SIZE // 2
                self.overlay.geometry(f"{RETICLE_SIZE}x{RETICLE_SIZE}+{x - half}+{y - half}")
                self.overlay.deiconify()
                self.overlay.attributes("-topmost", True)
        except Exception:
            pass
        self.root.after(400, self._track)

    def _serve(self):
        try:
            while True:
                self.requests.get_nowait()
                if self.center is not None:
                    self._fire(*self.center)
        except Exception:
            pass
        self.root.after(30, self._serve)

    def _earth_active(self):
        fg = self.user32.GetForegroundWindow()
        return bool(self.earth_hwnd) and bool(fg) and self._exe_of(fg) == self._exe_of(self.earth_hwnd)

    def _click(self, x, y):
        old = wintypes.POINT()
        self.user32.GetCursorPos(ctypes.byref(old))
        steps = 12
        for i in range(1, steps + 1):          # glide onto the target like a real mouse
            self.user32.SetCursorPos(int(old.x + (x - old.x) * i / steps), int(old.y + (y - old.y) * i / steps))
            time.sleep(0.01)
        time.sleep(HOVER_BEFORE_S)
        self.user32.mouse_event(0x0002, 0, 0, 0, 0)    # left down
        time.sleep(PRESS_S)
        self.user32.mouse_event(0x0004, 0, 0, 0, 0)    # left up
        time.sleep(HOVER_AFTER_S)
        self.user32.SetCursorPos(old.x, old.y)

    def _fire(self, x, y):
        self.overlay.withdraw()                         # crosshair out of the way
        self.root.update()
        try:
            if not self._earth_active():
                self._click(x, y)                       # first click makes ArcGIS Earth active
                time.sleep(ACTIVATE_PAUSE_S)            # longer than a double-click
            self._click(x, y)
        finally:
            self.overlay.deiconify()
            self.overlay.attributes("-topmost", True)


# ---------------------------------------------------------------------------
# Wormholes (1.3). A gate is a vertical ring: centre (lat, lon, alt_m absolute),
# radius_m, and facing = compass direction a pilot flies to go through it.

_KML_NS = "{http://www.opengis.net/kml/2.2}"


def _gate_from_placemark(pm):
    data = {}
    for d in pm.iter(_KML_NS + "Data"):
        v = d.find(_KML_NS + "value")
        data[(d.get("name") or "").strip().lower()] = (v.text or "").strip() if v is not None else ""
    if data.get("gate", "").lower() not in ("1", "yes", "true"):
        return None
    name_el = pm.find(_KML_NS + "name")
    gate = {"name": (name_el.text or "").strip() if name_el is not None else ""}
    for k in ("lat", "lon", "alt_m", "radius_m", "facing"):
        gate[k] = float(data[k])
    gate["to"] = data.get("to", "")
    if not gate["to"]:
        for k in ("dest_lat", "dest_lon", "dest_alt_m", "dest_heading"):
            gate[k] = float(data[k])
    for k, v in gate.items():
        if isinstance(v, float) and not math.isfinite(v):
            raise ValueError(f"gate {gate['name']!r}: {k} is not a number")
    if not (-90 <= gate["lat"] <= 90 and -180 <= gate["lon"] <= 180 and gate["radius_m"] > 0):
        raise ValueError(f"gate {gate['name']!r}: bad position or radius")
    return gate


def load_gates(folder):
    """Read every gate in *.kmz / *.kml in folder. Returns (gates, problems)."""
    gates, problems = [], []
    folder = Path(folder)
    if not folder.is_dir():
        return gates, problems
    for f in sorted(folder.iterdir()):
        if f.suffix.lower() not in (".kmz", ".kml"):
            continue
        try:
            if f.suffix.lower() == ".kmz":
                with zipfile.ZipFile(f) as z:
                    name = next((n for n in z.namelist() if n.lower().endswith(".kml")), None)
                    if name is None:
                        raise ValueError("no KML inside")
                    root = ET.fromstring(z.read(name))
            else:
                root = ET.parse(f).getroot()
            for pm in root.iter(_KML_NS + "Placemark"):
                try:
                    g = _gate_from_placemark(pm)
                except (KeyError, ValueError) as exc:
                    problems.append(f"{f.name}: {exc}")
                    continue
                if g is not None:
                    g["file"] = f.name
                    gates.append(g)
        except Exception as exc:
            problems.append(f"{f.name}: {exc}")
    kept = []
    for g in gates:
        if g["to"]:
            same = [p for p in gates if p is not g and p["file"] == g["file"] and p["name"] == g["to"]]
            other = [p for p in gates if p["file"] != g["file"] and p["name"] == g["to"]]
            if len(same) == 1:
                g["partner"] = same[0]
            elif not same and len(other) == 1:
                g["partner"] = other[0]
            else:
                where = "is not in the Gates folder" if not (same or other) else "matches more than one gate"
                problems.append(f"{g['file']}: gate {g['name']!r} leads to {g['to']!r}, which {where}")
                continue
        kept.append(g)
    return kept, problems


def _local_xyz(lat0, lon0, lat, lon, alt):
    k = math.pi / 180.0 * EARTH_RADIUS_M
    return ((lon - lon0) * k * math.cos(math.radians(lat0)), (lat - lat0) * k, alt)


def gate_crossed(gate, p0, p1):
    """True if the move p0 -> p1 ((lon, lat, alt) each) passes forwards through the ring."""
    a = _local_xyz(gate["lat"], gate["lon"], p0[1], p0[0], p0[2] - gate["alt_m"])
    b = _local_xyz(gate["lat"], gate["lon"], p1[1], p1[0], p1[2] - gate["alt_m"])
    if math.hypot(a[0], a[1]) > GATE_MAX_RANGE_M:
        return False
    f = math.radians(gate["facing"])
    n = (math.sin(f), math.cos(f), 0.0)
    d0 = a[0] * n[0] + a[1] * n[1]
    d1 = b[0] * n[0] + b[1] * n[1]
    if not (d0 < 0.0 <= d1):          # forwards only
        return False
    s = d0 / (d0 - d1)
    q = [a[i] + s * (b[i] - a[i]) for i in range(3)]
    return math.sqrt(q[0] ** 2 + q[1] ** 2 + q[2] ** 2) <= gate["radius_m"]


def gate_arrival(gate, gates):
    """(lon, lat, alt_m, heading) where a jump through gate lands."""
    if gate["to"]:
        p = gate.get("partner") or next(g for g in gates if g["name"] == gate["to"])
        heading = (p["facing"] + 180.0) % 360.0      # away from the partner ring
        lon, lat = move_lonlat(p["lon"], p["lat"], heading, GATE_EXIT_M, 0.0)
        return lon, lat, p["alt_m"], heading
    return gate["dest_lon"], gate["dest_lat"], gate["dest_alt_m"], gate["dest_heading"] % 360.0


def gate_label(gate):
    return gate["name"]


def run():
    print(f"EarthStick {VERSION}")
    print("Minimal T.A320 Pilot -> ArcGIS Earth bridge")
    print("Button 4 = descend/zoom in; Button 3 = climb/zoom out; neutral = hover.")
    print(f"Button {TRIGGER_BUTTON} (trigger) = click the object under the crosshair.")
    print()

    if os.name != "nt":
        raise RuntimeError("EarthStick requires Windows")

    # Same retry used after a mid-flight unplug, so EarthStick can be started
    # before the joystick is plugged in.
    try:
        joy = WinJoystick()
    except RuntimeError as exc:
        print(f"Joystick not ready: {exc}")
        print("Waiting for the joystick - plug it in or check joy.cpl. Ctrl+C to stop.")
        joy = wait_for_joystick_reconnect()
    print(f"Joystick: {joy.caps.szPname}  (Windows ID {joy.id})")
    print(f"Slider0 source: WinMM {joy.slider_name} axis")
    print(f"Waiting for ArcGIS Earth Automation API at {BASE_URL} ...")

    cam = None
    last_reason = None
    while cam is None:
        try:
            cam = get_camera()
        except EarthAPIError as exc:
            reason = str(exc)
            if reason != last_reason:
                print(f"  Still waiting: {reason}")
                print("  Check that ArcGIS Earth is open with Automation API enabled "
                      "(Settings > Advanced).")
                last_reason = reason
            time.sleep(1.0)
    print("ArcGIS Earth: connected")
    clicker = TriggerClick.start()
    gates, gate_problems = load_gates(Path(__file__).resolve().parent / GATES_FOLDER)
    for msg in gate_problems:
        print(f"Wormholes: skipped - {msg}")
    if gates:
        print(f"Wormholes: {len(gates)} gate(s) armed: " + ", ".join(gate_label(g) for g in gates))
    else:
        print(f"Wormholes: none (put gate files in the {GATES_FOLDER} folder beside EarthStick.py)")
    last_jump = -1e9
    print("Close this window or press Ctrl+C to stop EarthStick.\n")

    dt_target = 1.0 / POLL_HZ
    last_t = time.perf_counter()
    last_idle_sync = time.perf_counter()
    was_active = False
    last_status = 0.0
    api_fault = False

    while True:
        loop_start = time.perf_counter()

        # After any API fault, do not send another camera write until a fresh
        # camera has been read from ArcGIS Earth. This prevents stale local
        # movement from accumulating while Earth/API communication is down.
        if api_fault:
            try:
                cam = get_camera()
            except EarthAPIError:
                time.sleep(0.25)
                continue

            api_fault = False
            last_t = time.perf_counter()
            last_idle_sync = last_t
            was_active = False
            sys.stdout.write("\nArcGIS Earth: reconnected; camera re-synchronized.\n")
            sys.stdout.flush()
            continue

        dt = clamp(loop_start - last_t, 0.001, 0.10)
        last_t = loop_start

        try:
            state = joy.read()
        except RuntimeError as exc:
            sys.stdout.write(f"\nJoystick connection lost: {exc}\nWaiting for joystick to reconnect...\n")
            sys.stdout.flush()

            joy = wait_for_joystick_reconnect()
            sys.stdout.write(
                f"Joystick: reconnected as {joy.caps.szPname}  "
                f"(Windows ID {joy.id}); Slider0 source: WinMM {joy.slider_name} axis\n"
            )
            sys.stdout.flush()

            # Re-read the live ArcGIS Earth camera before accepting any new
            # joystick movement. If the API is also unavailable, the
            # API recovery path takes ownership of the wait.
            try:
                cam = get_camera()
            except EarthAPIError:
                api_fault = True
                sys.stdout.write(
                    "ArcGIS Earth connection unavailable after joystick reconnect. "
                    "Waiting to re-synchronize...\n"
                )
                sys.stdout.flush()

            last_t = time.perf_counter()
            last_idle_sync = last_t
            was_active = False
            continue

        if clicker is not None:
            clicker.on_buttons(state["buttons"])

        # Button 4 (red trigger) = zoom in.
        # Button 3 (black thumb) = zoom out.
        zoom_in = bool(state["buttons"] & (1 << (4 - 1)))
        zoom_out = bool(state["buttons"] & (1 << (3 - 1)))
        zoom_dir = (1 if zoom_out else 0) - (1 if zoom_in else 0)

        active = (
            any(abs(state[k]) > 0.0 for k in ("strafe", "forward", "yaw", "tilt"))
            or zoom_dir != 0
        )

        # Re-sync from Earth when the user first moves the stick, so mouse navigation
        # performed while idle is respected.
        if active and not was_active:
            try:
                cam = get_camera()
            except EarthAPIError:
                api_fault = True
                sys.stdout.write("\nArcGIS Earth connection lost. Holding position; waiting to re-synchronize...\n")
                sys.stdout.flush()
                time.sleep(0.25)
                continue

        if active:
            # Work on a temporary camera. The confirmed local camera is updated
            # only after ArcGIS Earth accepts the PUT.
            next_cam = {
                "position": dict(cam["position"]),
                "heading": cam["heading"],
                "tilt": cam["tilt"],
                "roll": cam["roll"],
            }
            pos = next_cam["position"]

            # Continuous altitude-only zoom.
            # Zoom rate scales with current altitude: roughly 75% of current
            # altitude per second while held, with a 2 m/s floor near ground.
            if zoom_dir != 0:
                zoom_rate_mps = max(2.0, float(pos["z"]) * 0.75)
                pos["z"] = max(1.0, float(pos["z"]) + zoom_dir * zoom_rate_mps * dt)

            speed = speed_from_throttle(state["throttle"], pos["z"])

            # Translation uses current heading.
            travel = speed * dt
            lon, lat = move_lonlat(
                pos["x"], pos["y"], next_cam["heading"],
                state["forward"] * travel,
                state["strafe"] * travel,
            )
            pos["x"] = lon
            pos["y"] = lat

            next_cam["heading"] = (next_cam["heading"] + state["yaw"] * YAW_RATE_DPS * dt) % 360.0
            next_cam["tilt"] = clamp(next_cam["tilt"] + state["tilt"] * TILT_RATE_DPS * dt, 0.0, 180.0)

            jumped = None
            if gates and loop_start - last_jump >= GATE_COOLDOWN_S:
                p0 = (float(cam["position"]["x"]), float(cam["position"]["y"]), float(cam["position"]["z"]))
                p1 = (float(pos["x"]), float(pos["y"]), float(pos["z"]))
                for g in gates:
                    if gate_crossed(g, p0, p1):
                        lon, lat, alt, heading = gate_arrival(g, gates)
                        pos["x"], pos["y"], pos["z"] = lon, lat, alt
                        next_cam["heading"] = heading
                        jumped = g
                        break

            try:
                put_camera(next_cam)
            except EarthAPIError:
                api_fault = True
                sys.stdout.write("\nArcGIS Earth connection lost. Holding position; waiting to re-synchronize...\n")
                sys.stdout.flush()
                time.sleep(0.25)
                continue

            cam = next_cam
            if jumped is not None:
                last_jump = loop_start
                sys.stdout.write(f"\nWormhole: through the {jumped['name']} gate.\n")
                sys.stdout.flush()
        else:
            speed = speed_from_throttle(state["throttle"], cam["position"]["z"])
            if loop_start - last_idle_sync >= IDLE_RESYNC_SECONDS:
                try:
                    cam = get_camera()
                except EarthAPIError:
                    api_fault = True
                    sys.stdout.write("\nArcGIS Earth connection lost. Holding position; waiting to re-synchronize...\n")
                    sys.stdout.flush()
                    time.sleep(0.25)
                    continue
                last_idle_sync = loop_start

        if loop_start - last_status >= 0.10:
            print_status(joy.caps.szPname, state, cam, speed, active)
            last_status = loop_start

        was_active = active
        elapsed = time.perf_counter() - loop_start
        if elapsed < dt_target:
            time.sleep(dt_target - elapsed)


def selftest():
    # Deadzone
    assert deadzone(0.0) == 0.0
    assert deadzone(0.05) == 0.0
    assert deadzone(1.0) == 1.0
    assert deadzone(-1.0) == -1.0

    # Normalization
    assert abs(norm_centered(0, 0, 100) + 1.0) < 1e-9
    assert abs(norm_centered(50, 0, 100)) < 1e-9
    assert abs(norm_centered(100, 0, 100) - 1.0) < 1e-9

    # Heading-relative movement sanity checks.
    lon, lat = move_lonlat(-81.65, 30.33, 0.0, 1000.0, 0.0)
    assert lat > 30.33 and abs(lon + 81.65) < 1e-6
    lon, lat = move_lonlat(-81.65, 30.33, 90.0, 1000.0, 0.0)
    assert lon > -81.65 and abs(lat - 30.33) < 1e-6
    lon, lat = move_lonlat(-81.65, 30.33, 0.0, 0.0, 1000.0)
    assert lon > -81.65 and abs(lat - 30.33) < 1e-6

    assert 0.5 <= speed_from_throttle(0.0, 3000.0) < speed_from_throttle(1.0, 3000.0)

    # Camera response validation for API fault isolation.
    original_http_json = globals()["http_json"]
    try:
        globals()["http_json"] = lambda method, url, body=None: {
            "position": {
                "x": -81.65,
                "y": 30.33,
                "z": 1000.0,
                "spatialReference": {"wkid": 4326},
            },
            "heading": 90.0,
            "tilt": 45.0,
            "roll": 0.0,
        }
        cam = get_camera()
        assert cam["position"]["x"] == -81.65

        globals()["http_json"] = lambda method, url, body=None: {
            "position": {"x": "bad", "y": 30.33, "z": 1000.0}
        }
        try:
            get_camera()
            raise AssertionError("Malformed camera response was not rejected")
        except EarthAPIError:
            pass
    finally:
        globals()["http_json"] = original_http_json

    # Simulate two failed joystick detection attempts followed by a
    # successful reconnect without sleeping.
    attempts = {"count": 0}
    marker = object()

    def fake_factory():
        attempts["count"] += 1
        if attempts["count"] < 3:
            raise RuntimeError("simulated joystick missing")
        return marker

    slept = []
    reconnected = wait_for_joystick_reconnect(fake_factory, slept.append)
    assert reconnected is marker
    assert attempts["count"] == 3
    assert slept == [1.0, 1.0]

    # Trigger-click (1.2)
    assert window_center((0, 0, 1200, 2000)) == (600, 1000)
    assert window_center((100, 50, 1300, 2050), 5, -10) == (705, 1040)
    assert is_earth_exe(r"C:\Program Files\ArcGIS\Earth\ArcGISEarth.exe")
    assert not is_earth_exe(r"C:\Windows\explorer.exe") and not is_earth_exe("")
    g = TriggerGate(0.8)
    # press, hold, release, press too soon, release, press later
    assert [g.update(d, t) for d, t in ((True, 0.0), (True, 0.1), (False, 0.2), (True, 0.5),
                                         (False, 0.6), (True, 1.0))] == [True, False, False, False, False, True]
    assert TRIGGER_BUTTON not in (3, 4)
    assert ACTIVATE_PAUSE_S > 0.5 and CLICK_LOCKOUT_S > ACTIVATE_PAUSE_S

    # Wormholes (1.3): a ring facing north over (30.0, -81.0) at 500 m, radius 150 m.
    g = {"name": "A", "lat": 30.0, "lon": -81.0, "alt_m": 500.0, "radius_m": 150.0, "facing": 0.0, "to": "B"}
    b = {"name": "B", "lat": 40.0, "lon": -74.0, "alt_m": 400.0, "radius_m": 150.0, "facing": 210.0, "to": "A"}
    south, north = move_lonlat(-81.0, 30.0, 180.0, 50.0, 0.0), move_lonlat(-81.0, 30.0, 0.0, 50.0, 0.0)
    assert gate_crossed(g, (*south, 520.0), (*north, 520.0))                 # through the ring, forwards
    assert not gate_crossed(g, (*north, 520.0), (*south, 520.0))             # backwards: no jump
    assert not gate_crossed(g, (*south, 900.0), (*north, 900.0))             # above the ring
    east = move_lonlat(-81.0, 30.0, 90.0, 400.0, 0.0)
    assert not gate_crossed(g, (east[0], south[1], 500.0), (east[0], north[1], 500.0))  # beside it
    lon, lat, alt, hd = gate_arrival(g, [g, b])
    assert abs(hd - 30.0) < 1e-9 and alt == 400.0 and lat > 40.0              # past B, facing away
    assert not gate_crossed(b, (-74.0, 40.0, 400.0), (lon, lat, 400.0))      # leaving B does not trigger B
    one = dict(g, to="", dest_lat=1.0, dest_lon=2.0, dest_alt_m=3.0, dest_heading=370.0)
    assert gate_arrival(one, [one]) == (2.0, 1.0, 3.0, 10.0)

    print("EarthStick self-test PASS")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        selftest()
        raise SystemExit(0)
    try:
        run()
    except KeyboardInterrupt:
        print("\nStopped.")
    except Exception as exc:
        # EarthStick.bat pauses after this, so no second prompt here.
        print(f"\nEarthStick stopped: {exc}")
