# EarthStick 1.0 Technical Notes

## Architecture

EarthStick uses the Windows Multimedia joystick API through `ctypes` and the ArcGIS Earth local Automation API through Python's standard `urllib` modules.

```text
TCA Sidestick -> WinMM joyGetPosEx -> EarthStick.py -> HTTP camera GET/PUT -> ArcGIS Earth
```

There are no third-party Python dependencies.

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
```

## Spatial reference

EarthStick expects the ArcGIS Earth camera position in WKID 4326.
