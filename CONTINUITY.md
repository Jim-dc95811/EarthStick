# CONTINUITY - EarthStick 1.0

## Official baseline

**EarthStick 1.0 is the only current release and the accepted standalone baseline.**

Purpose: use a Thrustmaster TCA Sidestick Airbus Edition to provide direct, helicopter-style free camera navigation in ArcGIS Earth desktop through the ArcGIS Earth Automation API.

The defining interaction is:

> **Neutral controls = stop and hover in place.**

## Accepted controls

- stick forward/back -> fly forward/reverse
- stick left/right -> strafe left/right
- twist/RZ -> heading left/right
- Slider0 -> movement speed
- POV up/down -> camera tilt
- Button 4 red top button -> hold to zoom in / descend
- Button 3 black thumb button -> hold to zoom out / climb
- all other buttons -> unused

## Accepted recovery behavior

- ArcGIS Earth API loss does not terminate EarthStick.
- During API loss, EarthStick does not accumulate stale camera movement.
- After API recovery, EarthStick re-reads the live ArcGIS Earth camera before sending movement again.
- Joystick USB loss does not terminate EarthStick.
- EarthStick retries joystick detection and supports reconnection under a different Windows joystick ID.
- After joystick reconnection, EarthStick re-reads the current ArcGIS Earth camera before accepting movement.
- Malformed or non-finite camera data is rejected as an API fault rather than used as movement state.

## Tested environment

- Windows 11
- Python 3.14.5
- ArcGIS Earth desktop with Automation API enabled
- Thrustmaster TCA Sidestick Airbus Edition
- Windows controller name observed: `T.A320 Pilot`
- local API: `http://localhost:8000`

No third-party Python packages are required.

## Technical constants

- `POLL_HZ = 30.0`
- `DEADZONE = 0.08`
- `YAW_RATE_DPS = 55.0`
- `TILT_RATE_DPS = 45.0`
- `EARTH_RADIUS_M = 6378137.0`
- `IDLE_RESYNC_SECONDS = 0.50`
- `HTTP_TIMEOUT = 0.75`
- `INVERT_TWIST = False`
- `INVERT_THROTTLE = True`

Throttle speed function:

```text
base_max = clamp(max(8.0, altitude_m * 0.020), 8.0, 12000.0)
max_speed = base_max * 60.0
min_speed = 0.50
speed = min_speed + (max_speed - min_speed) * throttle^2
```

Zoom:

```text
zoom_rate_mps = max(2.0, altitude * 0.75)
minimum altitude = 1.0 m
```

## Modification rules

1. Treat EarthStick 1.0 as the protected known-good baseline.
2. Discuss functional changes before making them.
3. Make one functional modification at a time.
4. Preserve control meanings, movement constants, API address, and recovery behavior unless a change is explicitly authorized.
5. Test changed behavior in ArcGIS Earth before replacing the accepted release.
6. Do not assign unused buttons without an operational reason.
7. Do not add dependencies unless they solve a demonstrated need.
8. Keep filenames short and practical.
9. Never describe untested behavior as verified.

## Repository presentation

The repository intentionally presents one product line only: **EarthStick 1.0**.

Current files:

- `EarthStick.py`
- `EarthStick.bat`
- `releases/EarthStick_v1.0.zip`
- `assets/EarthStick_controls.svg`
- `docs/USER_GUIDE.md`
- `docs/EarthStick_User_Guide.pdf`
- `docs/TECHNICAL_NOTES.md`
- `docs/TROUBLESHOOTING.md`
- `docs/HARDWARE_MAP.md`

Development packages and superseded integration material are not part of the public 1.0 presentation.
