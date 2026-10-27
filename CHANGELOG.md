# EarthStick Release Notes

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

EarthStick 1.0 is the only release presented by this repository.
