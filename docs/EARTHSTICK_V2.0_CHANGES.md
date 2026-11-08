# EarthStick 2.0 and World Gate Maker 2.0 - change document

**Released 2026-11-08 as part of the 2.0 Reference:** Jim moved the whole ArcGIS Earth Unlocked family to 2.0 as one reference point. EarthStick 2.0 = 1.3.11 TEST3 (live-accepted by Jim 15:48) + a wider notice line; World Gate Maker 2.0 = 1.2.2 TEST2 (live-tested 15:51). Test builds 1.3.11 TEST-TEST3 and 1.2.2 TEST-TEST2 lived on test branches.

## Why

Jim asked why a gate file opened with ArcGIS Earth's **Add Data** did nothing. ArcGIS Earth only *draws* it: its Automation API has no call that lists what is on the map (checked against Esri's documentation, 2026-11-08), so EarthStick cannot see it. EarthStick 1.3.10 also read its Gates folder only at startup, so new gates needed a restart, and World Gate Maker could not tell which of several EarthStick copies Jim was flying.

## EarthStick 2.0

1. **Gates picked up while flying.** Every 2 seconds EarthStick looks in its Gates folder. A new or changed gate file is armed and put on the map (`POST /arcgisearth/layer`) - gold notice **NEW GATES ARMED · name**; a removed file is disarmed and, if EarthStick drew it, taken off the map (**GATES DISARMED · name**). A file is read only after it looks the same on two looks in a row, so a half-written file is never read. Files dropped or undone with the trigger are not picked up twice.
2. **+ ADD GATES button** above the readout (clickable, does not take the keyboard from ArcGIS Earth). It opens gate files from anywhere, checks each one really holds gate data, copies it into the Gates folder - never over a different file of the same name (that becomes `name_2.kmz`; an identical file is not copied again) - and item 1 arms and shows it. Picking a file that is already in the Gates folder just shows it on the map.
3. **Last-flown note.** At startup EarthStick writes `%LOCALAPPDATA%\ArcGIS Earth Unlocked\last_earthstick.txt` (its Gates folder, version, start time). World Gate Maker 2.0 reads it.
4. **Gate Dropper uses World Gate Maker's kernel.** The two dropped gates now face each other; through one you land 300 m past the other, facing away from it - turn round once to go back. (1.3.6-1.3.10 faced each gate the way you looked when you pressed, which left the second gate backwards for a pair dropped along a line; TEST2's guess looped.) Gates still appear 500 m ahead of where you pressed, at your height; black look, wide grab zone and hold-to-undo unchanged. Gate files dropped earlier keep their own directions.
5. **Wider notice line** (1000 -> 1600 px) so long notices such as *NEW GATES ARMED · Gate_bry_jax* are not cut off (Jim's screenshot).

Flying with no gate changes is identical to 1.3.10 (replay, unplugged, proxy, port-conflict and trigger rigs: identical camera streams). Rigs: `earthstick_rig_pickup.py` (file appears half-written then complete, armed and shown once within 4 s, flown through, removed, + ADD GATES copy / duplicate / no-gates file, Gate Dropper shown once, note written) and `earthstick_rig_roundtrip.py` (pairs dropped with mark 2 looking 90 / 270 / 0 / 180: one hop per leg, home with one turn round, tractor beam on the way back) - both pass; 1.3.10's Dropper fails the round trip.

## World Gate Maker 2.0

- Saves into the Gates folder from EarthStick's note first (the EarthStick you fly), then the folder used last time, then the newest EarthStick folder nearby. A line under *Save into* says which: **running now**, **flown last**, **found nearby** - or, in red, **EarthStick not found** with what to do.
- **Choose...** accepts only an EarthStick Gates folder; picking the EarthStick folder or its System Files folder is corrected to its Gates folder. A deleted remembered folder is never re-created.
- The **Saved** message says whether EarthStick is running and will pick the gates up by itself, or needs starting.
- Also from 1.2.2: newest EarthStick by version number, `elev 85 ft` pasted as is, sharp text on scaled screens.
- Gate files are byte-identical to 1.2.1. Gates stay **gold** (Jim: the Gate Dropper's black gates are the "favorites").

**Needs:** World Gate Maker 2.0 needs EarthStick 2.0 to have been started once (for the note). Without it, it falls back to the folder used last time or the newest EarthStick nearby.
