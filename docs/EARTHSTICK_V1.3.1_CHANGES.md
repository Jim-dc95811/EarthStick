# EarthStick 1.3.1 - Changes

Released 2026-11-03. Built and live-tested by Jim on ArcGIS Earth Desktop 3.0.1 the same day (the World Gates tour video, [ArcGIS Earth Flight: City to City Using Wormholes](https://www.youtube.com/watch?v=2N8-4cWMoPw), was flown on exactly this gate pack).

## The program: one change

The crosshair is larger and thicker, for aiming at gate centres and objects: `RETICLE_SIZE` 48 -> 80 px, new `RETICLE_WIDTH = 5` (was a fixed 3), centre gap 6 -> 8 px, centre dot radius 2 -> 3 px. Version strings say 1.3.1. Nothing else in `EarthStick.py` changed; flying, trigger-click and gates behave exactly as in 1.3. Accepted live by Jim ("the crosshair mod is great").

`EarthStick.py` 1.3.1 SHA-256: `3ec65b44c0bfa55c6b85f1ec101298a29b18205f794d13e68297705ac6f81488`

## The World Gates pack: v14

`Gates/World_Gates_JAX_ATL_v14.kmz` (SHA-256 `16ab9263328e4819c1abc96f9e67c82111e03f1f6276c7eb7fc5086f1791ffdd`, 22 gates; the 1.3 pack had 16). Built with `tools/build_world_gates.py` in ArcGIS-Earth-Unlocked; the version is in the file name and layer name.

- **Round-the-world tour:** each city gets a next-city gate 2 km beyond its landmark (New York > London > Paris > Rome > Tokyo > Sydney > Rio; Rio's onward gate is its ATL gate). The ATL gate sits 2 km from the landmark toward Atlanta. You arrive 1.7 km short of the landmark, facing it.
- **Welcome signs** at arrival height, 1.2 km straight ahead.
- **Site stars:** five per city (also Atlanta and Jacksonville), one row 900 m out below the sign, spaced by name length. The sign and row turn sideways until no gate at that city is behind them.
- **One-click beacons:** clicking a star opens a short information box whose script draws a 3 km beacon line and a ground name in the site's colour (red, blue, green, magenta, orange) through ArcGIS Earth's Automation API. Cleared by unticking under My Drawings. A second click does not duplicate (live-checked).
- **Near-only text:** signs, stars and ring names are in KML Regions that show within about 20,000 ft (ArcGIS Earth draws KML text at a fixed screen size, so it would otherwise cover the map from far away).
- Names are kept short enough not to wrap in ArcGIS Earth (signs 18 characters, site names 19, checked when the pack is built).

Known: the beacon's ground name sits on ArcGIS Earth's blue pin (left as is). The Atlanta hub welcome sign overlaps the London gate's name, and "World of Coca-Cola" wraps at its hyphen: cosmetic, queued for the next gate pack.

## City Beacons

`City_Beacons/` (also `gates/World_Gates_City_Beacons_v2.zip`): nine red 3 km beacons named "Go to ...". Double-click in the Data list to fly straight to a city. ArcGIS Earth ignores KML LookAt/Camera views on double-click, so you arrive overhead.

## ArcGIS Earth Flight launcher v1.0

`Fly_ArcGIS_Earth.bat` finds `ArcGISEarth.exe` (known folders, then a search; remembered in `ArcGIS_Earth_path.txt`), starts it unless it is running, then calls `EarthStick.bat`. `Make_Taskbar_Shortcut.bat` makes a desktop shortcut "ArcGIS Earth Flight" with the ArcGIS Earth icon, to pin to the taskbar. Accepted live by Jim ("worked the first time"); on his PC ArcGIS Earth is at `C:\Program Files\ArcGIS\ArcGIS Earth\bin\ArcGISEarth.exe`.

## Release file

`archive/EarthStick_v1.3.1.zip` SHA-256: `fd739b5189318966d9b91170cb0d33764335fffe7cdb4c7499a00eea4d34d2f0`

Folder `EarthStick_v1.3.1/`: `EarthStick.py`, `EarthStick.bat`, `Fly_ArcGIS_Earth.bat`, `Make_Taskbar_Shortcut.bat`, `Gates/World_Gates_JAX_ATL_v14.kmz`, `City_Beacons/` (9 KMZ). The 1.3 zip and the 1.3 gate file stay for existing links.
