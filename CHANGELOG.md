# EarthStick Release Notes

## EarthStick 1.3.2 - World Gates v19 (2026-11-04)

The program is unchanged (version text only).

- World Gates pack v19: welcome signs and site stars up in the sky, several km out, two rows that fit the screen and clear the gates
- Atlanta hub: sign above the ring of gates; "World of Coca-Cola" -> "Coca-Cola Museum"

Details: [docs/EARTHSTICK_V1.3.2_CHANGES.md](docs/EARTHSTICK_V1.3.2_CHANGES.md).

## EarthStick 1.3.1 - Round the world (2026-11-03)

Flying and gates work exactly as in 1.3.

- larger, thicker crosshair (80 px, 5 px lines; was 48 px, 3 px)
- World Gates pack v14: round-the-world tour gates (New York > London > Paris > Rome > Tokyo > Sydney > Rio > Atlanta), welcome signs, five site stars per city with one-click coloured beacons, signs and names shown only when near
- City Beacons: double-click to go straight to any city
- ArcGIS Earth Flight one-click launcher (`Make_Taskbar_Shortcut.bat`, `Fly_ArcGIS_Earth.bat`)

Details and verification: [docs/EARTHSTICK_V1.3.1_CHANGES.md](docs/EARTHSTICK_V1.3.1_CHANGES.md).

## EarthStick 1.3 - World Gates (2026-11-02)

Flying is identical to 1.2.

- golden gate rings: fly through one (gold side, at the altitude under its name) and the camera jumps to its destination
- gate files in a `Gates` folder beside EarthStick, read at startup; partners or one-way destinations
- World Gates pack included: Jacksonville -> Atlanta hub -> New York, London, Paris, Rome, Tokyo, Sydney, Rio and back
- with no gate files, camera output is byte-identical to 1.2

Details and verification: [docs/EARTHSTICK_V1.3_CHANGES.md](docs/EARTHSTICK_V1.3_CHANGES.md).

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
