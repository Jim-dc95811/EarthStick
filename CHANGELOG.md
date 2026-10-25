# Changelog

This repository now tracks two related version lines:

- **EarthStick** - standalone flight controller
- **PRAVE/ME + EarthStick** - separate integration that embeds the accepted EarthStick flight core behind ME/FLY camera ownership

## PRAVE/ME + EarthStick v0.2.0 TEST - 2026-10-25

First repository-documented integrated test build.

Architecture:

- preserved `AE_PRAVE_LIVE_v0_1_0_TEST.py` PRAVE/ME core
- preserved exact EarthStick v0.5 core
- added `PRAVE_ME_FLY_v0_2.py` coordinator as the single ArcGIS Earth camera writer
- kept PRAVE serial reception, logging and drawings independent of the 30 Hz EarthStick camera loop

Control addition in the integrated program only:

- T.A320 Button 1 index-finger / gun-style trigger toggles **ME <-> FLY**
- ME -> FLY does not require GPS
- FLY -> ME acts as a deliberate return-to-ME/RTH request and requires a fresh accepted GPS position
- original `T` key remains as fallback toggle

Safety/failure behavior:

- FLY does not depend on GPS
- stale or missing GPS blocks RTH and leaves the program in FLY
- GPS recovery does not automatically pull the camera home
- no joystick at startup leaves PRAVE/ME available without flight control

Live test on 2026-10-25 with T.A320 and ArcGIS Earth connected but `COM12` completely absent verified:

- EarthStick controller remained connected
- ArcGIS Earth API remained connected
- PRAVE serial reconnect attempts continued independently
- FLY remained operational
- Button 1 toggled the joystick-enabled FLY state on/off through ME/FLY mode changes

Still pending live acceptance:

- valid-GPS ME recentering in the integrated build
- FLY -> Button 1 -> RTH to current ME
- GPS-loss/recovery sequence after an initially valid fix

The standalone EarthStick v0.5 source and behavior were not changed by this integration.

---

## EarthStick v0.5 - 2026-10-25

One functional change from v0.4:

- Button 4 red top button = continuous zoom in by lowering camera altitude
- Button 3 black thumb = continuous zoom out by raising camera altitude
- zoom rate scales with current altitude

Preserved v0.4 translation, throttle, twist/heading, POV tilt, dead zone, and all other button behavior.

## EarthStick v0.4 - 2026-10-25

One functional change from v0.3:

- multiplied the existing altitude-aware maximum translation speed by 20

At the same test altitude where v0.3 showed about 92 m/s maximum, v0.4 produced about 1,840 m/s maximum.

Minimum speed, throttle curve, X/Y response, twist/heading, POV tilt, dead zone, buttons, and camera logic otherwise remained unchanged.

## EarthStick v0.3 - 2026-10-25

One functional change from v0.2:

- Slider0 is detected from the actual WinMM Z/U/V capability instead of assuming the U axis

This fixed the throttle slider so `THR` and calculated `SPD` changed correctly in the running console.

## EarthStick v0.2 - 2026-10-25

One functional change from v0.1:

- added capability-based joystick identification when WinMM reports the generic `Microsoft PC-joystick driver` name instead of `T.A320 Pilot`

Fallback characteristics:

- at least four axes
- 17 buttons
- POV capability

## EarthStick v0.1 - 2026-10-25

Initial direct T.A320 Pilot -> ArcGIS Earth camera bridge.

Implemented:

- X/Y translation
- RZ heading
- throttle speed
- POV tilt
- ArcGIS Earth camera GET/PUT
- neutral stop/hover behavior
- standard-library-only Windows implementation
