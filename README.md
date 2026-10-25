# EarthStick

**Helicopter-style joystick control for ArcGIS Earth on Windows.**

EarthStick connects a **Thrustmaster TCA Sidestick Airbus Edition** to the **ArcGIS Earth Automation API** and turns the Earth camera into a continuously navigable 3D space.

The defining behavior is simple:

> **Neutral controls = stop and hover in place.**

Push the stick to move. Twist to turn. Use the POV hat to tilt. Use the throttle slider to control travel speed. Hold two top buttons to zoom in or out. Release the controls and the camera stays where you left it.

![EarthStick control map](assets/EarthStick_controls.svg)

## Two related programs

The repository now contains two intentionally separate operating choices.

### 1. Standalone EarthStick v0.5

**EarthStick v0.5** is the tested and accepted standalone flight-control baseline, accepted 2026-10-25.

Download:

- [`releases/EarthStick_v0.5.zip`](releases/EarthStick_v0.5.zip)

The standalone release contains only:

- `EarthStick.py`
- `EarthStick.bat`

No third-party Python packages are required by standalone EarthStick v0.5.

### 2. PRAVE/ME + EarthStick v0.2.0 TEST

The second program integrates the existing PRAVE/ME GPS/vehicle tracker with an **unchanged EarthStick v0.5 flight core**.

Current live-tested package name:

`PRAVE_ME_FLY_v0.2_TEST.zip`

Verified local package SHA-256:

`83df19a3319ac6497417affe947574f58fef1bcac715ac3bcabc161e1acb5531`

The exact tested binary package is intentionally not linked from the GitHub release folder until its uploaded bytes can be verified against that checksum. The repository documentation below records the current v0.2.0 TEST behavior and test state.

The integrated program adds two deliberate camera states:

- **ME** - fresh GPS/PRAVE position owns camera recentering
- **FLY** - EarthStick v0.5 owns the camera and GPS is not required

The T.A320 **Button 1 index-finger / gun-style trigger** toggles between them.

> **ME finds you. FLY lets you leave.**

In FLY mode, Button 1 acts like a map-camera Return-to-Home request: if a fresh ME/GPS position exists, it returns the camera to the current ME position and resumes tracking. If GPS is stale or missing, the return is blocked and FLY remains available.

The original `T` key remains as a fallback ME/FLY toggle.

## Current test status

### Standalone EarthStick v0.5

**Accepted.** Live-tested in ArcGIS Earth and demonstrated in a recorded flight.

### PRAVE/ME + EarthStick v0.2.0 TEST

**Test build. Partially live-verified on 2026-10-25.**

Verified with the T.A320 connected, ArcGIS Earth Automation API connected, and **no GPS/serial device available at all** (`COM12` absent):

- EarthStick v0.5 controller detection remained operational
- ArcGIS Earth API remained connected
- PRAVE/ME serial reconnect attempts continued independently
- FLY remained usable despite total GPS/serial failure
- Button 1 toggled between the ME state and joystick-enabled FLY state
- the missing GPS subsystem did not take down flight control

Still pending live acceptance testing:

- fresh-GPS ME recentering in the integrated build
- FLY -> Button 1 -> immediate RTH to current ME
- GPS loss after a valid fix followed by deliberate return after GPS recovery

Software self-tests cover the preserved parsers, 30 Hz flight rate, 20x speed math, neutral hover, zoom buttons, Button 1 edge-toggle logic, stale-GPS RTH rejection, and no automatic return when GPS recovers.

## Standalone EarthStick controls

| Physical control | EarthStick v0.5 action |
|---|---|
| Stick forward / back | Fly forward / reverse |
| Stick left / right | Strafe left / right |
| Stick twist / RZ | Change heading |
| Slider 0 / throttle | Movement speed |
| POV hat up / down | Camera tilt |
| Red top button - Button 4 | Hold to zoom in / descend |
| Black thumb button - Button 3 | Hold to zoom out / climb |
| Neutral controls | Stop and hover in place |

Everything else is intentionally left unassigned in standalone v0.5.

### Integrated PRAVE/ME control addition

| Physical control | PRAVE/ME + EarthStick v0.2 TEST action |
|---|---|
| Index-finger / gun-style trigger - Button 1 | Toggle **ME <-> FLY** / deliberate RTH request |
| Button 4 | Same v0.5 zoom in |
| Button 3 | Same v0.5 zoom out |
| All flight axes | Same accepted EarthStick v0.5 behavior while in FLY |

Button 1 remains unused by standalone EarthStick v0.5.

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

The PRAVE/ME integration adds a second operational idea: use GPS to establish or recover the operator's real position, then deliberately leave that position and fly the ArcGIS Earth camera anywhere without GPS constraining the view.

## Requirements

### Standalone EarthStick v0.5

- Windows 10 or Windows 11
- ArcGIS Earth desktop
- ArcGIS Earth Automation API enabled
- Python 3
- Thrustmaster TCA Sidestick Airbus Edition connected by USB
- Thrustmaster driver/control panel recommended

EarthStick was developed and field-tested with the controller appearing in Windows as **T.A320 Pilot**. Some Windows installations expose the underlying WinMM device using the generic name `Microsoft PC-joystick driver`; v0.5 includes a capability-based fallback for this case.

### PRAVE/ME + EarthStick v0.2 TEST

Adds the existing PRAVE/ME requirements:

- `pyserial`
- configured PRAVE/RMC serial input when ME/GPS tracking is desired
- existing PRAVE icon path/configuration

The default preserved PRAVE configuration in the test package is:

- `COM12`
- `19200` baud
- `C:\MyData\PRAVE_ME\Icons`
- ArcGIS Earth API `http://localhost:8000`

A missing GPS/serial port does **not** prevent FLY operation when the joystick is available.

## Quick start - standalone

1. Install the Thrustmaster driver package and connect the sidestick directly to the PC.
2. Press `Win + R`, run `joy.cpl`, select the T.A320 controller, and verify X/Y, rudder/twist, throttle, POV, and buttons respond.
3. Open ArcGIS Earth.
4. In ArcGIS Earth settings, enable **Automation API** under **Advanced**.
5. Leave the default Automation API address at `http://localhost:8000` unless you intentionally changed it.
6. Extract `EarthStick_v0.5.zip`.
7. Double-click `EarthStick.bat`.
8. Wait for the console to report `ArcGIS Earth: connected`.
9. Fly.

## Quick start - PRAVE/ME + EarthStick

1. Configure the preserved PRAVE/ME core for the correct serial port and icon path if your system differs from the current defaults.
2. Open ArcGIS Earth and enable its Automation API.
3. Connect the T.A320 if FLY mode is desired.
4. Run `Run_SELF_TEST.bat` once after extraction.
5. Run `Run_PRAVE_ME_FLY.bat`.
6. Confirm the console reports the EarthStick v0.5 controller when present.
7. In **ME**, valid GPS may recenter the camera.
8. Squeeze Button 1 firmly once to enter **FLY**.
9. Fly with the unchanged EarthStick v0.5 controls.
10. With a fresh GPS fix available, squeeze Button 1 again to request return to **ME**.

See [`docs/PRAVE_ME_FLY.md`](docs/PRAVE_ME_FLY.md) for the integrated operating model and test state.

Detailed standalone setup remains in [`docs/USER_GUIDE.md`](docs/USER_GUIDE.md), the printable [`docs/EarthStick_User_Guide.pdf`](docs/EarthStick_User_Guide.pdf), and [`docs/TROUBLESHOOTING.md`](docs/TROUBLESHOOTING.md).

## Architecture at a glance

### Standalone

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

### Integrated PRAVE/ME + EarthStick

```text
PRAVE/RMC serial thread ---------> latest valid ME position
          |                                  |
          |                                  v
          |                         ME / FLY coordinator
          |                                  ^
          v                                  |
PRAVE/ME drawings/logging          EarthStick v0.5 controls
                                             |
                                             v
                                  ONE ArcGIS Earth camera writer
                                             |
                                             v
                                      ArcGIS Earth camera
```

The integration deliberately prevents PRAVE/ME and EarthStick from independently writing competing camera commands.

## Design principles

EarthStick is intentionally small.

- Do not assign buttons just because buttons exist.
- Preserve neutral/hover behavior.
- Keep movement controls independent and predictable.
- Prefer direct camera control over mouse/keyboard emulation.
- Avoid external Python dependencies in standalone EarthStick when Windows standard interfaces already provide what is needed.
- Change one behavior at a time and test it in ArcGIS Earth before adding another.
- Keep standalone EarthStick usable independently of PRAVE/ME.
- GPS failure must not disable FLY.
- GPS recovery must not automatically yank the camera home.

## Repository map

- `EarthStick.py` - tested standalone v0.5 controller bridge
- `EarthStick.bat` - standalone Windows launcher
- `releases/EarthStick_v0.5.zip` - packaged tested standalone release
- `assets/EarthStick_controls.svg` - scalable standalone control pictogram
- `assets/EarthStick_YouTube_Thumbnail.gif` - prepared comparison thumbnail
- `docs/USER_GUIDE.md` - standalone setup and operating manual plus integration overview
- `docs/EarthStick_User_Guide.pdf` - printable standalone v0.5 user manual
- `docs/PRAVE_ME_FLY.md` - integrated ME/FLY operating model
- `docs/TECHNICAL_NOTES.md` - architecture, APIs, math, constants, integration design
- `docs/TROUBLESHOOTING.md` - failure modes and checks
- `docs/HARDWARE_MAP.md` - observed axes and button numbers, including Button 1 trigger
- `docs/FIELD_TEST.md` - standalone v0.5 first flight and integrated no-GPS test
- `docs/VIDEO_GUIDE.md` - video/demo guidance
- `docs/PROJECT_NOTES.md` - project origin and integration rationale
- `ACKNOWLEDGEMENTS.md` - technology/trademark notes
- `CHANGELOG.md` - standalone and integration version history
- `CONTINUITY.md` - exact project state and modification rules

## Safety and scope

EarthStick and PRAVE/ME + EarthStick are ArcGIS Earth camera-control/tracking utilities. They are **not** aircraft flight-control systems, certified navigation systems, dispatch systems, or safety-of-life products. Users remain responsible for validating maps, layers, imagery, GPS data, coordinates, serial feeds, and operational procedures.

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

**Standalone EarthStick v0.5 works and remains the accepted baseline.**

**PRAVE/ME + EarthStick v0.2.0 is a separate TEST integration.** Its no-GPS/serial-failure behavior has now been live-verified; the complete fresh-GPS ME -> FLY -> RTH -> ME cycle still requires live acceptance testing before that integration is called field-proven.
