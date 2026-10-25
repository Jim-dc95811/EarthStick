# EarthStick

**Helicopter-style joystick control for ArcGIS Earth on Windows.**

EarthStick connects a **Thrustmaster TCA Sidestick Airbus Edition** to the **ArcGIS Earth Automation API** and turns the Earth camera into a continuously navigable 3D space.

The defining behavior is simple:

> **Neutral controls = stop and hover in place.**

Push the stick to move. Twist to turn. Use the POV hat to tilt. Use the throttle slider to control travel speed. Hold two top buttons to zoom in or out. Release the controls and the camera stays where you left it.

![EarthStick control map](assets/EarthStick_controls.svg)

## Current release

**EarthStick v0.5** - tested working baseline, 2026-10-25.

Download the packaged release from:

- [`releases/EarthStick_v0.5.zip`](releases/EarthStick_v0.5.zip)

The release contains only:

- `EarthStick.py`
- `EarthStick.bat`

No third-party Python packages are required.

## What it controls

| Physical control | EarthStick action |
|---|---|
| Stick forward / back | Fly forward / reverse |
| Stick left / right | Strafe left / right |
| Stick twist / RZ | Change heading |
| Slider 0 / throttle | Movement speed |
| POV hat up / down | Camera tilt |
| Red trigger - Button 4 | Hold to zoom in / descend |
| Black thumb - Button 3 | Hold to zoom out / climb |
| Neutral controls | Stop and hover in place |

Everything else is intentionally left unassigned in v0.5.

## Why it feels different

EarthStick does not emulate a mouse, keyboard, or game command. It talks directly to ArcGIS Earth's camera through Esri's local REST Automation API.

The joystick supplies independent physical axes. EarthStick continuously translates those axes into camera position, heading, tilt, altitude, and travel speed.

That produces a control model closer to piloting a helicopter than manipulating a 3D scene:

- motion is commanded only while you ask for it
- neutral means hold position
- heading and translation can be changed together
- speed is independent of stick deflection
- altitude/zoom is independent of forward motion
- camera tilt is independent of heading

## Requirements

- Windows 10 or Windows 11
- ArcGIS Earth desktop
- ArcGIS Earth Automation API enabled
- Python 3
- Thrustmaster TCA Sidestick Airbus Edition connected by USB
- Thrustmaster driver/control panel recommended

EarthStick was developed and field-tested with the controller appearing in Windows as **T.A320 Pilot**. Some Windows installations expose the underlying WinMM device using the generic name `Microsoft PC-joystick driver`; v0.5 includes a capability-based fallback for this case.

## Quick start

1. Install the Thrustmaster driver package and connect the sidestick directly to the PC.
2. Press `Win + R`, run `joy.cpl`, select the T.A320 controller, and verify X/Y, rudder/twist, throttle, POV, and buttons respond.
3. Open ArcGIS Earth.
4. In ArcGIS Earth settings, enable **Automation API** under **Advanced**.
5. Leave the default Automation API address at `http://localhost:8000` unless you intentionally changed it.
6. Extract `EarthStick_v0.5.zip`.
7. Double-click `EarthStick.bat`.
8. Wait for the console to report `ArcGIS Earth: connected`.
9. Fly.

Detailed setup and troubleshooting are in [`docs/USER_GUIDE.md`](docs/USER_GUIDE.md) and [`docs/TROUBLESHOOTING.md`](docs/TROUBLESHOOTING.md).

## Architecture at a glance

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

EarthStick uses Python's standard library plus Windows `winmm.dll` through `ctypes`. The current build polls the joystick at 30 Hz and updates the ArcGIS Earth camera using `GET /arcgisearth/camera` and `PUT /arcgisearth/camera`.

See [`docs/TECHNICAL_NOTES.md`](docs/TECHNICAL_NOTES.md) for the implementation details and movement math.

## Design principles

EarthStick is intentionally small.

- Do not assign buttons just because buttons exist.
- Preserve neutral/hover behavior.
- Keep movement controls independent and predictable.
- Prefer direct camera control over mouse/keyboard emulation.
- Avoid external Python dependencies when the Windows standard interfaces already provide what is needed.
- Change one behavior at a time and test it in ArcGIS Earth before adding another.

## Repository map

- `EarthStick.py` - tested v0.5 controller bridge
- `EarthStick.bat` - Windows launcher
- `releases/EarthStick_v0.5.zip` - packaged tested release
- `assets/EarthStick_controls.svg` - scalable control pictogram
- `assets/EarthStick_YouTube_Thumbnail.jpg` - prepared 1280x720 video thumbnail
- `docs/USER_GUIDE.md` - setup and operating manual
- `docs/TECHNICAL_NOTES.md` - architecture, APIs, math, constants
- `docs/TROUBLESHOOTING.md` - failure modes and checks
- `docs/HARDWARE_MAP.md` - observed axes and button numbers
- `docs/FIELD_TEST.md` - first accepted v0.5 flight test
- `docs/VIDEO_GUIDE.md` - video title, description, and demo sequence
- `docs/PROJECT_NOTES.md` - project origin and design rationale
- `ACKNOWLEDGEMENTS.md` - Esri, Thrustmaster, Microsoft, Python, trademark notes
- `CHANGELOG.md` - version history
- `CONTINUITY.md` - exact project state and modification rules for future work

## Video thumbnail

The repository includes a thumbnail prepared from the first working EarthStick flight recording:

![EarthStick video thumbnail](assets/EarthStick_YouTube_Thumbnail.jpg)

## Safety and scope

EarthStick is a camera-control utility for ArcGIS Earth. It is **not** an aircraft flight-control system, certified navigation system, dispatch system, or safety-of-life product. Users remain responsible for validating the maps, layers, imagery, coordinates, and operational procedures used with ArcGIS Earth.

## License

MIT License. See [`LICENSE`](LICENSE).

## References

- Esri - ArcGIS Earth Automation API overview: https://doc.arcgis.com/en/arcgis-earth/automation-api/overview.htm
- Esri - Using ArcGIS Earth Automation API: https://doc.arcgis.com/en/arcgis-earth/automation-api/use-api.htm
- Esri - Set Camera: https://doc.arcgis.com/en/arcgis-earth/automation-api/set-camera.htm
- Thrustmaster - TCA Sidestick Airbus Edition: https://www.thrustmaster.com/en-us/products/tca-sidestick-airbus-edition/
- Thrustmaster - PC installation and testing guide: https://support.thrustmaster.com/en/kb/1764-en/
- Microsoft - `joyGetPosEx`: https://learn.microsoft.com/en-us/windows/win32/api/joystickapi/nf-joystickapi-joygetposex

## Project status

**v0.5 works.** The current goal is to preserve that behavior, document it clearly, and only add new functions when a real operational need appears.
