# EarthStick 1.3.10

> 🤖 **Using AI assistance?** Have the agent read the [CLAUDE.md](https://github.com/Jim-dc95811/ArcGIS-Earth-Unlocked/blob/main/CLAUDE.md) file first.

[![Fly the real world in 7 steps: 1 get ArcGIS Earth, 2 turn on the Automation API, 3 get Python 3, 4 plug in the joystick (no driver needed), 5 download EarthStick and Extract All, 6 start it, 7 open the KMZ file, then fly through the gold side of a ring](images/earthstick_getting_started.png)](images/earthstick_getting_started_full.png)

*The whole setup on one page - click the picture for the full-size version.*

## Get everything you need

**1. ⬇️ [ArcGIS Earth](https://www.esri.com/en-us/arcgis/products/arcgis-earth/downloads)** - free 3D globe from Esri (Windows desktop version). After installing: Settings > Advanced > turn on **Automation API**.

**2. ⬇️ [Python 3](https://www.python.org/downloads/windows/)** - free; install with the default options.

**3. 🕹️ [Thrustmaster TCA Sidestick Airbus Edition](https://www.thrustmaster.com/en-us/products/tca-sidestick-airbus-edition/)** - the joystick EarthStick is built and tested with. Just plug it in by USB - Windows recognizes it by itself, no driver needed (the [Thrustmaster driver](https://support.thrustmaster.com/en/product/tca-sidestick-x-airbus-ed-en/#drivers) is optional).

> **First time? Three quick tips**
> 1. **Extract the zip first:** right-click the downloaded zip > **Extract All**, then open the new folder. Double-clicking files while they are still inside the zip does not work.
> 2. **Windows security warning:** Windows may warn about any program downloaded from the internet. Click **More info > Run anyway** (blue "Windows protected your PC" screen) or **Run**. To avoid the warning, right-click the zip > **Properties** > tick **Unblock** > **OK** before extracting.
> 3. **Installing Python:** if the installer shows **"Add python.exe to PATH"**, tick it.

### **⬇️ [4. DOWNLOAD EARTHSTICK v1.3.10](releases/EarthStick_v1.3.10.zip)**
**📖 [User manual](docs/USER_GUIDE.md)**
**🗂️ [What's in the zip - every file explained](images/earthstick_whats_in_the_folder_full.png)**
**📦 [Download the Whole ArcGIS Earth Unlocked Series of Tools - all 10 in one zip](https://github.com/Jim-dc95811/ArcGIS-Earth-Unlocked/raw/main/downloads/ArcGIS_Earth_Unlocked_All_Tools.zip)**

Fly the real map with a Thrustmaster TCA Sidestick and ArcGIS Earth desktop - and fly through golden **World Gates** that take you across the planet. **New in 1.3.10: the trigger drops gates** (Button 2 now clicks objects). **New in 1.3.9: Ready to Fly** - one double-click gets the PC ready: it installs Python for you if it is missing, starts ArcGIS Earth and checks it is ready to fly. New in 1.3.6: the Gate Dropper - press Button 2 at two places and a pair of gates appears there, no typing. New in 1.3.5: a tidy folder - one file to double-click. New in 1.3.4: square gates that show you how to line up, a green light when you're at the gate's height, and a tractor beam that guides you through. New in 1.3.3: your height, heading and map zoom on screen, even in full-screen mode. New in 1.3.1 and 1.3.2: a round-the-world tour with welcome signs and one-click site beacons, a bigger crosshair, and a one-click taskbar start.

[![Flying ArcGIS Earth with EarthStick: low over the St. Johns River with a beacon and sky compass letters on the horizon](images/earthstick_flight_arcgis_earth.jpg)](https://www.youtube.com/watch?v=5Wn14qlC7n4)

*Flying the real map: low over the St. Johns River, with an Object Factory beacon and sky compass on the horizon. ▶️ [Watch the video](https://www.youtube.com/watch?v=5Wn14qlC7n4) (YouTube).*

> **ArcGIS Earth Unlocked:** EarthStick is the navigation component of the broader project family. See the [master system map](https://github.com/Jim-dc95811/ArcGIS-Earth-Unlocked) and the [ArcGIS Earth Object Factory](https://github.com/Jim-dc95811/ArcGIS-Earth-Object-Factory).

**Fly the real map.**

EarthStick turns **ArcGIS Earth desktop** into a directly flyable map using a **Thrustmaster TCA Sidestick Airbus Edition**. Instead of simulating an aircraft inside a virtual world, EarthStick gives analog flight-style control to the ArcGIS Earth camera itself.

That means the environment remains a working map: satellite or aerial imagery, roads, street names, place labels, GIS layers, offline tile packages, and other ArcGIS Earth content stay available while you move through it.

> **Neutral controls = stop and hover in place.**

Push forward to travel. Pull back to reverse. Move the stick sideways to strafe. Twist to change heading. Use the throttle slider for speed, the POV hat for camera tilt, and the two top buttons to climb or descend. Release the controls and the camera stays where you left it. Pull the trigger to drop gates where you fly; press Button 2 to open the information box of whatever sits under the red crosshair.

![EarthStick control map](assets/EarthStick_controls.svg)

## Quick start

1. Plug the sidestick in by USB. No driver is needed - Windows recognizes it by itself (the Thrustmaster driver/control panel is optional).
2. Press `Win + R`, run `joy.cpl`, select the T.A320 controller, and verify X/Y, twist/RZ, Slider 0, POV, Button 1 (trigger), Button 2, Button 3, and Button 4.
3. Open ArcGIS Earth.
4. Open ArcGIS Earth settings and enable **Automation API** under **Advanced**.
5. Leave the default local API address at `http://localhost:8000` unless you intentionally changed it.
6. Extract `EarthStick_v1.3.10.zip` and open the `EarthStick_v1.3.10` folder.
7. Double-click `Fly_ArcGIS_Earth.bat` - it gets the PC ready (installs Python if it is missing - answer **Y**; on an older PC this can take several minutes), starts ArcGIS Earth if it is not open yet, checks the Automation API, then starts EarthStick (or set up the one-click taskbar start - see *One-click start* below).
8. Wait for the console to report `ArcGIS Earth: connected`. If the joystick is not plugged in yet, EarthStick waits for it.
9. Fly.

**What's in the folder you just extracted** (click the picture for a bigger copy):

[![What's in the EarthStick folder: Fly_ArcGIS_Earth.bat is the go button, Gates holds the World Gates, City_Beacons has shortcuts to 9 cities, System Files holds the program (leave it alone)](images/earthstick_whats_in_the_folder.png)](images/earthstick_whats_in_the_folder_full.png)

## Controls

| Physical control | EarthStick action |
|---|---|
| Stick forward / back | Fly forward / reverse |
| Stick left / right | Strafe left / right |
| Stick twist / RZ | Change heading |
| Slider 0 / throttle | Travel speed |
| POV hat up / down | Camera tilt |
| Red top button - Button 4 | Hold to zoom in / descend |
| Black thumb button - Button 3 | Hold to zoom out / climb |
| Trigger - Button 1 - press | Gate Dropper: mark a place (press at two places = a gate pair) (1.3.10; was Button 2) |
| Trigger - Button 1 - hold 2 s | Undo the last gate drop |
| Button 2 | Click the object under the red crosshair (opens its information box; on open map, closes it) (1.3.10; was the trigger) |
| Neutral controls | Stop and hover in place |

Other joystick buttons are intentionally unassigned.

### Trigger-click (new in 1.2)

![The red crosshair in the middle of the ArcGIS Earth window, beside a camera object over the SR-200 / I-95 interchange](images/earthstick_trigger_click_crosshair.jpg)

A red crosshair sits in the middle of the ArcGIS Earth window. Fly an object (here, a camera) under it, let go so you hover, and press **Button 2** (the trigger until 1.3.9): its information box opens. To close the box, aim at open map and press Button 2 again.

### World Gates (1.3; round-the-world tour in 1.3.1)

[![Eight golden World Gates in a circle around Atlanta's Hartsfield-Jackson airport, labeled NYC, London, Paris, Rome, JAX, Rio, Sydney and Tokyo](images/world_gates_atl_hub_arcgis_earth.jpg)](https://www.youtube.com/watch?v=2N8-4cWMoPw)

*The World Gates hub over Atlanta, filmed when the gates were round (1.3). ▶️ [Watch the video: ArcGIS Earth Flight - City to City Using Wormholes](https://www.youtube.com/watch?v=2N8-4cWMoPw) (YouTube).*

Golden gates float in the sky. **Fly through one and you come out on the other side of the world.** EarthStick comes with the **World Gates** pack (v21, since 1.3.4):

- **Square gates with legs (new in 1.3.4):** each gate is a gold square with four legs running back the way you fly. Lined up, the legs make an even X; off line, they lean toward where you need to go.
- **Ring-height light and tractor beam (new in 1.3.4):** a green **● RING HEIGHT** comes on above the readout when you're at the height of the gate you're flying toward; get within about a mile and **● LOCKED ON** - EarthStick glides you onto its height. Climb or descend lets go.

- **Jacksonville to Atlanta:** a gate over Jacksonville International takes you to a hub over Atlanta's airport, where eight gates in a circle lead to New York, London, Paris, Rome, Tokyo, Sydney, Rio and home to Jacksonville - connect in Atlanta, just like real flights.
- **Round-the-world tour (new in 1.3.1):** every city also has a gate to the next one - New York, London, Paris, Rome, Tokyo, Sydney, Rio - and Rio's onward gate brings you back to Atlanta. Each city still has its **ATL** gate home.
- **Welcome signs (new in 1.3.1):** you arrive facing the landmark with "Welcome to ..." floating ahead of you, up in the sky.
- **Sites with beacons (new in 1.3.1):** under the sign, five gold stars in two rows name the city's famous sites, all in clear sky well away from the gates. Aim the crosshair at a star and press Button 2: a beacon in that site's colour shoots up over it to guide you there. To clear a beacon, untick it under **My Drawings** on the left. Atlanta and Jacksonville have their own five sites too.
- Signs, stars and gate names only show when you are near (within about 4 miles), so the view stays clean from far away.

[![Arriving in London: Welcome to London high in the sky, with five coloured site names above gold stars in two rows - Tower Bridge, Tower of London, St Paul's Cathedral, London Eye, Big Ben](images/world_gates_london_sky_board_arcgis_earth.jpg)](https://www.youtube.com/watch?v=2N8-4cWMoPw)

*Coming out of a gate in London (1.3.2): the welcome sign and the city's five sites up in the sky.*

![Paris with two site beacons up: an orange beacon on Sacre-Coeur and a red one on the Eiffel Tower](images/world_gates_paris_beacons_arcgis_earth.jpg)

*Paris after two clicks: orange beacon on Sacré-Cœur, red on the Eiffel Tower.*

1. Open the **World Gates** file in ArcGIS Earth: drag `Gates\World_Gates_JAX_ATL_v21.kmz` (in the EarthStick folder) onto the map, so you can see the gates.
2. Start EarthStick. The console lists the gates it armed: `Wormholes: 22 gate(s) armed: ATL, JAX, NYC, ...`
3. Fly to a gate and put it under the crosshair, gold side toward you (from the red side nothing happens). Look down the legs - an even X means lined up. The green light (and the tractor beam, close in) takes care of the height. Fly through the middle.
4. The view jumps to the destination and the console says `Wormhole: through the ... gate.` You arrive still flying, already facing the landmark.

Gold side = way in. Red side = wrong way. The number under each name is the eye alt to fly at. Want the gates without EarthStick, just to look at? [Download the World Gates file](https://github.com/Jim-dc95811/EarthStick/raw/main/gates/World_Gates_JAX_ATL_v21.kmz) and drag it onto ArcGIS Earth.

**Shortcut to any city:** the `City_Beacons` folder holds nine red beacons (Go to Jacksonville, Go to Atlanta, Go to Paris ...). Drag them onto ArcGIS Earth, then double-click one in the Data list to jump straight there without the gates (you arrive above it; nudge the view to see the beacon). Also available as a [separate download](https://github.com/Jim-dc95811/EarthStick/raw/main/gates/World_Gates_City_Beacons_v2.zip).

### Drop gates as you fly (new in 1.3.6)

No coordinates, no typing: fly to a place, face the way you want to go, and pull the **trigger** (Button 1; Button 2 before 1.3.10). Fly to a second place and pull it again. A pair of gates appears, each **500 m in front of where you pressed**, at your height, facing your way. Push forward and fly through. **Hold the trigger for 2 seconds** to undo. Dropped gates are thin and black so they stay quiet over a painting or a picture world, and they lock on from 3 km out and 2,000 ft above or below, with a countdown.

![A thin black dropped gate down in Bruegel's Tower of Babel, among the workers on the scaffolding](images/gate_dropper_babel_black_gate.jpg)

*A dropped gate down among Bruegel's workers in the Tower of Babel (a picture world made with [Picture World Maker](https://github.com/Jim-dc95811/Picture-World-Maker)) - fly through it and you come out in London.*

![LOCKED ON at 560 ft: the countdown to the dropped gate in the London panorama](images/gate_dropper_london_locked_on_countdown.jpg)

*On the way back in: LOCKED ON · 560 ft - the light counts down to the gate.*

### Make your own gates

### **⬇️ [DOWNLOAD WORLD GATE MAKER v1.2.1](releases/World_Gate_Maker_v1.2.1.zip)**
**📖 [User manual](docs/WORLD_GATE_MAKER.md)**
**🗂️ [What's in the zip - every file explained](images/world_gate_maker_whats_in_the_zip_full.png)**
**📦 [Download the Whole ArcGIS Earth Unlocked Series of Tools - all 10 in one zip](https://github.com/Jim-dc95811/ArcGIS-Earth-Unlocked/raw/main/downloads/ArcGIS_Earth_Unlocked_All_Tools.zip)**

Pick two places - home and Central Park, a fire station and a hospital - and World Gate Maker builds a pair of golden gates between them for EarthStick. New in 1.2: a tidy folder - `World_Gate_Maker.bat` plus `System Files`. New in 1.1: square gates with legs, like the World Gates pack - one glance shows the way in. **New in 1.2.1 (Ready to Fly):** the .bat installs Python for you if it is missing - answer **Y**, no admin needed.

![A square World Gate named jax seen from the side over Seattle: the gold square and its legs make a box that points the way in](images/world_gate_maker_v1.1_seattle_arrival.jpg)

*Jacksonville to Seattle and back with World Gate Maker 1.1: the "jax" gate home, seen from the side in Seattle.*

Type a name for each place, paste its coordinates from Google Maps (**From Clipboard**), type the ground **elev** from ArcGIS Earth's status bar, choose a height and gate size, and press **MAKE GATES**. The file goes straight into your EarthStick **Gates** folder; restart EarthStick and fly. `World_Gate_Maker_v1.2.zip` SHA-256: `d06c88152c40f6d08b3df382948cebb0dbe1962cf1572be79c4c655e7e03549f` ([what changed in 1.2](docs/WORLD_GATE_MAKER_V1.2_CHANGES.md))

### One-click start (new in 1.3.1)

Put **ArcGIS Earth Flight** on your taskbar: one click starts ArcGIS Earth, then EarthStick.

1. In the EarthStick folder, open **System Files** and double-click `Make_Taskbar_Shortcut.bat` once. It finds ArcGIS Earth and puts an **ArcGIS Earth Flight** shortcut (ArcGIS Earth icon) on your desktop.
2. Right-click the shortcut > **Show more options** > **Pin to taskbar**.

Clicking it starts ArcGIS Earth (unless it is already open), then EarthStick, which waits until ArcGIS Earth is ready. You can also just double-click `Fly_ArcGIS_Earth.bat`.

## Release details

**EarthStick 1.3.10** (2026-11-08) - the trigger drops gates (press at two places, hold 2 s to undo) and Button 2 clicks the object under the crosshair, for two-handed flying with the mouse. Everything else as 1.3.9. See [docs/EARTHSTICK_V1.3.10_CHANGES.md](docs/EARTHSTICK_V1.3.10_CHANGES.md).

**EarthStick 1.3.9** (2026-11-08) - Ready to Fly: the launcher checks the internet, finds or installs Python (per user, no admin), finds and starts ArcGIS Earth (or offers Esri's download page) and checks the Automation API; plus hardening: one copy at a time, the tractor beam respects mouse moves while hovering, the status line fits the window, undo by gate number, clearer API message. Flying, gates and the Gate Dropper as 1.3.6. See [docs/EARTHSTICK_V1.3.9_CHANGES.md](docs/EARTHSTICK_V1.3.9_CHANGES.md).

**EarthStick 1.3.6** (2026-11-06) - the Gate Dropper: Button 2 drops gate pairs where you fly (500 m ahead, your height, your heading), hold Button 2 to undo; dropped gates are thin black with a 425 m opening and lock on from 3 km / 2,000 ft; the LOCKED ON light counts down the distance. Flying with no Button 2 is identical to 1.3.5. See [docs/EARTHSTICK_V1.3.6_CHANGES.md](docs/EARTHSTICK_V1.3.6_CHANGES.md).

**EarthStick 1.3.5** (2026-11-06) - one obvious file: the folder shows only `Fly_ArcGIS_Earth.bat`, `Gates`, `City_Beacons` and `System Files`. Flying is identical to 1.3.4 (World Gates v21, ring-height light, tractor beam). See [docs/EARTHSTICK_V1.3.5_CHANGES.md](docs/EARTHSTICK_V1.3.5_CHANGES.md).

![A square ATL gate over London with the tractor beam LOCKED ON at 1,500 ft](images/world_gates_v21_locked_on.jpg)

`EarthStick_v1.3.10.zip` SHA-256:

`18229d3ebf8c7dbb1c6acf4e080ed50803c75263dd7fc5234c85fcf399c8a4c3`

The release contains one folder, `EarthStick_v1.3.10`, holding `Fly_ArcGIS_Earth.bat`, the user guide `EarthStick_User_Guide.pdf`, `Gates\World_Gates_JAX_ATL_v21.kmz`, a `City_Beacons` folder and `System Files` (`EarthStick.py`, `gate_dropper.py`, `Ready_To_Fly.ps1`, `EarthStick.bat`, `Make_Taskbar_Shortcut.bat`).

**Earlier releases** (1.3.9, 1.3.6, 1.3.5, 1.3.4, 1.3.3, 1.3.2, 1.3.1, 1.3, 1.2, 1.1, 1.0): their zips stay in [`releases/`](releases/) so existing links keep working. What changed in each, with file fingerprints, is in the [release history](CHANGELOG.md) and the change documents listed under *Documentation*.

## What makes EarthStick different

EarthStick is not mouse emulation and it is not keyboard remapping. It reads the joystick through Windows and sends camera position directly through the **ArcGIS Earth Automation API**.

The result is a control model built around observation rather than aircraft physics:

- **hover anywhere** by returning the controls to neutral
- **strafe sideways** without turning
- **reverse** without turning around
- **pivot heading in place**
- **climb or descend independently** of forward motion
- **change travel speed independently** with the throttle slider
- move from street-level inspection to continent-scale travel and back with the same controls
- use the same camera-control model with online maps or offline ArcGIS Earth content

A flight simulator moves an aircraft through scenery. **EarthStick moves you through the map.**

## Requirements

- **Windows 11**
- **ArcGIS Earth desktop**
- **ArcGIS Earth Automation API enabled**
- **Python 3.x** - tested with Python 3.14.5
- **Thrustmaster TCA Sidestick Airbus Edition** connected by USB
- the EarthStick folder (`Fly_ArcGIS_Earth.bat` + `System Files`)
- Thrustmaster driver/control panel optional - not needed (proven 2026-11-08 on a PC that never had it)

The tested controller appears in Windows as **T.A320 Pilot**. EarthStick also contains a capability-based fallback for installations where WinMM exposes the device using a generic joystick-driver name.

## Documentation

How EarthStick works inside - the movement math, technical constants, architecture and how it recovers when the joystick or ArcGIS Earth drops out - is in [`docs/TECHNICAL_NOTES.md`](docs/TECHNICAL_NOTES.md).

- [`docs/USER_GUIDE.md`](docs/USER_GUIDE.md) - installation and operation
- [`docs/EarthStick_User_Guide.pdf`](docs/EarthStick_User_Guide.pdf) - printable user guide
- [`docs/TECHNICAL_NOTES.md`](docs/TECHNICAL_NOTES.md) - architecture, movement math, API recovery, constants
- [`docs/TROUBLESHOOTING.md`](docs/TROUBLESHOOTING.md) - failure checks and recovery
- [`docs/HARDWARE_MAP.md`](docs/HARDWARE_MAP.md) - tested controller mapping
- [`docs/WORLD_GATE_MAKER.md`](docs/WORLD_GATE_MAKER.md) - World Gate Maker user manual ([PDF](docs/World_Gate_Maker_User_Manual.pdf))
- [`docs/EARTHSTICK_V1.3.10_CHANGES.md`](docs/EARTHSTICK_V1.3.10_CHANGES.md) - 1.3.10 change document (trigger = Gate Dropper, Button 2 = click)
- [`docs/EARTHSTICK_V1.3.9_CHANGES.md`](docs/EARTHSTICK_V1.3.9_CHANGES.md) - 1.3.9 change document (Ready to Fly launcher, hardening)
- [`docs/EARTHSTICK_V1.3.4_CHANGES.md`](docs/EARTHSTICK_V1.3.4_CHANGES.md) - 1.3.4 change document (square gates, ring-height light, tractor beam)
- [`docs/EARTHSTICK_V1.3.3_CHANGES.md`](docs/EARTHSTICK_V1.3.3_CHANGES.md) - 1.3.3 change document (height / heading / zoom readout)
- [`docs/EARTHSTICK_V1.3.2_CHANGES.md`](docs/EARTHSTICK_V1.3.2_CHANGES.md) - 1.3.2 change document (World Gates v19)
- [`docs/EARTHSTICK_V1.3.1_CHANGES.md`](docs/EARTHSTICK_V1.3.1_CHANGES.md) - 1.3.1 change document
- [`docs/EARTHSTICK_V1.3_CHANGES.md`](docs/EARTHSTICK_V1.3_CHANGES.md) - 1.3 change document and verification record
- [`docs/EARTHSTICK_V1.2_CHANGES.md`](docs/EARTHSTICK_V1.2_CHANGES.md) - 1.2 change document
- [`docs/EARTHSTICK_V1.1_CHANGES.md`](docs/EARTHSTICK_V1.1_CHANGES.md) - 1.1 change document
- [`CHANGELOG.md`](CHANGELOG.md) - release history

## Human-AI engineering collaboration

EarthStick was conceived, directed, flown and live-tested by **Jim Gaddy**, working with **OpenAI's ChatGPT** and **Anthropic's Claude** as AI coding and documentation partners. Jim supplied the idea of flying the map itself, every feature request, the joystick and ArcGIS Earth acceptance tests and the screenshots that measured how ArcGIS Earth really behaves. ChatGPT helped build the original EarthStick (up to 1.0). Claude built every release since: the 1.1 hardening, trigger-click (1.2), **World Gates** and the round-the-world pack (1.3-1.3.2), City Beacons and the one-click launcher, the height / heading / zoom readout (1.3.3), square gates, the ring-height light and the tractor beam (1.3.4), and **World Gate Maker** - plus the test rigs, the viewer model used to lay out everything in the sky, the user guides and the picture guides.

This acknowledgment is not a claim of OpenAI or Anthropic sponsorship or endorsement.

## Safety and scope

EarthStick controls the **ArcGIS Earth map camera**. It is not an aircraft flight-control system, certified navigation system, dispatch system, or safety-of-life product. Users remain responsible for validating maps, layers, imagery, coordinates, and operational procedures.

## License

MIT License. See [`LICENSE`](LICENSE).

## References

- Esri - ArcGIS Earth Automation API overview: https://doc.arcgis.com/en/arcgis-earth/automation-api/overview.htm
- Esri - Using ArcGIS Earth Automation API: https://doc.arcgis.com/en/arcgis-earth/automation-api/use-api.htm
- Esri - Set Camera: https://doc.arcgis.com/en/arcgis-earth/automation-api/set-camera.htm
- Thrustmaster - TCA Sidestick Airbus Edition: https://www.thrustmaster.com/en-us/products/tca-sidestick-airbus-edition/
- Microsoft - `joyGetPosEx`: https://learn.microsoft.com/en-us/windows/win32/api/joystickapi/nf-joystickapi-joygetposex

## Status

**EarthStick 1.3.4 is the current release.** The previous packages remain at `releases/EarthStick_v1.3.3.zip`, `releases/EarthStick_v1.3.2.zip`, `releases/EarthStick_v1.3.1.zip`, `releases/EarthStick_v1.3.zip`, `releases/EarthStick_v1.2.zip`, `releases/EarthStick_v1.1.zip` and `releases/EarthStick_v1.0.zip` for existing links.