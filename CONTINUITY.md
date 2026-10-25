# CONTINUITY - EarthStick

## Project

Repository:

`Jim-dc95811/EarthStick`

Purpose:

Use a Thrustmaster TCA Sidestick Airbus Edition to provide helicopter-style direct camera navigation in ArcGIS Earth desktop through the ArcGIS Earth Automation API.

## Current accepted baseline

**EarthStick v0.5**

Date accepted: **2026-10-25**

v0.5 was live-tested in ArcGIS Earth and demonstrated in a recorded flight.

The current accepted behavior is:

- stick forward/back -> fly forward/reverse
- stick left/right -> strafe left/right
- twist/RZ -> heading
- Slider0 -> movement speed
- POV up/down -> camera tilt
- Button 4 red trigger -> hold to zoom in / descend
- Button 3 black thumb -> hold to zoom out / climb
- neutral controls -> stop and hover in place

## Strict modification rules

These rules are part of the project and must be preserved:

1. Discuss a code modification before making it.
2. Make one functional modification at a time.
3. Every code modification receives a new version number.
4. Do not add unrequested "improvements," cleanup, refactoring, extra features, or button assignments.
5. Preserve proven behavior unless the user explicitly authorizes a change.
6. Test the changed behavior in ArcGIS Earth before calling a new version accepted.
7. Unused joystick buttons remain unused unless a real operational need is identified.
8. Do not silently change movement constants, dead zones, rates, inversions, file names, API address, or control meanings.

## Current files

Root:

- `EarthStick.py` - v0.5
- `EarthStick.bat`
- `README.md`
- `LICENSE`
- `ACKNOWLEDGEMENTS.md`
- `CHANGELOG.md`
- `CONTINUITY.md`

Release:

- `releases/EarthStick_v0.5.zip`

Assets:

- `assets/EarthStick_controls.svg`
- `assets/EarthStick_YouTube_Thumbnail.jpg`

Docs:

- `docs/USER_GUIDE.md`
- `docs/TECHNICAL_NOTES.md`
- `docs/TROUBLESHOOTING.md`
- `docs/VIDEO_GUIDE.md`
- `docs/PROJECT_NOTES.md`

## Tested hardware facts

Windows/Thrustmaster control panel displayed:

`T.A320 Pilot`

Confirmed hardware inputs during mapping:

- X/Y stick axes: full travel and return to center
- RZ/rudder twist: full travel and return to center
- Slider0/throttle: full travel
- POV: all directions
- red trigger: Button 4
- black thumb: Button 3
- top-left stick-side pattern: 11, 12, 13
- top-right stick-side pattern: 7, 6, 5
- left base: 14, 15, 16
- right base: 8, 9, 10

Buttons beyond 3 and 4 have no EarthStick function in v0.5.

## Current technical constants

From v0.5 source:

- `POLL_HZ = 30.0`
- `DEADZONE = 0.08`
- `YAW_RATE_DPS = 55.0`
- `TILT_RATE_DPS = 45.0`
- `EARTH_RADIUS_M = 6378137.0`
- `IDLE_RESYNC_SECONDS = 0.50`
- `HTTP_TIMEOUT = 0.75`
- `BASE_URL = http://localhost:8000`
- `INVERT_TWIST = True`
- `INVERT_THROTTLE = True`

Throttle speed function:

```text
base_max = clamp(max(8.0, altitude_m * 0.020), 8.0, 12000.0)
max_speed = base_max * 20.0
min_speed = 0.50
speed = min_speed + (max_speed - min_speed) * throttle^2
```

Zoom:

```text
zoom_rate_mps = max(2.0, altitude * 0.75)
minimum altitude = 1.0 m
```

## Controller detection history

v0.1 attempted to match the literal name `T.A320 Pilot`.

On the tested PC, `joy.cpl` showed `T.A320 Pilot`, but WinMM returned the generic name `Microsoft PC-joystick driver`.

v0.2 added a fallback for one unique connected controller with:

- `wNumAxes >= 4`
- `wNumButtons == 17`
- POV capability

This behavior is accepted.

## Slider history

v0.2 assumed throttle was WinMM U and the slider did not change speed.

v0.3 added Slider0 detection among Z/U/V using WinMM capability flags. Live test then showed:

- `THR 1.00` -> high speed
- `THR 0.00` -> `0.5 m/s`

This behavior is accepted.

## Speed history

v0.3 maximum translation at the test altitude was about 92 m/s and was judged much too slow.

v0.4 multiplied the existing altitude-aware maximum by 20. Live flight testing judged the result "perfect."

Do not revert the 20x multiplier without an explicit new test/change request.

## Zoom history

v0.5 assigned only two buttons:

- red trigger Button 4 -> zoom in
- black thumb Button 3 -> zoom out

The resulting flight was described as true helicopter-style control and was accepted.

## Key interaction discovery

The major design success is **neutral = hover**.

The controls command motion only while active. Releasing them leaves the ArcGIS Earth camera at the current position. This is the intended interaction model and should not be replaced with momentum/inertia unless explicitly requested.

## Known cosmetic issues in v0.5

Do not silently repair these in-place:

1. startup console still prints `Buttons are intentionally unused in this build.`
2. the unsupported-spatial-reference diagnostic still says `EarthStick 0.3 expects WKID 4326`

They do not affect operation. Fixing either requires discussion and a new version number.

## Potential future ideas - not approved

These are only ideas and must not be implemented without discussion:

- one ME/recenter button
- optional status GUI
- optional controller selection if multiple matching devices are connected
- configurable API base URL
- alternate controller profiles

Do not interpret this list as a roadmap authorization.

## Public positioning

Useful plain-language description:

> EarthStick turns ArcGIS Earth into a helicopter-style 3D navigation environment using a Thrustmaster TCA Sidestick and Esri's existing local camera Automation API.

Do not claim affiliation or endorsement by Esri, Thrustmaster/Guillemot, or Airbus.

## Video

First successful flight recording was made after v0.5 acceptance.

Prepared thumbnail:

`assets/EarthStick_YouTube_Thumbnail.jpg`

Recommended title:

`Fly ArcGIS Earth Like a Helicopter | EarthStick Joystick Control`
