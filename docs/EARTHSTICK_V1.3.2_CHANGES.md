# EarthStick 1.3.2 - Changes

Released 2026-11-04. Jim flew World Gates v15-v19 the same evening; v19 accepted ("jolly good!", London) and released with "go, these are more ornaments on our beta".

## The program

Unchanged from 1.3.1 apart from the version text (`VERSION = "1.3.2"`, docstring line, console title in `EarthStick.bat`).

`EarthStick.py` 1.3.2 SHA-256: `c55df61f78bf0bc46b9b413f515e3d0232d08961b840e1cc2e6a895ba99e493f`

## The World Gates pack: v19

`Gates/World_Gates_JAX_ATL_v19.kmz` (SHA-256 `33ba39b95b9b37ed751b6f4999dcfeb7701e9b5b75cfc8ad20b79205ebfdeeee`, 22 gates - the gates themselves are as in v14). What changed, each step from Jim's live flights:

- **v15:** Atlanta hub sign lifted above the ring of gates (it sat on the London gate's name); "World of Coca-Cola" -> "Coca-Cola Museum" (it split at the hyphen); unused pin-hiding code removed.
- **v16:** signs and stars moved far out (sign 6 km, stars 5 km; were 1.2 km / 0.9 km). Near objects shift and pile up as you fly; far ones stay put like scenery, and the trigger reaches them anyway (Jim: "if they were distant you wouldn't have this effect").
- **v17:** two rows of stars instead of one (ArcGIS Earth's view is about 78 degrees wide and a one-row board reached 79); stars 4 km out; boards show from about 8 miles.
- **v18:** boards keep clear of each gate and its name and stay inside the view; if no gap fits, the board lifts above the gates.
- **v19:** the whole board in the sky (stars 2 and 6 degrees above eye level, sign 10.5) - from arrival height the horizon is at eye level and anything lower sat on the city (Jim, London).

Layout from v18 on was checked before flying with a viewer model of ArcGIS Earth (`tools/preview_view.py` in ArcGIS-Earth-Unlocked) fitted to Jim's screenshots within 2-5 pixels.

## Release file

`archive/EarthStick_v1.3.2.zip` SHA-256: `1631ab1c2c6a3c875ffa7e35a639faa8fb3242bfece1d8849d8231cb0b5e5f7f`

Folder `EarthStick_v1.3.2/`: `EarthStick.py`, `EarthStick.bat`, `Fly_ArcGIS_Earth.bat`, `Make_Taskbar_Shortcut.bat`, `Gates/World_Gates_JAX_ATL_v19.kmz`, `City_Beacons/` (9 KMZ, unchanged). Earlier zips and gate files stay for existing links.
