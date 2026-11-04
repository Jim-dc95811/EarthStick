# CONTINUITY - EarthStick 1.3.1

## Official baseline

**2026-11-01 update:** the front page follows the family-wide layout (download link, user manual link, one line, screenshot that opens the video). Screenshot `images/earthstick_flight_arcgis_earth.jpg` opens video `5Wn14qlC7n4`. `docs/USER_GUIDE.md` was corrected against the code (updated for 1.2 the same day, with a trigger-click section) and `docs/EarthStick_User_Guide.pdf` is generated from it with the Unlocked `tools/md2pdf.py`.

**EarthStick 1.3 (previous release, live-accepted 2026-11-02; superseded by 1.3.1 below).** 1.3 = 1.2 plus **World Gates** (wormholes, Jim's idea): gate KMZ files in a `Gates` folder beside EarthStick.py (ExtendedData `gate=1, lat, lon, alt_m` (sea level), `radius_m, facing, to` or `dest_lat/dest_lon/dest_alt_m/dest_heading`), read at startup; flying forwards through a ring (crossing test on each step, within radius) replaces the next camera position with the arrival; 2 s cooldown; only while the stick moves the camera; partners resolved in the same file first. Ships with `Gates/World_Gates_JAX_ATL.kmz` (also loose at `gates/`): JIA -> ATL hub (8 gates, 3 km circle, eye alt 2,530 ft) -> NYC/London/Paris/Rome/Tokyo/Sydney/Rio landmarks, each with an ATL return. Eye alt in ArcGIS Earth = sea level (measured). No gates = byte-identical to 1.2. Gate files are made with `tools/make_gate_kmz.py` / `tools/build_world_gates.py` in ArcGIS-Earth-Unlocked. See `docs/EARTHSTICK_V1.3_CHANGES.md`.

**EarthStick 1.3.1 RELEASED 2026-11-03** (Jim: "expedite to now", after flying and filming the World Gates tour on it): 1.3 + a larger crosshair (80 px, 5 px lines; accepted), World Gates pack **v14** (`Gates/World_Gates_JAX_ATL_v14.kmz`, 22 gates: round-the-world tour, welcome signs, one-click coloured site beacons, near-only text), `City_Beacons/` and the ArcGIS Earth Flight launcher v1.0 (`Fly_ArcGIS_Earth.bat`, `Make_Taskbar_Shortcut.bat`; accepted). See `docs/EARTHSTICK_V1.3.1_CHANGES.md`. Video: `2N8-4cWMoPw`. Next gate pack (v15, queued): ATL hub sign above the rings, 'Coca-Cola Museum', remove the unused pin-hiding code.

**World Gate Maker 1.0 RELEASED 2026-11-04** (Jim's idea; accepted live: Home <-> Central Park, 'truly a marvel'): standalone tool, two places (name, lat/lon or Google Maps clipboard, ground elev ft) + height above ground + ring size -> `Gate_<a>_<b>.kmz` in the Gates folder. `releases/World_Gate_Maker_v1.0.zip` SHA-256 `15bf077395307eda1fa988e9c1b2da003a7c1ec0d231ca594481f585aa0c91a1`, `gate_maker/World_Gate_Maker.py` `d1e678c91871406b8242947ae650506f416b3c41445a74ef382d976f4d5c8b9a`, manual `docs/WORLD_GATE_MAKER.md` + PDF. Section 'Make your own gates' on the README.

`EarthStick.py` 1.3.1 SHA-256: `3ec65b44c0bfa55c6b85f1ec101298a29b18205f794d13e68297705ac6f81488`
`releases/EarthStick_v1.3.1.zip` SHA-256: `fd739b5189318966d9b91170cb0d33764335fffe7cdb4c7499a00eea4d34d2f0` (folder `EarthStick_v1.3.1/`)

`EarthStick.py` 1.3 SHA-256: `df0e48dda1da08a7439b118bb5f44d731f6c215e4e86d4f7f223fae9dbde26fe`
`releases/EarthStick_v1.3.zip` SHA-256: `0e8c394748f428eef42fed5aa1da5e5d317557082505ad4ca52e4d271ce0731f` (folder `EarthStick_v1.3/` with `Gates/`)

**EarthStick 1.2** (live-accepted 2026-11-01). 1.2 = 1.1 plus trigger-click: a click-through red crosshair centred on the ArcGIS Earth window; Button 1 (trigger) glides the Windows pointer there and clicks (opens a popup; on open map, closes it). Flying is byte-identical to 1.1 (335-write replay). A Button 2 = Esc close was tried in a test build, did not work on Jim's PC, and was dropped. See `docs/EARTHSTICK_V1.2_CHANGES.md`.

`EarthStick.py` 1.2 SHA-256: `63dd9b55af8aa8273dee212ed2da41ea73395752da898b8a09877d6f9bbefe5a`
`releases/EarthStick_v1.2.zip` SHA-256: `ad114b6197037f8851db459b244f98befee70066b458369ea993b0dcd6f224a5` (zip holds folder `EarthStick_v1.2/`)

EarthStick 1.1 (live-accepted 2026-10-31) was a hardening release on top of the 1.0 baseline: it waits for the joystick at startup, bypasses system proxies for the localhost API, prints the reason while waiting for ArcGIS Earth, and leaves the single post-error prompt to the .bat. Controls, constants, movement and recovery are unchanged from 1.0. See `docs/EARTHSTICK_V1.1_CHANGES.md`.

`EarthStick.py` 1.1 SHA-256: `84894c2f2d6c857ba71b2153126cb274254e3dbf23099ca1b821dbc2ca7400c7`
`releases/EarthStick_v1.1.zip` SHA-256: `505295a68e041bec7ae921f2c71b5240816946a8d5bb5f48459f3b237819c52e`

Purpose: use a Thrustmaster TCA Sidestick Airbus Edition to provide direct, helicopter-style free camera navigation in ArcGIS Earth desktop through the ArcGIS Earth Automation API.

The defining interaction is:

> **Neutral controls = stop and hover in place.**

## Accepted controls

- stick forward/back -> fly forward/reverse
- stick left/right -> strafe left/right
- twist/RZ -> heading left/right
- Slider0 -> movement speed
- POV up/down -> camera tilt
- Button 4 red top button -> hold to zoom in / descend
- Button 3 black thumb button -> hold to zoom out / climb
- Button 1 trigger -> trigger-click the object under the crosshair (1.2)
- flying through a gate ring (gold side) -> jump to its destination (1.3)
- all other buttons -> unused

## Accepted recovery behavior

- ArcGIS Earth API loss does not terminate EarthStick.
- During API loss, EarthStick does not accumulate stale camera movement.
- After API recovery, EarthStick re-reads the live ArcGIS Earth camera before sending movement again.
- Joystick USB loss does not terminate EarthStick.
- EarthStick retries joystick detection and supports reconnection under a different Windows joystick ID.
- After joystick reconnection, EarthStick re-reads the current ArcGIS Earth camera before accepting movement.
- Malformed or non-finite camera data is rejected as an API fault rather than used as movement state.

## Tested environment

- Windows 11
- Python 3.14.5
- ArcGIS Earth desktop with Automation API enabled
- Thrustmaster TCA Sidestick Airbus Edition
- Windows controller name observed: `T.A320 Pilot`
- local API: `http://localhost:8000`

No third-party Python packages are required.

## Technical constants

- `POLL_HZ = 30.0`
- `DEADZONE = 0.08`
- `YAW_RATE_DPS = 55.0`
- `TILT_RATE_DPS = 45.0`
- `EARTH_RADIUS_M = 6378137.0`
- `IDLE_RESYNC_SECONDS = 0.50`
- `HTTP_TIMEOUT = 0.75`
- `INVERT_TWIST = False`
- `INVERT_THROTTLE = True`

Throttle speed function:

```text
base_max = clamp(max(8.0, altitude_m * 0.020), 8.0, 12000.0)
max_speed = base_max * 60.0
min_speed = 0.50
speed = min_speed + (max_speed - min_speed) * throttle^2
```

Zoom:

```text
zoom_rate_mps = max(2.0, altitude * 0.75)
minimum altitude = 1.0 m
```

## Modification rules

1. Treat EarthStick 1.2 as the protected known-good baseline.
2. Discuss functional changes before making them.
3. Make one functional modification at a time.
4. Preserve control meanings, movement constants, API address, and recovery behavior unless a change is explicitly authorized.
5. Test changed behavior in ArcGIS Earth before replacing the accepted release.
6. Do not assign unused buttons without an operational reason.
7. Do not add dependencies unless they solve a demonstrated need.
8. Keep filenames short and practical.
9. Never describe untested behavior as verified.

## Repository presentation

The repository intentionally presents one product line only: **EarthStick 1.3.1**. `releases/EarthStick_v1.3.zip`, `v1.2`, `v1.1` and `v1.0` are kept only so existing links keep working.

Current files:

- `EarthStick.py`
- `EarthStick.bat`
- `releases/EarthStick_v1.3.1.zip`
- `releases/EarthStick_v1.3.zip`
- `releases/EarthStick_v1.2.zip`, `v1.1`, `v1.0` (previous releases)
- `gates/World_Gates_JAX_ATL_v14.kmz` (current gate pack, also inside the 1.3.1 zip), `gates/World_Gates_City_Beacons_v2.zip`, `gates/World_Gates_JAX_ATL.kmz` (1.3 pack, kept for links)
- `Fly_ArcGIS_Earth.bat`, `Make_Taskbar_Shortcut.bat` (launcher, also in the 1.3.1 zip)
- `docs/EARTHSTICK_V1.3.1_CHANGES.md`, `docs/EARTHSTICK_V1.3_CHANGES.md`, `docs/EARTHSTICK_V1.2_CHANGES.md`, `docs/EARTHSTICK_V1.1_CHANGES.md`
- `images/world_gates_atl_hub_arcgis_earth.jpg`, `images/world_gates_paris_ring_arcgis_earth.jpg`
- `assets/EarthStick_controls.svg`
- `docs/USER_GUIDE.md`
- `docs/EarthStick_User_Guide.pdf`
- `docs/TECHNICAL_NOTES.md`
- `docs/TROUBLESHOOTING.md`
- `docs/HARDWARE_MAP.md`

Development packages and superseded integration material are not part of the public presentation.
