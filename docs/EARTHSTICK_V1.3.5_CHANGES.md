# EarthStick 1.3.5 - One obvious file (2026-11-06)

## Why

Jim's packaging rule for every tool: *one obvious .bat file to click, and everything else under a system folder.* Jim chose to keep **Gates** and **City_Beacons** in view (people use them) and to tuck the taskbar-shortcut maker into System Files.

## The folder after Extract All

```
EarthStick_v1.3.5\
   Fly_ArcGIS_Earth.bat      <- double-click this (starts ArcGIS Earth if needed, then EarthStick)
   Gates\                    <- World Gates pack v21 (and your own gates)
   City_Beacons\             <- 9 "Go to ..." city beacons
   System Files\             <- EarthStick.py, EarthStick.bat, Make_Taskbar_Shortcut.bat
```

## What changed

- `EarthStick.py` reads the **Gates** folder of the EarthStick folder (one level above System Files when it runs from there; beside itself otherwise). Version text 1.3.5.
- `Fly_ArcGIS_Earth.bat` (launcher v1.1) starts `System Files\EarthStick.bat`, and keeps the remembered ArcGIS Earth location in `System Files\ArcGIS_Earth_path.txt` instead of the top folder.
- `Make_Taskbar_Shortcut.bat` lives in System Files and points the desktop shortcut at `Fly_ArcGIS_Earth.bat` one level up.
- `EarthStick.bat`: window title 1.3.5.

## What did not change

Flying. Checked here: the replay and trigger-click camera command streams are byte-identical to 1.3.4 (no gates), and the wormhole flight test passes with Gates beside System Files (one jump, Statue of Liberty arrival at 457 m, heading 33.2). Gate pack: World Gates v21 (same file as 1.3.4). The launcher's search for ArcGIS Earth is unchanged.

Not testable here: the Windows .bat files themselves - Jim's run of the release is the live test.

## Files

- `releases/EarthStick_v1.3.5.zip` SHA-256 `a9b81467cb840bf1ef177616565fb43b76469fc03f0d256c215b7945f6b8c5f3`
- `System Files/EarthStick.py` SHA-256 `a928f356b5bf356a98bb1926513c4dd9daa462c2245845ae72cd98d53c516534`
- Earlier zips kept in `releases/` for existing links.
