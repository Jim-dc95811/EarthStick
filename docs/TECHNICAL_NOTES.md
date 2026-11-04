# EarthStick 1.3.2 Technical Notes

## Architecture

EarthStick uses the Windows Multimedia joystick API through `ctypes` and the ArcGIS Earth local Automation API through Python's standard `urllib` modules.

```text
TCA Sidestick -> WinMM joyGetPosEx -> EarthStick.py -> HTTP camera GET/PUT -> ArcGIS Earth
```

There are no third-party Python dependencies. Trigger-click (1.2) uses Tkinter, which ships with the standard python.org installer.

The ArcGIS Earth connection uses a `urllib` opener with an empty `ProxyHandler`, so requests to `localhost` never go through a system or agency proxy (1.1).

## Input model

The program discovers the T.A320 controller by preferred name and includes a capability-based fallback for the tested T.A320 control layout. Slider 0 may appear on WinMM Z, U, or V; EarthStick identifies the single present slider axis from capability flags.

Accepted mappings:

- X -> strafe
- Y -> forward/reverse
- R axis -> twist/heading
- one Z/U/V slider -> speed
- POV up/down -> tilt
- Button 4 -> descend
- Button 3 -> climb
- Button 1 (trigger) -> trigger-click (1.2)

## Movement loop

The loop targets 30 Hz. `dt` is clamped between 0.001 and 0.10 seconds. This prevents a long scheduling stall from becoming one oversized movement step.

## Translation

Heading-relative forward and right movement are resolved to north/east components and converted to latitude/longitude increments using an Earth radius of 6,378,137 m. Latitude is limited to +/-89.9 degrees and longitude wraps at +/-180 degrees.

## Speed

```text
base_max = clamp(max(8.0, altitude_m * 0.020), 8.0, 12000.0)
max_speed = base_max * 60.0
min_speed = 0.50
speed = min_speed + (max_speed - min_speed) * throttle^2
```

The squared throttle curve keeps the low end controllable while allowing rapid long-distance movement at high altitude.

## Heading and tilt

- heading rate: 55 degrees/second at full twist
- tilt rate: 45 degrees/second at full POV command
- heading wraps through 360 degrees
- tilt is clamped from 0 to 180 degrees

## Vertical movement

Button 4 and Button 3 change altitude only.

```text
zoom_rate_mps = max(2.0, altitude * 0.75)
minimum altitude = 1.0 m
```

## Camera synchronization

EarthStick reads the camera before flight starts. While the joystick is idle, it periodically refreshes camera state so normal ArcGIS Earth mouse navigation remains compatible.

For active movement, EarthStick computes the proposed next camera in a temporary copy. The confirmed local camera is updated only after ArcGIS Earth accepts the write.

## API fault isolation

If a camera read or write fails:

1. camera writes stop;
2. no stale movement is accumulated;
3. EarthStick retries the API;
4. after recovery, it reads the current ArcGIS Earth camera;
5. timing state is reset before control resumes.

Malformed or non-finite camera values are treated as API faults.

## Joystick reconnect handling

A WinMM read failure does not terminate the application. EarthStick waits for the joystick to be detected again. Re-detection rebuilds the capabilities and slider mapping, allowing recovery even when Windows returns the controller under a different joystick ID.

After reconnection, EarthStick reads the current ArcGIS Earth camera before accepting joystick movement.

The same wait is used at startup (1.1): if no joystick is found when EarthStick starts, it reports the reason and retries every second instead of exiting.

## Trigger-click (1.2)

The ArcGIS Earth Automation API has no click or selection call, so EarthStick clicks the way a person would: with the Windows mouse.

- **Crosshair:** a small Tkinter window (borderless, always on top, transparent background, click-through via `WS_EX_LAYERED | WS_EX_TRANSPARENT | WS_EX_TOOLWINDOW | WS_EX_NOACTIVATE`) centred on the ArcGIS Earth window. The window is found with `EnumWindows` by its program file name (`arcgisearth` in the .exe name) and re-checked every 0.4 s, so the crosshair follows moves and resizes and hides while ArcGIS Earth is minimized. The process is DPI-aware so the centre is correct on scaled displays.
- **Gate:** one click per trigger pull (edge detection) and never two within `CLICK_LOCKOUT_S = 0.8` s, because a double-click makes ArcGIS Earth zoom in.
- **Click recipe:** an instant pointer jump followed by a click zooms instead of selecting. EarthStick hides the crosshair, glides the pointer to the centre in 12 steps of 10 ms, rests `HOVER_BEFORE_S = 0.25` s, presses for `PRESS_S = 0.08` s, rests `HOVER_AFTER_S = 0.4` s, then restores the pointer and the crosshair. If ArcGIS Earth is not the foreground window, a first click activates it and the real click follows after `ACTIVATE_PAUSE_S = 0.7` s.
- **Isolation:** the crosshair and clicks run in their own thread. The flying loop only hands over the button mask and never waits. If the crosshair cannot start, EarthStick prints `Trigger-click: unavailable (...)` and flies exactly as 1.1.
- Clicking open map closes an open popup, so no separate close button is needed.

## World Gates / wormholes (1.3)

- **Gate files:** every `.kmz`/`.kml` in the `Gates` folder beside `EarthStick.py` is read once at startup. A gate is a Placemark whose `ExtendedData` has `gate=1` plus `lat`, `lon`, `alt_m` (metres above sea level, the same reference as the Automation API camera `z`), `radius_m`, `facing` (compass direction of travel through the ring) and either `to` (partner gate name) or `dest_lat`, `dest_lon`, `dest_alt_m`, `dest_heading` (fixed landing spot). The drawing in the file is only for the eye; EarthStick uses the data.
- **Pairing:** `to` is resolved in the same file first, then by a unique name across files; an ambiguous or missing partner is reported (`Wormholes: skipped - ...`) and that gate is not armed.
- **Crossing test:** each active loop step tests the segment from the last confirmed camera position to the next one, in local metres around the gate (equirectangular, fine within the 50 km check range). The step must cross the ring plane forwards (`d0 < 0 <= d1` along the facing direction) and the crossing point must lie within `radius_m` of the centre. Backwards, outside or above the ring: no jump.
- **Jump:** the next camera position, altitude and heading are replaced by the arrival (partner: `GATE_EXIT_M = 300` m past the partner ring, facing away from it; one-way: the fixed spot), tilt is kept, and the normal PUT sends it. A jump is reported in the console and gates rest for `GATE_COOLDOWN_S = 2.0` s.
- Gates only act while the joystick is moving the camera. With no gate files, the camera stream is byte-identical to 1.2 (335-write replay).
- ArcGIS Earth's status bar **eye alt** is measured from sea level (measured over Atlanta, field elevation ~1,026 ft), so gate files label rings with sea-level feet.

## Constants

```text
POLL_HZ = 30.0
DEADZONE = 0.08
YAW_RATE_DPS = 55.0
TILT_RATE_DPS = 45.0
EARTH_RADIUS_M = 6378137.0
IDLE_RESYNC_SECONDS = 0.50
HTTP_TIMEOUT = 0.75
INVERT_TWIST = False
INVERT_THROTTLE = True
BASE_URL = http://localhost:8000
TRIGGER_BUTTON = 1
CENTER_OFFSET_X = 0, CENTER_OFFSET_Y = 0
RETICLE_SIZE = 80, RETICLE_WIDTH = 5, RETICLE_COLOR = #ff2020 (1.3.1; 1.3 was 48 px with 3 px lines)
CLICK_LOCKOUT_S = 0.8
ACTIVATE_PAUSE_S = 0.7
HOVER_BEFORE_S = 0.25, PRESS_S = 0.08, HOVER_AFTER_S = 0.4
GATES_FOLDER = Gates, GATE_EXIT_M = 300, GATE_COOLDOWN_S = 2.0, GATE_MAX_RANGE_M = 50000
```

## Spatial reference

EarthStick expects the ArcGIS Earth camera position in WKID 4326.
