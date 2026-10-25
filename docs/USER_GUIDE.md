# EarthStick v0.5 User Guide

## 1. Purpose

EarthStick gives ArcGIS Earth desktop a helicopter-style joystick navigation model using the Thrustmaster TCA Sidestick Airbus Edition.

The central behavior is:

> When you release the controls, the camera stops and hovers in place.

You do not need to keep correcting the camera to remain stationary.

Standalone EarthStick v0.5 remains the accepted baseline. A separate PRAVE/ME + EarthStick v0.2 TEST integration is documented later in this guide.

## 2. What you need - standalone EarthStick

- Windows 10 or Windows 11 PC
- ArcGIS Earth desktop
- Python 3
- Thrustmaster TCA Sidestick Airbus Edition
- Thrustmaster driver/control panel recommended
- `EarthStick.py` and `EarthStick.bat` in the same folder

No pip install is required for standalone EarthStick. It uses Python's standard library and Windows joystick services already present in the operating system.

## 3. Install and test the joystick

### 3.1 Install the Thrustmaster driver

Install the current Thrustmaster driver package for the TCA Sidestick Airbus Edition, then connect the controller directly to the PC by USB.

The tested Windows controller name was:

`T.A320 Pilot`

### 3.2 Verify Windows sees the controller

1. Press `Win + R`.
2. Type `joy.cpl`.
3. Press Enter.
4. Select the T.A320 controller.
5. Click **Properties**.

Verify:

- X axis reaches left and right limits
- Y axis reaches forward and back limits
- RZ/Rudder responds to stick twist
- Slider 0 responds to the throttle lever
- POV hat responds in all directions
- red top button reports Button 4
- black thumb button reports Button 3
- index-finger / gun-style trigger reports Button 1 when squeezed firmly

Button 1 is not used by standalone EarthStick v0.5. It is used by the separate PRAVE/ME integration.

If those tests fail in `joy.cpl`, fix the joystick/driver problem before troubleshooting EarthStick.

## 4. Enable ArcGIS Earth Automation API

1. Open ArcGIS Earth desktop.
2. Open **Settings**.
3. Open **Advanced**.
4. Enable **Automation API**.

The default API address used by EarthStick is:

`http://localhost:8000`

EarthStick waits for ArcGIS Earth at startup, so ArcGIS Earth should be open and the Automation API should be enabled before you run EarthStick.

## 5. Start standalone EarthStick

1. Extract `EarthStick_v0.5.zip` to a normal writable folder.
2. Keep `EarthStick.py` and `EarthStick.bat` together.
3. Double-click `EarthStick.bat`.

The console should identify the joystick, identify the Slider0 source, wait for ArcGIS Earth, and then report:

`ArcGIS Earth: connected`

Leave the EarthStick console open while flying.

To stop EarthStick, close its console window or press `Ctrl+C`.

## 6. Standalone controls

![EarthStick control map](../assets/EarthStick_controls.svg)

### Stick forward / back

Moves the camera forward or backward in the direction of the current heading.

### Stick left / right

Strafes the camera left or right without changing heading.

### Stick twist

Changes camera heading.

Twist right to turn right. Twist left to turn left.

### Throttle / Slider 0

Controls translation speed.

The speed curve is deliberately nonlinear so the low end provides fine control while the high end provides rapid travel.

The available top speed also increases with camera altitude.

### POV hat up / down

Changes camera tilt.

Left/right POV directions are not assigned in v0.5.

### Red top button - Button 4

Hold to zoom in by lowering camera altitude.

Release to stop changing altitude.

### Black thumb button - Button 3

Hold to zoom out by raising camera altitude.

Release to stop changing altitude.

### Neutral

Release the stick, twist, POV, and zoom buttons and EarthStick stops commanding motion.

The camera remains where it is: the default condition is hover.

## 7. Flying technique

### Close inspection

- Reduce the throttle.
- Use small stick movements.
- Twist to line up with roads or features.
- Use POV tilt to establish the viewing angle.
- Release the controls whenever you want to inspect one location without drift.

### Cross-area travel

- Zoom out / climb.
- Increase throttle.
- Fly toward the target area.
- Reduce throttle before descending.
- Zoom in / descend for local inspection.

Because maximum translation speed scales with altitude, climbing also makes wide-area travel faster.

## 8. Using the mouse while EarthStick is running

EarthStick periodically re-synchronizes with the current ArcGIS Earth camera while idle. When you begin moving the joystick again, it re-reads the camera so ordinary mouse navigation performed while EarthStick is idle is respected.

This lets you move between mouse and joystick operation without restarting EarthStick.

## 9. Console status

While running, EarthStick prints a live status line similar to:

`FLY X +0.22 Y +0.73 RZ -0.12 THR 0.80 SPD 1234.5 m/s HDG 212.0 TILT 52.0`

Fields:

- `X` - strafe command
- `Y` - forward/back command
- `RZ` - twist/heading command
- `THR` - normalized throttle position from 0.00 to 1.00
- `SPD` - calculated translation speed in meters per second
- `HDG` - current heading
- `TILT` - current camera tilt

`IDLE` means no movement/tilt/zoom control is currently active. `FLY` means at least one active control is being applied.

## 10. Known cosmetic messages in standalone v0.5

The tested v0.5 code contains two stale diagnostic strings from earlier test versions:

- startup text says buttons are intentionally unused even though Buttons 3 and 4 are used for zoom
- an unusual spatial-reference error still names EarthStick 0.3

These strings do not affect controller behavior. They are deliberately left unchanged in the v0.5 tested baseline. Any code edit requires a new version number under the project's continuity rules.

---

# PRAVE/ME + EarthStick v0.2.0 TEST

## 11. What the integration adds

The integrated test build combines the existing PRAVE/ME tracker with the accepted EarthStick v0.5 flight core.

It does not replace standalone EarthStick.

The package uses two modes:

- **ME** - PRAVE/ME may recenter the camera on fresh GPS
- **FLY** - EarthStick controls the camera freely and GPS is not required

## 12. Integration requirements

In addition to the EarthStick requirements:

- `pyserial`
- PRAVE/RMC serial source when ME tracking is desired
- valid PRAVE icon/configuration path

Current preserved defaults in the test package:

- `COM12`
- `19200` baud
- `C:\MyData\PRAVE_ME\Icons`
- `http://localhost:8000`

Change the PRAVE core configuration only if your installation requires it.

## 13. Start the integrated program

1. Extract `PRAVE_ME_FLY_v0.2_TEST.zip`.
2. Open ArcGIS Earth and enable the Automation API.
3. Connect the T.A320 if FLY is desired.
4. Run `Run_SELF_TEST.bat`.
5. Run `Run_PRAVE_ME_FLY.bat`.
6. Confirm the console reports EarthStick v0.5 detected when the joystick is present.
7. Confirm the console title/status shows the current ME/FLY mode.

The package contains the preserved PRAVE core and an exact EarthStick v0.5 snapshot plus the coordinator.

## 14. ME / FLY trigger

T.A320 Button 1 is the index-finger / gun-style trigger.

It may require a firm squeeze.

### From ME

Squeeze Button 1 once:

- ME recentering turns off
- mode becomes FLY
- EarthStick v0.5 camera control becomes active
- flight begins from the camera location where ME left you

GPS is not required to enter or remain in FLY.

### From FLY

Squeeze Button 1 once:

- if a fresh accepted GPS position exists, request return to ME and resume tracking
- if GPS is stale or missing, the request is blocked and the program stays in FLY

The keyboard `T` key remains as a fallback toggle.

## 15. RTH behavior

The trigger provides a map-camera equivalent of Return-to-Home:

1. ME establishes the real-world reference position.
2. Trigger to FLY.
3. Fly anywhere in the ArcGIS Earth environment.
4. If orientation is lost, trigger back to ME when fresh GPS is available.

The program does not use an old stale GPS coordinate as automatic home.

## 16. GPS failure

FLY is deliberately independent of GPS.

If GPS/serial disappears while flying:

- keep flying
- hover still works
- zoom still works
- throttle still works
- heading/tilt/strafe still work

If GPS recovers, the camera stays where you are. It does not jump home automatically.

Press Button 1 deliberately after recovery if you want to return to ME.

## 17. No joystick connected

The integrated program is also designed to preserve PRAVE/ME when EarthStick hardware is absent.

No T.A320 means no FLY control, but PRAVE/ME remains the useful GPS/vehicle tracker.

## 18. Current live-test state

Verified 2026-10-25 with no GPS/serial device at all (`COM12` absent):

- EarthStick v0.5 detected
- ArcGIS Earth API connected
- PRAVE serial reconnect kept retrying
- FLY still worked
- Button 1 toggled the joystick-enabled FLY state on/off

Still pending live GPS testing:

- actual ME recenter in the integrated coordinator
- Button 1 RTH from FLY to current ME
- stale/recovered GPS sequence after a valid fix

See [`PRAVE_ME_FLY.md`](PRAVE_ME_FLY.md) and [`FIELD_TEST.md`](FIELD_TEST.md) for the exact test record.

## 19. Troubleshooting

See [`TROUBLESHOOTING.md`](TROUBLESHOOTING.md).

## 20. Safety

EarthStick and PRAVE/ME + EarthStick control only the ArcGIS Earth map/camera workflow. They do not validate imagery age, GIS layer accuracy, GPS accuracy, operational data, or incident procedures and are not certified aviation or safety-of-life navigation systems.
