#!/usr/bin/env python3
"""EarthStick 1.0

Thrustmaster T.A320 Pilot -> ArcGIS Earth camera bridge.

Controls:
  X axis       : strafe left/right
  Y axis       : move forward/back
  RZ axis      : heading left/right
  Slider0      : movement speed
  POV up/down  : camera tilt

Button 4 (red top button) zooms in / descends.
Button 3 (black thumb button) zooms out / climbs.
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

VERSION = "1.0"
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


def http_json(method: str, url: str, body=None):
    data = None
    headers = {"Accept": "application/json"}
    if body is not None:
        data = json.dumps(body, separators=(",", ":")).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT) as resp:
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


def run():
    print(f"EarthStick {VERSION}")
    print("Minimal T.A320 Pilot -> ArcGIS Earth bridge")
    print("Button 4 = descend/zoom in; Button 3 = climb/zoom out; neutral = hover.")
    print()

    joy = WinJoystick()
    print(f"Joystick: {joy.caps.szPname}  (Windows ID {joy.id})")
    print(f"Slider0 source: WinMM {joy.slider_name} axis")
    print("Waiting for ArcGIS Earth Automation API at http://localhost:8000 ...")

    cam = None
    while cam is None:
        try:
            cam = get_camera()
        except EarthAPIError:
            time.sleep(1.0)
    print("ArcGIS Earth: connected")
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

            try:
                put_camera(next_cam)
            except EarthAPIError:
                api_fault = True
                sys.stdout.write("\nArcGIS Earth connection lost. Holding position; waiting to re-synchronize...\n")
                sys.stdout.flush()
                time.sleep(0.25)
                continue

            cam = next_cam
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
        print(f"\nEarthStick stopped: {exc}")
        input("Press Enter to close...")
