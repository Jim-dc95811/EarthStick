# EarthStick 1.3

## Get everything you need

**1. ⬇️ [ArcGIS Earth](https://www.esri.com/en-us/arcgis/products/arcgis-earth/downloads)** - free 3D globe from Esri (Windows desktop version). After installing: Settings > Advanced > turn on **Automation API**.

**2. ⬇️ [Python 3](https://www.python.org/downloads/windows/)** - free; install with the default options.

**3. 🕹️ [Thrustmaster TCA Sidestick Airbus Edition](https://www.thrustmaster.com/en-us/products/tca-sidestick-airbus-edition/)** - the joystick EarthStick is built and tested with.

> **First time? Three quick tips**
> 1. **Extract the zip first:** right-click the downloaded zip > **Extract All**, then open the new folder. Double-clicking files while they are still inside the zip does not work.
> 2. **Windows security warning:** Windows may warn about any program downloaded from the internet. Click **More info > Run anyway** (blue "Windows protected your PC" screen) or **Run**. To avoid the warning, right-click the zip > **Properties** > tick **Unblock** > **OK** before extracting.
> 3. **Installing Python:** if the installer shows **"Add python.exe to PATH"**, tick it.

### **⬇️ [4. DOWNLOAD EARTHSTICK v1.3](releases/EarthStick_v1.3.zip)**
**📖 [User manual](docs/USER_GUIDE.md)**

Fly the real map with a Thrustmaster TCA Sidestick and ArcGIS Earth desktop - and, new in 1.3, fly through golden **World Gates** that take you across the planet.

[![Flying ArcGIS Earth with EarthStick: low over the St. Johns River with a beacon and sky compass letters on the horizon](images/earthstick_flight_arcgis_earth.jpg)](https://www.youtube.com/watch?v=5Wn14qlC7n4)

*Flying the real map: low over the St. Johns River, with an Object Factory beacon and sky compass on the horizon. ▶️ [Watch the video](https://www.youtube.com/watch?v=5Wn14qlC7n4) (YouTube).*

> **ArcGIS Earth Unlocked:** EarthStick is the navigation component of the broader project family. See the [master system map](https://github.com/Jim-dc95811/ArcGIS-Earth-Unlocked) and the [ArcGIS Earth Object Factory](https://github.com/Jim-dc95811/ArcGIS-Earth-Object-Factory).

**Fly the real map.**

EarthStick turns **ArcGIS Earth desktop** into a directly flyable map using a **Thrustmaster TCA Sidestick Airbus Edition**. Instead of simulating an aircraft inside a virtual world, EarthStick gives analog flight-style control to the ArcGIS Earth camera itself.

That means the environment remains a working map: satellite or aerial imagery, roads, street names, place labels, GIS layers, offline tile packages, and other ArcGIS Earth content stay available while you move through it.

> **Neutral controls = stop and hover in place.**

Push forward to travel. Pull back to reverse. Move the stick sideways to strafe. Twist to change heading. Use the throttle slider for speed, the POV hat for camera tilt, and the two top buttons to climb or descend. Release the controls and the camera stays where you left it. Pull the trigger to open the information box of whatever sits under the red crosshair.

![EarthStick control map](assets/EarthStick_controls.svg)

## Quick start

1. Install the Thrustmaster driver/control panel and connect the sidestick by USB.
2. Press `Win + R`, run `joy.cpl`, select the T.A320 controller, and verify X/Y, twist/RZ, Slider 0, POV, Button 1 (trigger), Button 3, and Button 4.
3. Open ArcGIS Earth.
4. Open ArcGIS Earth settings and enable **Automation API** under **Advanced**.
5. Leave the default local API address at `http://localhost:8000` unless you intentionally changed it.
6. Extract `EarthStick_v1.3.zip` and open the `EarthStick_v1.3` folder.
7. Double-click `EarthStick.bat`.
8. Wait for the console to report `ArcGIS Earth: connected`. If the joystick is not plugged in yet, EarthStick waits for it.
9. Fly.

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
| Trigger - Button 1 | Click the object under the red crosshair (opens its information box; on open map, closes it) |
| Neutral controls | Stop and hover in place |

Other joystick buttons are intentionally unassigned.

### Trigger-click (new in 1.2)

![The red crosshair in the middle of the ArcGIS Earth window, beside a camera object over the SR-200 / I-95 interchange](images/earthstick_trigger_click_crosshair.jpg)

A red crosshair sits in the middle of the ArcGIS Earth window. Fly an object (here, a camera) under it, let go so you hover, and pull the trigger: its information box opens. To close the box, aim at open map and pull the trigger again.

### World Gates (new in 1.3)

[![Eight golden World Gates in a circle around Atlanta's Hartsfield-Jackson airport, labeled NYC, London, Paris, Rome, JAX, Rio, Sydney and Tokyo](images/world_gates_atl_hub_arcgis_earth.jpg)](images/world_gates_atl_hub_arcgis_earth.jpg)

Golden rings float in the sky. **Fly through one and you come out on the other side of the world.** EarthStick 1.3 comes with the **World Gates** pack: a gate over Jacksonville International takes you to a hub over Atlanta's airport, where eight gates in a circle lead to New York (Statue of Liberty), London (Tower Bridge), Paris (Eiffel Tower), Rome (Colosseum), Tokyo (Tokyo Tower), Sydney (Opera House), Rio (Christ the Redeemer) and home to Jacksonville. Every city has a gate back to Atlanta - connect there, just like real flights.

![Approaching the Paris gate over Atlanta: a gold ring with the label Paris and the altitude 2,530 ft beside it](images/world_gates_paris_ring_arcgis_earth.jpg)

1. Open the **World Gates** file in ArcGIS Earth: drag `Gates\World_Gates_JAX_ATL.kmz` (in the EarthStick folder) onto the map, so you can see the rings.
2. Start EarthStick. The console lists the gates it armed: `Wormholes: 16 gate(s) armed: ATL, JAX, NYC, ...`
3. Fly to a ring, line up on its **gold** side (from the red side nothing happens), match the altitude shown under its name using **eye alt** at the bottom of ArcGIS Earth, and fly through the middle.
4. The view jumps to the destination and the console says `Wormhole: through the ... gate.` You arrive still flying, already facing the landmark.

Gold side = way in. Red side = wrong way. The number under each name is the eye alt to fly at. Want the rings without EarthStick, just to look at? [Download the World Gates file](https://github.com/Jim-dc95811/EarthStick/raw/main/gates/World_Gates_JAX_ATL.kmz) and drag it onto ArcGIS Earth.

## Release details

**EarthStick 1.3** (2026-11-02) - World Gates: fly through a golden ring and the camera jumps to its destination. Gate files go in the `Gates` folder beside EarthStick; the World Gates pack (JAX -> ATL hub -> 7 world landmarks) is included. With no gate files, flying is identical to 1.2. See [docs/EARTHSTICK_V1.3_CHANGES.md](docs/EARTHSTICK_V1.3_CHANGES.md).

`EarthStick_v1.3.zip` SHA-256:

`0e8c394748f428eef42fed5aa1da5e5d317557082505ad4ca52e4d271ce0731f`

The release contains one folder, `EarthStick_v1.3`, holding `EarthStick.py`, `EarthStick.bat` and `Gates\World_Gates_JAX_ATL.kmz`.

**EarthStick 1.2** (2026-11-01) - trigger-click: a red crosshair in the middle of the ArcGIS Earth window, and the trigger clicks whatever is under it, so information boxes open and close without the mouse. Flying is identical to 1.1. See [docs/EARTHSTICK_V1.2_CHANGES.md](docs/EARTHSTICK_V1.2_CHANGES.md).

No third-party Python packages are required (the crosshair uses Tkinter, part of the standard Python install).

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
- `EarthStick.py` and `EarthStick.bat`
- Thrustmaster driver/control panel recommended

The tested controller appears in Windows as **T.A320 Pilot**. EarthStick also contains a capability-based fallback for installations where WinMM exposes the device using a generic joystick-driver name.

## Built-in recovery behavior

EarthStick is designed to keep a temporary hardware or ArcGIS Earth interruption from turning into a crash or a camera jump.

- If the ArcGIS Earth API disappears, EarthStick stops sending movement, waits for the API to return, then re-reads the live camera before resuming.
- If the joystick is unplugged, EarthStick remains running, waits for the controller to return, accepts a newly assigned Windows joystick ID, and re-synchronizes from the current ArcGIS Earth camera before movement resumes.
- Camera data is validated before it is accepted.
- The movement time step is bounded so a temporary stall cannot create one giant movement command.

## Technical constants

| Setting | Value |
|---|---:|
| Poll rate | 30 Hz |
| Deadzone | 0.08 |
| Heading rate | 55 deg/s |
| Tilt rate | 45 deg/s |
| Idle camera resync | 0.50 s |
| HTTP timeout | 0.75 s |
| Minimum altitude | 1 m |
| Maximum travel multiplier | 60x altitude-aware base speed |

The throttle uses a squared response curve to preserve fine low-speed control while still allowing very high travel speed at altitude.

## Architecture

```text
Thrustmaster TCA Sidestick
          |
          | Windows joystick state
          v
   WinMM / joyGetPosEx
          |
          v
      EarthStick.py
          |
          | HTTP GET/PUT camera JSON
          v
ArcGIS Earth Automation API
 http://localhost:8000
          |
          v
   ArcGIS Earth camera
```

## Documentation

- [`docs/USER_GUIDE.md`](docs/USER_GUIDE.md) - installation and operation
- [`docs/EarthStick_User_Guide.pdf`](docs/EarthStick_User_Guide.pdf) - printable user guide
- [`docs/TECHNICAL_NOTES.md`](docs/TECHNICAL_NOTES.md) - architecture, movement math, API recovery, constants
- [`docs/TROUBLESHOOTING.md`](docs/TROUBLESHOOTING.md) - failure checks and recovery
- [`docs/HARDWARE_MAP.md`](docs/HARDWARE_MAP.md) - tested controller mapping
- [`docs/EARTHSTICK_V1.3_CHANGES.md`](docs/EARTHSTICK_V1.3_CHANGES.md) - 1.3 change document and verification record
- [`docs/EARTHSTICK_V1.2_CHANGES.md`](docs/EARTHSTICK_V1.2_CHANGES.md) - 1.2 change document
- [`docs/EARTHSTICK_V1.1_CHANGES.md`](docs/EARTHSTICK_V1.1_CHANGES.md) - 1.1 change document
- [`CHANGELOG.md`](CHANGELOG.md) - release history

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

**EarthStick 1.3 is the official accepted release.** The previous packages remain at `releases/EarthStick_v1.2.zip`, `releases/EarthStick_v1.1.zip` and `releases/EarthStick_v1.0.zip` for existing links.