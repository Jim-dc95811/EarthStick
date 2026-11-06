# CONTINUITY - EarthStick 1.3.6

## Official baseline

**2026-11-06 evening - 1.3.6 released (Gate Dropper; = TEST5, live-accepted 18:41 by Jim: 'going in, coming out, back in, back out').** Button 2 short press = mark (acts on release); second press >= 1,100 m away drops a one-way gate pair `Gates/Dropped_Gate_NN.kmz` (each gate 500 m ahead of its press along the heading, at camera z, facing the heading; arrive 300 m past the partner looking its heading); hold Button 2 2 s = undo (file, gates, map layer). Gates are armed at once and added to the map via `POST /arcgisearth/layer` (proven live); undo uses `DELETE /arcgisearth/layer/{id}` (untested live). Dropped gates: radius 300 m, black lines width 4, own grab zone `lock_capture_m` 609.6 / `lock_range_m` 3000. New `System Files/gate_dropper.py` (loaded with importlib). Zip `5b443f85a748ee049902f472c6a5a14597b3c434f44dc633858cbf4126757454`, py `cac0436c...`, gate_dropper `c0f7f1aa...`. Full math and design history: `docs/EARTHSTICK_V1.3.6_CHANGES.md` and the Unlocked `CLAUDE.md` section 3a 'Gate Dropper math'. Flying without Button 2 = 1.3.5.

**2026-11-01 update:** the front page follows the family-wide layout (download link, user manual link, one line, screenshot that opens the video). Screenshot `images/earthstick_flight_arcgis_earth.jpg` opens video `5Wn14qlC7n4`. `docs/USER_GUIDE.md` was corrected against the code (updated for 1.2 the same day, with a trigger-click section) and `docs/EarthStick_User_Guide.pdf` is generated from it with the Unlocked `tools/md2pdf.py`.

**EarthStick 1.3 (previous release, live-accepted 2026-11-02; superseded by 1.3.1 below).** 1.3 = 1.2 plus **World Gates** (wormholes, Jim's idea): gate KMZ files in a `Gates` folder beside EarthStick.py (ExtendedData `gate=1, lat, lon, alt_m` (sea level), `radius_m, facing, to` or `dest_lat/dest_lon/dest_alt_m/dest_heading`), read at startup; flying forwards through a ring (crossing test on each step, within radius) replaces the next camera position with the arrival; 2 s cooldown; only while the stick moves the camera; partners resolved in the same file first. Ships with `Gates/World_Gates_JAX_ATL.kmz` (also loose at `gates/`): JIA -> ATL hub (8 gates, 3 km circle, eye alt 2,530 ft) -> NYC/London/Paris/Rome/Tokyo/Sydney/Rio landmarks, each with an ATL return. Eye alt in ArcGIS Earth = sea level (measured). No gates = byte-identical to 1.2. Gate files are made with `tools/make_gate_kmz.py` / `tools/build_world_gates.py` in ArcGIS-Earth-Unlocked. See `docs/EARTHSTICK_V1.3_CHANGES.md`.

**EarthStick 1.3.5 + World Gate Maker 1.2 RELEASED 2026-11-06** (Jim's one-obvious-file rule; he tests the released zips, fix forward). EarthStick: `Fly_ArcGIS_Earth.bat` + `Gates` + `City_Beacons` + `System Files/` (EarthStick.py, EarthStick.bat, Make_Taskbar_Shortcut.bat - Jim's choices); the repo root mirrors that layout. `EarthStick.py` reads `<top>/Gates` where top = parent of `System Files`; launcher v1.1 calls `System Files\EarthStick.bat`, path file in System Files; shortcut maker finds the Fly bat one level up. Flying byte-identical to 1.3.4 (replay + trigger streams), wormhole rig `--system-files` PASS. World Gate Maker: `gate_maker/World_Gate_Maker.bat` + `gate_maker/System Files/World_Gate_Maker.py`; `guess_gates_folder` also searches one level higher, newest EarthStick* first. Zips `EarthStick_v1.3.5.zip` `a9b81467...`, `World_Gate_Maker_v1.2.zip` `d06c8815...`.

**EarthStick 1.3.4 RELEASED 2026-11-05** (Jim: TEST7 'to london and back, working great' ... 'perfect please do'): 1.3.3 + ring-height light (`ring_ahead`: nearest gate within 15 deg of heading, facing within 60, within 10 km; green within 0.5 radius) + tractor beam (`tractor_pull`: within 1,500 m and 1 radius; hovering or flying; max(half-life 1 s, travel/distance glide path); buttons 3/4 release) + World Gates **v21** (square gates with 320 m legs; gate data = v19). `releases/EarthStick_v1.3.4.zip` `cd600e6281bb07f7281cc1d2097e51d30646c1b605bccd8d6829afd002c2d3d2`, `EarthStick.py` `7ab8f8cd94cdf35b9be903e7b581f71604e9d95d0484d40c86afed1e850739b0` (= TEST7), `gates/World_Gates_JAX_ATL_v21.kmz` `df42e344317e1abaa7d40a9a659ab579fe1ed38e825273d708a88ba56e228d94`. Shelved: trigger beam (TEST-TEST3), v20 approach arrows. See `docs/EARTHSTICK_V1.3.4_CHANGES.md`.

**World Gate Maker 1.1 RELEASED 2026-11-05** (Jim flew JAX <-> Seattle: 'my safe return home'; asked for gate-not-ring wording before posting): square gates with legs (1.42 x radius: Small 71 m, Medium 178 m, Large 320 m); sizes labelled by square width (70/180/320 m, same trigger radii 50/125/225 m); gate data identical to 1.0. `releases/World_Gate_Maker_v1.1.zip` `9dd731c0bbc5d9ca6acc19e294a35d95055f09b30af8581b6f4d0b26a2d802e9`, `gate_maker/World_Gate_Maker.py` `7c018f7aea5e1789791f86429071517e48433ba88f344b116ccd106d0286fbf5`; change doc `docs/WORLD_GATE_MAKER_V1.1_CHANGES.md`; pictures `images/world_gate_maker_v1.1_seattle_arrival.jpg`, `_home_ring_height.jpg`. 1.0 zip kept. The full gate-alignment math (ring separation, light, tractor beam, square geometry) is in the umbrella repo's CLAUDE.md section 3a.

**EarthStick 1.3.3 RELEASED 2026-11-04** (Jim: "Go!" after TEST3): 1.3.2 + a click-through readout (Tk Toplevel, transparent key colour) on the right of the ArcGIS Earth window above the globe button: height ft / compass + heading / ≈ zoom (two lines), set from the flying loop at the 0.10 s status cadence, no extra API calls; full screen 480 px up, windowed 695 px (windowed position not yet measured on Jim's screen). `releases/EarthStick_v1.3.3.zip` `758dc8537c16ef5e789db0353422cf2661ab10edaad41ddfcb66f0719d816079`, `EarthStick.py` `36429640d3affab6e6641679797a0a3afd1d04c57c21259c416ba9b6dfab848b`. See `docs/EARTHSTICK_V1.3.3_CHANGES.md`.

**Pictograms (2026-11-04):** 'Fly the real world in 7 steps' (`images/earthstick_getting_started*.png`, top of README + user guide, dark style) and 'What's in the EarthStick folder?' (`images/earthstick_whats_in_the_folder*.png`, bright style; under the README quick start, the README download line and the user guide). World Gate Maker has its own sheet `images/world_gate_maker_whats_in_the_zip*.png` (README + manual). Sources: Unlocked `tools/graphics/`. **If the EarthStick or World Gate Maker zip contents change, update the sheet** (EarthStick: `earthstick_whats_in_the_folder.html`; Gate Maker: `make_zip_sheets.py`).

**EarthStick 1.3.2 RELEASED 2026-11-04** (Jim: "go"): 1.3.1 program (version text only) + World Gates **v19** (`Gates/World_Gates_JAX_ATL_v19.kmz`, also `gates/`): signs and site stars in the sky, far out, two rows, clear of gates. `releases/EarthStick_v1.3.2.zip` `1631ab1c2c6a3c875ffa7e35a639faa8fb3242bfece1d8849d8231cb0b5e5f7f`, `EarthStick.py` `c55df61f78bf0bc46b9b413f515e3d0232d08961b840e1cc2e6a895ba99e493f`. See `docs/EARTHSTICK_V1.3.2_CHANGES.md`.

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

The repository intentionally presents one product line only: **EarthStick 1.3.4**. `releases/EarthStick_v1.3.3.zip`, `releases/EarthStick_v1.3.2.zip`, `releases/EarthStick_v1.3.1.zip`, `releases/EarthStick_v1.3.zip`, `v1.2`, `v1.1` and `v1.0` are kept only so existing links keep working.

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
