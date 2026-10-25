# TCA Sidestick Hardware Map Observed During EarthStick Development

Date: 2026-10-25

This file records the button/axis numbers actually observed in the Thrustmaster control panel on the development PC. It is a hardware reference, not a list of EarthStick assignments.

## Axes

| Physical input | Control-panel input | EarthStick v0.5 |
|---|---|---|
| Stick left/right | X Axis | strafe |
| Stick forward/back | Y Axis | forward/reverse |
| Stick twist | RZ Axis / Rudder | heading |
| Throttle lever | Slider 0 | movement speed |
| POV hat | Point of View hat-switch | up/down used for tilt |

## Buttons observed

| Physical location | Button number | EarthStick v0.5 |
|---|---:|---|
| Red trigger | 4 | zoom in |
| Black thumb button | 3 | zoom out |
| Top-left group | 11 | unused |
| Top-left group | 12 | unused |
| Top-left group | 13 | unused |
| Top-right group | 7 | unused |
| Top-right group | 6 | unused |
| Top-right group | 5 | unused |
| Left base top | 14 | unused |
| Left base middle | 15 | unused |
| Left base bottom | 16 | unused |
| Right base top | 8 | unused |
| Right base middle | 9 | unused |
| Right base bottom | 10 | unused |

Buttons 1 and 2 were not needed for the EarthStick control design and were not assigned during the v0.5 development sequence.

Thrustmaster documentation also describes a virtual Button 17 associated with part of the throttle travel. EarthStick v0.5 does not use it.

## Important design rule

Do not assign the remaining buttons merely to make use of them. EarthStick intentionally keeps the physical control model sparse. Add a button only when a real navigation/operational need is identified and approved as a new version.
