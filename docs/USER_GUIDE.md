# EarthStick 1.0 User Guide

## Purpose

EarthStick gives a Thrustmaster TCA Sidestick Airbus Edition direct control of the ArcGIS Earth camera. The goal is free movement inside a functioning map: imagery, labels, roads, GIS layers, and offline content remain part of the environment while you fly the camera.

The defining behavior is **neutral = hover**. When the movement controls return to neutral, EarthStick stops moving the camera.

## Requirements

- Windows 11
- ArcGIS Earth desktop
- ArcGIS Earth Automation API enabled
- Python 3.x; tested with Python 3.14.5
- Thrustmaster TCA Sidestick Airbus Edition connected by USB
- Thrustmaster driver/control panel recommended
- `EarthStick.py` and `EarthStick.bat` in the same folder

No third-party Python packages are required.

## Controller check

Before running EarthStick:

1. Press `Win + R`.
2. Run `joy.cpl`.
3. Select the T.A320 controller.
4. Confirm the stick X/Y axes move and return to center.
5. Confirm twist/rudder responds.
6. Confirm Slider 0 travels through its range.
7. Confirm POV up/down responds.
8. Confirm Button 4 and Button 3 respond.

The tested controller normally appears as `T.A320 Pilot`.

## ArcGIS Earth setup

1. Open ArcGIS Earth desktop.
2. Open Settings.
3. Under Advanced, enable **Automation API**.
4. Use the default local API address `http://localhost:8000`.

## Start EarthStick

1. Extract `EarthStick_v1.0.zip`.
2. Double-click `EarthStick.bat`.
3. EarthStick reports the detected joystick and Slider 0 source.
4. Wait for `ArcGIS Earth: connected`.
5. Return the stick to neutral before beginning.

## Controls

| Control | Action |
|---|---|
| Stick forward | Fly forward |
| Stick back | Reverse |
| Stick left/right | Strafe left/right |
| Twist/RZ | Change heading |
| Slider 0 | Travel speed |
| POV up/down | Camera tilt |
| Red Button 4 | Hold to descend / zoom in |
| Black Button 3 | Hold to climb / zoom out |
| Neutral | Stop and hover |

## Flying technique

For precise inspection, lower the throttle, approach the target, release the stick, and hover. Use strafe and twist independently to inspect the target from different positions without being forced into forward motion.

For long-distance movement, climb to a high altitude and increase the throttle. The maximum travel rate scales with altitude. Descend again when you reach the destination.

## Using the mouse while EarthStick is running

When the joystick is idle, EarthStick periodically re-reads the ArcGIS Earth camera. You can reposition the map with normal ArcGIS Earth controls, then return to the joystick. When movement begins, EarthStick synchronizes from the current camera state.

## Automatic recovery

### ArcGIS Earth API interruption

If the Automation API disappears, EarthStick stops writing camera movement and waits. It does not keep advancing a hidden local camera. When the API returns, EarthStick reads the live camera again before flight resumes.

### Joystick disconnect

If the sidestick is unplugged, EarthStick remains running and waits for it to return. Reconnect the joystick. EarthStick re-detects it, even if Windows assigns a different joystick ID, then reads the live ArcGIS Earth camera before movement resumes.

## Stop EarthStick

Press `Ctrl+C` in the EarthStick console or close the console window.

## Self-test

From a command prompt in the EarthStick folder:

```text
python EarthStick.py --selftest
```

A successful run prints:

```text
EarthStick self-test PASS
```

## Important scope note

EarthStick moves the ArcGIS Earth **map camera**. It is not an aircraft controller or certified navigation system. Always validate the underlying map, imagery, GIS layers, coordinates, and offline packages for the intended use.
