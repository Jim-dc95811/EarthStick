# CONTINUITY - EarthStick

## Project

Repository:

`Jim-dc95811/EarthStick`

Purpose:

Use a Thrustmaster TCA Sidestick Airbus Edition to provide helicopter-style direct camera navigation in ArcGIS Earth desktop through the ArcGIS Earth Automation API, while preserving an optional integrated PRAVE/ME GPS/vehicle tracking workflow.

## Two separate baselines

### Standalone EarthStick

**Current accepted baseline: EarthStick v0.5**

Date accepted: **2026-10-25**

v0.5 was live-tested in ArcGIS Earth and demonstrated in a recorded flight.

Accepted standalone behavior:

- stick forward/back -> fly forward/reverse
- stick left/right -> strafe left/right
- twist/RZ -> heading
- Slider0 -> movement speed
- POV up/down -> camera tilt
- Button 4 red top button -> hold to zoom in / descend
- Button 3 black thumb -> hold to zoom out / climb
- neutral controls -> stop and hover in place

Standalone v0.5 remains independent of PRAVE/ME and must remain usable as its own two-file program.

### PRAVE/ME + EarthStick integration

**Current integration test build: v0.2.0 TEST**

This is a separate version line. It does **not** replace or rename standalone EarthStick v0.5.

The integration wraps two preserved cores with a coordinator:

- `AE_PRAVE_LIVE_v0_1_0_TEST.py` - preserved PRAVE/RMC parsing, logging and drawings
- `EarthStick.py` - exact accepted EarthStick v0.5 core
- `PRAVE_ME_FLY_v0_2.py` - new coordinator and sole camera owner

Modes:

- **ME** -> PRAVE/ME may recenter ArcGIS Earth on fresh GPS
- **FLY** -> EarthStick v0.5 owns the camera at 30 Hz; GPS is not required

T.A320 Button 1, the index-finger / gun-style trigger, toggles **ME <-> FLY** in the integrated program only.

Button 1 remains unused by standalone EarthStick v0.5.

## Integrated RTH / GPS rules

Button 1 from FLY requests return to ME only if a fresh accepted RMC position exists.

Current freshness threshold:

`5.0 seconds`

Hard rules:

1. ME -> FLY never requires GPS.
2. GPS/serial failure must never disable FLY.
3. Missing/stale GPS must not cause a jump to a cached old position.
4. If RTH is requested without fresh GPS, remain in FLY.
5. GPS recovery alone must not automatically recenter the camera.
6. After GPS recovery, a new deliberate Button 1 press is required to return to ME.
7. Only the coordinator writes the ArcGIS Earth camera in the integrated program.
8. PRAVE reception, drawings and logging may continue while FLY owns the camera.

## Live test status - integration v0.2.0 TEST

Live-tested on 2026-10-25 with:

- T.A320 detected through WinMM
- ArcGIS Earth Automation API connected
- `COM12` absent / no GPS source available at all

Observed:

- startup entered ME state
- missing COM12 produced reconnect attempts every 5 seconds
- controller remained available
- ArcGIS Earth API remained available
- Button 1 toggled into/out of FLY
- joystick flight remained functional with total GPS/serial failure

This verifies the most important failure-isolation rule: **GPS failure does not take down EarthStick flight.**

Not yet live-accepted:

- fresh-GPS ME camera recentering in this coordinator
- fresh-GPS Button 1 RTH from FLY back to current ME
- loss and recovery of GPS after a valid fix

Do not describe the complete integrated workflow as field-proven until those tests are performed.

## Strict modification rules

These rules are part of the project and must be preserved:

1. Discuss a code modification before making it.
2. Make one functional modification at a time.
3. Every code modification receives a new version number.
4. Do not add unrequested improvements, cleanup, refactoring, extra features, or button assignments.
5. Preserve proven behavior unless explicitly authorized.
6. Test changed behavior in ArcGIS Earth before calling a new version accepted.
7. Unused joystick buttons remain unused unless a real operational need is identified.
8. Do not silently change movement constants, dead zones, rates, inversions, file names, API address, or control meanings.
9. Do not alter standalone EarthStick merely to support PRAVE/ME integration; the integration must consume the accepted v0.5 behavior without breaking the standalone program.
10. Do not let PRAVE/ME and EarthStick independently fight over the camera endpoint.

Documentation-only changes do not change the code version.

## Current repository files

Standalone root:

- `EarthStick.py` - accepted v0.5
- `EarthStick.bat`
- `README.md`
- `LICENSE`
- `ACKNOWLEDGEMENTS.md`
- `CHANGELOG.md`
- `CONTINUITY.md`

Releases:

- `releases/EarthStick_v0.5.zip`
- `releases/PRAVE_ME_FLY_v0.2_TEST.zip`

Assets:

- `assets/EarthStick_controls.svg`
- `assets/EarthStick_YouTube_Thumbnail.gif`

Docs:

- `docs/USER_GUIDE.md`
- `docs/EarthStick_User_Guide.pdf` - standalone v0.5 manual
- `docs/PRAVE_ME_FLY.md`
- `docs/TECHNICAL_NOTES.md`
- `docs/TROUBLESHOOTING.md`
- `docs/HARDWARE_MAP.md`
- `docs/FIELD_TEST.md`
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
- index-finger / gun-style trigger: Button 1; required a firm squeeze during mapping
- red top button: Button 4
- black thumb: Button 3
- top-left stick-side pattern: 11, 12, 13
- top-right stick-side pattern: 7, 6, 5
- left base: 14, 15, 16
- right base: 8, 9, 10

Standalone EarthStick v0.5 uses only Buttons 3 and 4.

Integrated v0.2.0 TEST additionally uses Button 1 for ME/FLY/RTH.

## Current standalone technical constants

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

## Key interaction discovery

The major standalone design success is **neutral = hover**.

The major integration design success is **explicit camera ownership**:

> **ME finds you. FLY lets you leave.**

When FLY is active, GPS is advisory state for a future deliberate RTH request; it does not constrain the camera.

## Known cosmetic issues in standalone v0.5

Do not silently repair these in-place:

1. startup console still prints `Buttons are intentionally unused in this build.`
2. the unsupported-spatial-reference diagnostic still says `EarthStick 0.3 expects WKID 4326`

They do not affect operation. Fixing either requires discussion and a new standalone version number.

## Future work - not approved merely by appearing here

Possible future work may include:

- complete live GPS/RTH acceptance test for integration v0.2.0 TEST
- optional status GUI
- optional controller selection if multiple matching devices are connected
- configurable API base URL
- alternate controller profiles

Do not interpret this list as authorization to change code.

## Public positioning

Useful plain-language description:

> EarthStick turns ArcGIS Earth into a helicopter-style 3D navigation environment using a Thrustmaster TCA Sidestick and Esri's existing local camera Automation API.

For the integrated program:

> PRAVE/ME establishes the real-world home position; EarthStick lets the operator leave that position and fly the ArcGIS Earth camera, with a deliberate trigger-controlled return to ME when fresh GPS is available.

Do not claim affiliation or endorsement by Esri, Thrustmaster/Guillemot, or Airbus.
