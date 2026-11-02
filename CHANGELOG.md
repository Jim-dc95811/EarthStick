# EarthStick Release Notes

## EarthStick 1.2 - Trigger-click (2026-11-01)

Flying is identical to 1.1.

- red crosshair in the middle of the ArcGIS Earth window
- pull the trigger (Button 1) to click the object under it and open its information box; trigger-click open map to close it
- one click per pull with a 0.8 s lockout, glide-and-rest click so ArcGIS Earth selects instead of zooming
- if the crosshair cannot be shown, EarthStick flies normally
- the zip now holds an `EarthStick_v1.2` folder

Details and verification: [docs/EARTHSTICK_V1.2_CHANGES.md](docs/EARTHSTICK_V1.2_CHANGES.md).

## EarthStick 1.1 - Hardening Release (2026-10-31)

Flying is identical to 1.0: same controls, constants, speed and zoom laws, and recovery behavior.

- waits for the joystick if it is not connected at startup (1.0 exited)
- the local ArcGIS Earth connection never goes through a system proxy
- the startup wait for ArcGIS Earth shows the reason when it appears or changes
- one prompt after an error instead of two

Details and verification: [docs/EARTHSTICK_V1.1_CHANGES.md](docs/EARTHSTICK_V1.1_CHANGES.md).

## EarthStick 1.0 - Official Release

EarthStick 1.0 is the accepted public baseline.

Core behavior:

- direct joystick control of the ArcGIS Earth camera
- forward/reverse travel
- left/right strafe
- twist heading control
- throttle-controlled travel speed
- POV camera tilt
- independent climb/descend buttons
- neutral controls stop and hover
- altitude-aware high-speed travel with fine low-speed throttle control

Reliability behavior:

- bounded 30 Hz control loop
- ArcGIS Earth API timeout and reconnect handling
- fresh camera re-synchronization after API loss
- joystick USB disconnect/reconnect handling
- controller re-discovery if Windows assigns a different joystick ID
- fresh camera re-synchronization after joystick reconnect
- camera response validation
- no third-party Python dependencies

EarthStick 1.0 was superseded by 1.1 on 2026-10-31. Its package remains at `releases/EarthStick_v1.0.zip`.
