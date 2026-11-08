# EarthStick Release Notes

## Ready to Fly 1.1 in every package (2026-11-08, same version numbers)

Microsoft Defender blocked the all-tools zip as 'Settings Modifier - potentially unwanted behavior'. Ready to Fly 1.1 installs Python only with Windows' own installer (winget), shown normally - the user answers its questions - with nothing silent, nothing downloaded and run by the script, and no Windows setting changed. Without winget it opens python.org's download page with three steps. Jim's Defender then downloaded the same tools cleanly. Every package's zip was replaced with only `System Files/Ready_To_Fly.ps1` changed.

## EarthStick 1.3.10 - The trigger drops gates (2026-11-08)

- Trigger (Button 1): Gate Dropper - press at two places for a gate pair, hold 2 s to undo
- Button 2: click the object under the red crosshair (was the trigger)
- Everything else as 1.3.9

Details: [docs/EARTHSTICK_V1.3.10_CHANGES.md](docs/EARTHSTICK_V1.3.10_CHANGES.md).

## World Gate Maker 1.2.1 - Ready to Fly (2026-11-08)

- `World_Gate_Maker.bat`: the launcher now gets the PC ready first: it finds Python or installs it for you (just for you, no admin - answer **Y**), then starts the tool. New file `System Files\Ready_To_Fly.ps1` (log: `System Files\Ready_To_Fly_log.txt`). Program byte-identical to the previous release. Live-tested by Jim 2026-11-08.

## EarthStick 1.3.9 - Ready to Fly + hardening (2026-11-08)

- `Fly_ArcGIS_Earth.bat` now gets the PC ready first: checks the internet, finds Python or installs it for you (no admin), finds and starts ArcGIS Earth (or offers Esri's download page), and checks its Automation API is switched on
- Only one EarthStick (and one Ready to Fly) at a time - an extra double-click no longer starts a second copy
- The tractor beam no longer pulls back what you do with the mouse while you hover near a gate
- The status line fits the window (no scrolling); undo always removes the newest dropped gate; clearer 'switch on the Automation API' message
- Flying, gates and the Gate Dropper unchanged (1.3.7 and 1.3.8 were test builds)

Details: [docs/EARTHSTICK_V1.3.9_CHANGES.md](docs/EARTHSTICK_V1.3.9_CHANGES.md).

## EarthStick 1.3.6 - The Gate Dropper (2026-11-06)

- Button 2: press at one place, then at another - a pair of gates appears, 500 m ahead of each press, at your height, facing your way; no typing, no restart
- Hold Button 2 for 2 seconds: undo the last drop (file, gates and map layer)
- Dropped gates: thin black lines, a 425 m opening, lock on from 3 km and 2,000 ft above or below
- LOCKED ON light counts down the distance to the gate
- Flying without Button 2 unchanged

Details: [docs/EARTHSTICK_V1.3.6_CHANGES.md](docs/EARTHSTICK_V1.3.6_CHANGES.md).

## EarthStick 1.3.5 + World Gate Maker 1.2 - One obvious file (2026-11-06)

- EarthStick folder: `Fly_ArcGIS_Earth.bat` (double-click this), `Gates`, `City_Beacons`, `System Files` (the program, its .bat and the taskbar-shortcut maker)
- World Gate Maker folder: `World_Gate_Maker.bat` + `System Files`; finds the newest EarthStick Gates folder next to it
- Flying unchanged (camera streams identical to 1.3.4)

Details: [docs/EARTHSTICK_V1.3.5_CHANGES.md](docs/EARTHSTICK_V1.3.5_CHANGES.md), [docs/WORLD_GATE_MAKER_V1.2_CHANGES.md](docs/WORLD_GATE_MAKER_V1.2_CHANGES.md).

## World Gate Maker 1.1 - Square gates (2026-11-05)

- Your own gates are now gold squares with legs, like the World Gates pack in 1.3.4
- Sizes shown as the square's width (Small 70 m, Medium 180 m, Large 320 m); screen says gate instead of ring
- Gate data unchanged: 1.0 gates still work

Details: [docs/WORLD_GATE_MAKER_V1.1_CHANGES.md](docs/WORLD_GATE_MAKER_V1.1_CHANGES.md).

## EarthStick 1.3.4 - Square gates, ring-height light, tractor beam (2026-11-05)

- World Gates v21: every gate is a gold square with legs - lined up, the legs make an even X
- Green RING HEIGHT light when you are at the height of the gate you are flying toward
- Tractor beam: near a gate, EarthStick glides you onto its height (LOCKED ON); climb/descend lets go
- Flying, trigger-click and the readout unchanged

Details: [docs/EARTHSTICK_V1.3.4_CHANGES.md](docs/EARTHSTICK_V1.3.4_CHANGES.md).

## EarthStick 1.3.3 - Height, heading and zoom readout (2026-11-04)

- A readout on the right of the ArcGIS Earth window, above the globe button: height in feet on top, compass heading and equivalent map zoom underneath - visible in full-screen mode, where ArcGIS Earth hides its eye alt
- Flying, World Gates and trigger-click unchanged

Details: [docs/EARTHSTICK_V1.3.3_CHANGES.md](docs/EARTHSTICK_V1.3.3_CHANGES.md).

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
