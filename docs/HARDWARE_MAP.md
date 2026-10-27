# EarthStick 1.0 Hardware Map

## Tested controller

**Thrustmaster TCA Sidestick Airbus Edition**

Windows control-panel name observed during testing:

`T.A320 Pilot`

## Inputs used by EarthStick

| Physical input | Windows / EarthStick input | Action |
|---|---|---|
| Stick left/right | X | Strafe left/right |
| Stick forward/back | Y | Fly forward/reverse |
| Stick twist | RZ / WinMM R | Change heading |
| Base throttle | Slider 0; WinMM Z/U/V depending on driver mapping | Travel speed |
| POV up/down | POV | Camera tilt |
| Red top button | Button 4 | Descend / zoom in |
| Black thumb button | Button 3 | Climb / zoom out |

Other buttons are intentionally unassigned.

## Driver note

Some Windows installations expose the device name through WinMM as a generic Microsoft joystick driver even though `joy.cpl` shows `T.A320 Pilot`. EarthStick includes a capability-based fallback using the tested T.A320 axis/button/POV layout.

## Slider note

WinMM may expose the physical Slider 0 as Z, U, or V. EarthStick uses capability flags to identify the single present slider axis rather than hard-coding one field.
