# EarthStick 1.3.6 - The Gate Dropper (2026-11-06)

Jim: *"manually entering that info is a huge pain ... I would love to automate that procedure."* After five live tests the same evening (TEST to TEST5), Jim: *"going in, coming out, back in, back out. you have solved the 2d/3d gate portal challenge."*

## What it does

- **Button 2, short press = mark.** First press: mark 1 (EarthStick reads the camera fresh: latitude, longitude, height, heading). Second press, at least `min_apart_m` (1,100 m) away: `gate_dropper.py` writes `Gates/Dropped_Gate_NN.kmz`, EarthStick reloads the Gates folder (armed at once, no restart) and asks ArcGIS Earth to show the file (`POST /arcgisearth/layer`, type KML - proven live: the layer appeared in My Data). A press closer than that to mark 1 clears it. A short press acts when the button is let go.
- **Button 2, hold 2 s = undo.** Clears a waiting mark 1, otherwise deletes the newest `Dropped_Gate_*.kmz`, reloads the Gates folder and removes the map layer (`DELETE /arcgisearth/layer/{id}`, id from the add-layer reply, remembered for this session only). Numbers are reused.
- **Where a dropped gate stands:** 500 m (`DROP_AHEAD_M`) in front of where you pressed, along your heading, at your exact height (sea level), facing your heading - so you just push forward.
- **Where you come out:** 300 m past the other gate along that gate's facing, looking the same way (one-way gates with `dest_*` data, both directions) - the gate is behind you, so no bounce back.
- **Look:** World Gate Maker's square-with-legs drawing (copied unchanged), but radius 300 m (opening about 425 m across, legs 427 m), lines black width 4, red back width 4, white names.
- **Grab zone:** dropped gates carry `lock_capture_m` = 609.6 m (2,000 ft) and `lock_range_m` = 3,000 m in their data; `tractor_pull` uses a gate's own values when present (World Gates and World Gate Maker gates keep 1,500 m and 1 radius).
- **Countdown:** while locked on, the light shows the horizontal distance to the gate in feet (nearest 10): `LOCKED ON · 560 ft` (all gates).
- Messages show as a gold line above the readout for 5 s (`NOTICE_S`) and in the console.

## Why it ended up like this (the test history)

| Test | Change | Jim's verdict |
|---|---|---|
| TEST | gate at the mark, facing the other mark (World Gate Maker's rule), Medium gold | works, but the gate over a painting faced 90 degrees away |
| TEST2 | gate faces your heading; arrive past the other gate looking that gate's heading | "impossible" - the way in was behind you |
| TEST3 | gate 500 m ahead of where you pressed | improving - a gate marked high stays high (by design: your height) |
| TEST4 | hold Button 2 = undo (file, gates, map layer) | works - at gate height you cannot see the gate; trust LOCKED ON |
| TEST5 | own grab zone (3 km, +-2,000 ft), countdown, thin black gates, bigger opening | accepted |

## Unchanged

Flying with Button 2 untouched is identical to 1.3.5 (rig PUT streams: replay, unplugged, proxy, port conflict, trigger, trigger replay); wormhole rig PASS; World Gates, trigger-click, readout and ring light unchanged.

## Files

- `archive/EarthStick_v1.3.6.zip` SHA-256 `5b443f85a748ee049902f472c6a5a14597b3c434f44dc633858cbf4126757454` (folder `EarthStick_v1.3.6/`: `Fly_ArcGIS_Earth.bat`, `Gates`, `City_Beacons`, `System Files` with `EarthStick.py`, `gate_dropper.py`, `EarthStick.bat`, `Make_Taskbar_Shortcut.bat`)
- `System Files/EarthStick.py` SHA-256 `cac0436c30cad87ebeee2bda35b61ea241b2bffc92e0030474cd7b4f60700c47`
- `System Files/gate_dropper.py` SHA-256 `c0f7f1aac2f66ee9fda0a02d5014b85faa34860953c1cc68037a4aa5108ffc39`
- Self-test: `py EarthStick.py --selftest` (adds Gate Dropper, undo and grab-zone checks). Flight rig: `tools/test-rigs/earthstick_rig_dropper.py` in ArcGIS-Earth-Unlocked.
