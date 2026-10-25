# TCA Sidestick Hardware Map Observed During EarthStick Development

Date: 2026-10-25

This file records the button/axis numbers actually observed in the Thrustmaster control panel on the development PC. It distinguishes physical hardware mapping from assignments in standalone EarthStick and the separate PRAVE/ME integration.

## Axes

| Physical input | Control-panel input | EarthStick v0.5 |
|---|---|---|
| Stick left/right | X Axis | strafe |
| Stick forward/back | Y Axis | forward/reverse |
| Stick twist | RZ Axis / Rudder | heading |
| Throttle lever | Slider 0 | movement speed |
| POV hat | Point of View hat-switch | up/down used for tilt |

## Buttons observed

| Physical location | Button number | Standalone EarthStick v0.5 | PRAVE/ME + EarthStick v0.2 TEST |
|---|---:|---|---|
| Index-finger / gun-style trigger | 1 | unused | toggle ME / FLY; RTH request from FLY |
| Red top button | 4 | zoom in | zoom in |
| Black thumb button | 3 | zoom out | zoom out |
| Top-left group | 11 | unused | unused |
| Top-left group | 12 | unused | unused |
| Top-left group | 13 | unused | unused |
| Top-right group | 7 | unused | unused |
| Top-right group | 6 | unused | unused |
| Top-right group | 5 | unused | unused |
| Left base top | 14 | unused | unused |
| Left base middle | 15 | unused | unused |
| Left base bottom | 16 | unused | unused |
| Right base top | 8 | unused | unused |
| Right base middle | 9 | unused | unused |
| Right base bottom | 10 | unused | unused |

Button 1 was mapped after standalone v0.5 was already accepted. It did not appear to respond at first; a firmer squeeze of the physical index-finger trigger showed it as **Button 1** in the Windows/Thrustmaster test panel.

Button 1 remains deliberately unassigned in standalone EarthStick v0.5. Its ME/FLY/RTH function belongs only to the separate PRAVE/ME integration.

Button 2 has not been assigned.

Thrustmaster documentation also describes a virtual Button 17 associated with part of the throttle travel. EarthStick v0.5 does not use it.

## Important design rule

Do not assign remaining buttons merely to make use of them. The control model stays sparse. Add a button only when a real navigation/operational need is identified and approved as a new version of the program that uses it.
