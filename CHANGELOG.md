# Changelog

## v0.5 - 2026-10-25

One functional change from v0.4:

- Button 4 red trigger = continuous zoom in by lowering camera altitude
- Button 3 black thumb = continuous zoom out by raising camera altitude
- zoom rate scales with current altitude

Preserved v0.4 translation, throttle, twist/heading, POV tilt, dead zone, and all other button behavior.

## v0.4 - 2026-10-25

One functional change from v0.3:

- multiplied the existing altitude-aware maximum translation speed by 20

At the same test altitude where v0.3 showed about 92 m/s maximum, v0.4 produced about 1,840 m/s maximum.

Minimum speed, throttle curve, X/Y response, twist/heading, POV tilt, dead zone, buttons, and camera logic otherwise remained unchanged.

## v0.3 - 2026-10-25

One functional change from v0.2:

- Slider0 is detected from the actual WinMM Z/U/V capability instead of assuming the U axis

This fixed the throttle slider so `THR` and calculated `SPD` changed correctly in the running console.

## v0.2 - 2026-10-25

One functional change from v0.1:

- added capability-based joystick identification when WinMM reports the generic `Microsoft PC-joystick driver` name instead of `T.A320 Pilot`

Fallback characteristics:

- at least four axes
- 17 buttons
- POV capability

## v0.1 - 2026-10-25

Initial direct T.A320 Pilot -> ArcGIS Earth camera bridge.

Implemented:

- X/Y translation
- RZ heading
- throttle speed
- POV tilt
- ArcGIS Earth camera GET/PUT
- neutral stop/hover behavior
- standard-library-only Windows implementation
