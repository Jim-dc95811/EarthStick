# EarthStick 1.3.9 - Ready to Fly + hardening (2026-11-08)

**Live-accepted by Jim 2026-11-08 12:51** (1.3.9 TEST on his PC: Ready to Fly found Python 3.14.5 and ArcGIS Earth, confirmed the Automation API, EarthStick flew with the status line updating in place; a second double-click was stopped with "EarthStick is already running"). Ready to Fly v1.0 was proven the same day on a worst-case PC: an old Windows 10 laptop with Python uninstalled, offline for weeks, where it installed Python by itself and EarthStick flew.

Flying, World Gates, the tractor beam's height pull, trigger-click and the Gate Dropper work as in 1.3.6 (versions 1.3.7 and 1.3.8 were test builds only).

## New: Ready to Fly (the launcher gets the PC ready)

`Fly_ArcGIS_Earth.bat` v2.0 now runs `System Files\Ready_To_Fly.ps1` v1.0.1 before EarthStick:

1. **Internet check** (never stops you): offline = "ArcGIS Earth's online basemaps won't load; your offline TPKX maps still work"; a Wi-Fi sign-in page is spotted and named.
2. **Python:** found wherever it is (ignoring the Microsoft Store placeholder). If it is missing, it asks, then installs it **for this user only, no admin** - with Windows' own winget, or the official python.org installer after checking it is signed by the Python Software Foundation. Progress every minute; plain words about Windows Defender making an old PC look frozen.
3. **ArcGIS Earth:** found (now including `C:\Program Files\ArcGIS\ArcGIS Earth\bin\ArcGISEarth.exe`), started if it is not running. If it is not installed: offers Esri's free download page (it never installs ArcGIS Earth itself).
4. **Automation API:** if ArcGIS Earth is open but not answering: "Settings > Advanced application settings > tick Enable Automation API", then Enter to check again.

Only one Ready to Fly runs at a time. A log is written to `System Files\Ready_To_Fly_log.txt`. Locked-down work PCs get a plain "ask IT" message. Source and notes: ArcGIS Earth Unlocked `tools/ready_to_fly/`.

## Hardening (re-hardening pass, approved by Jim: '12356 engage')

1. **One EarthStick at a time.** A second copy (an extra double-click on a slow PC) says "EarthStick is already running in another window" and stops, instead of two programs fighting over the camera (Windows named mutex `Local\EarthStick_single_instance`; if the check itself fails, EarthStick flies anyway).
2. **The tractor beam no longer pulls back mouse moves.** Hovering near a gate with the stick let go, 1.3.6 re-sent the last camera it knew, so panning with the mouse (two-handed flying) was undone - for up to ~10 s with dropped gates. 1.3.9 reads the camera fresh before each nudge and changes only the height. Rig `tools/test-rigs/earthstick_rig_mouse.py` (Unlocked repo): mouse panning 300 m - 1.3.6 pulled it back 149 of 150 updates (map moved 2 m), 1.3.9 0 of 150 (300 m); height pull identical (200 -> 490 m toward a 500 m gate).
3. **The status line fits the window** (at most 150 characters, else window width - 1), so it updates in place on a normal 120-column window instead of scrolling.
5. **Undo picks the right file:** the highest Dropped_Gate number (100 after 99), and only properly numbered gate files.
6. **The 'waiting for ArcGIS Earth' message names the exact setting.**

Held: 4 (ArcGIS Earth gets 0.75 s to answer each request; may be tight on old PCs - watch first).

## Proof

- Self-test PASS (new checks: undo order, single-instance off Windows).
- Rigs replay / unplugged_at_start / proxy / port_conflict / trigger-replay / trigger: identical to 1.3.6. Wormhole `--system-files` ALL PASS. Dropper ALL PASS. Mouse rig as above.
- Ready to Fly: tested here with PowerShell 7 and stand-ins (no Python, Python found, library missing offline, ArcGIS Earth missing / found / running with the API off, /find mode, winget stuck past its time limit, second copy); live on Jim's PC and his Windows 10 laptop.

## Files

`archive/EarthStick_v1.3.9.zip` SHA-256 `2352e1c6fe4facb7d727db7d5a0ba1abecc32cf439db32a5a93a0508f341126b` (folder `EarthStick_v1.3.9`, 20 files)

| File | SHA-256 |
|---|---|
| `System Files/EarthStick.py` | `1329169a6a02d3b55120f38dd17d0bbf2529ae8ee3b23c0bdf2f5d398a30e4bf` |
| `System Files/Ready_To_Fly.ps1` (new) | `b8ded20a71d8a0fd9fd4c5603aa60b60e9f5f15337d7f64579533c25b3a21dc3` |
| `Fly_ArcGIS_Earth.bat` (v2.0) | `92579f7c8e6476ff34444aaa2939c280008505ccfc2c078e08b3bdc286f2eb01` |
| `System Files/gate_dropper.py` | unchanged from 1.3.6 (`c0f7f1aa...`) |
