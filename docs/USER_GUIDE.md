# EarthStick 1.2 User Guide

A printable copy of this guide is available as [EarthStick_User_Guide.pdf](EarthStick_User_Guide.pdf).

## Purpose

EarthStick gives a Thrustmaster TCA Sidestick Airbus Edition direct control of the ArcGIS Earth camera. The goal is free movement inside a functioning map: imagery, labels, roads, GIS layers, and offline content remain part of the environment while you fly the camera.

The defining behavior is **neutral = hover**. When the movement controls return to neutral, EarthStick stops moving the camera.

New in 1.2: **trigger-click**. A red crosshair sits in the middle of the ArcGIS Earth window. Put an object under it and pull the trigger to open the object's information box (popup) without touching the mouse.

## Requirements

- Windows 11
- ArcGIS Earth desktop
- ArcGIS Earth Automation API enabled
- Python 3 from python.org; tested with Python 3.14.5 (the standard install includes Tkinter, which draws the crosshair)
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
8. Confirm Button 4, Button 3 and the trigger (Button 1) respond.

The tested controller normally appears as `T.A320 Pilot`.

## ArcGIS Earth setup

1. Open ArcGIS Earth desktop.
2. Open Settings.
3. Under Advanced, enable **Automation API**.
4. Use the default local API address `http://localhost:8000`.

## Start EarthStick

1. Download [`EarthStick_v1.2.zip`](../releases/EarthStick_v1.2.zip) and extract it. It contains a folder named `EarthStick_v1.2` holding `EarthStick.py` and `EarthStick.bat`.
2. Open ArcGIS Earth first, with the Automation API enabled.
3. Open the `EarthStick_v1.2` folder and double-click `EarthStick.bat`. A console window titled **EarthStick 1.2** opens.
4. EarthStick reports the detected joystick and Slider 0 source. If the joystick is not plugged in, it says so and waits until it is.
5. It then shows `Waiting for ArcGIS Earth Automation API at http://localhost:8000 ...`. If ArcGIS Earth is not ready, `Still waiting:` lines explain why.
6. Wait for `ArcGIS Earth: connected`, followed by `Trigger-click: ready`. The red crosshair appears in the middle of the ArcGIS Earth window.
7. Return the stick to neutral before beginning.

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
| Trigger (Button 1) | Click the object under the red crosshair |
| Neutral | Stop and hover |

## Flying technique

For precise inspection, lower the throttle, approach the target, release the stick, and hover. Use strafe and twist independently to inspect the target from different positions without being forced into forward motion.

For long-distance movement, climb to a high altitude and increase the throttle. The maximum travel rate scales with altitude. Descend again when you reach the destination.

## Trigger-click: opening and closing information boxes

1. Fly until the object (a beacon, a camera, a parcel, a point) sits under the red crosshair.
2. Let go of the stick so the camera hovers.
3. Pull the trigger once. EarthStick moves the Windows mouse pointer onto the object, clicks it, and puts the pointer back where it was. The object's information box opens.
4. **To close the box,** aim the crosshair at open map, away from the box, and pull the trigger again.

Tips:

- One pull = one click. A second pull within 0.8 seconds is ignored, so a bouncy trigger can never turn into a double-click (a double-click makes ArcGIS Earth zoom in).
- If another window is in front, the first click brings ArcGIS Earth to the front and EarthStick then clicks the object.
- The crosshair follows the ArcGIS Earth window if you move or resize it, and hides while ArcGIS Earth is minimized. Mouse clicks pass straight through it.
- If the crosshair cannot be shown, the console says `Trigger-click: unavailable` and EarthStick flies normally.
- If the crosshair sits off the true centre on your screen, the `CENTER_OFFSET_X` / `CENTER_OFFSET_Y` settings near the top of `EarthStick.py` nudge it by screen pixels.

## Using the mouse while EarthStick is running

When the joystick is idle, EarthStick periodically re-reads the ArcGIS Earth camera. You can reposition the map with normal ArcGIS Earth controls, then return to the joystick. When movement begins, EarthStick synchronizes from the current camera state.

## Automatic recovery

### ArcGIS Earth API interruption

If the Automation API disappears, EarthStick stops writing camera movement and waits. It does not keep advancing a hidden local camera. When the API returns, EarthStick reads the live camera again before flight resumes.

### Joystick disconnect

If the sidestick is unplugged, EarthStick remains running and waits for it to return. Reconnect the joystick. EarthStick re-detects it, even if Windows assigns a different joystick ID, then reads the live ArcGIS Earth camera before movement resumes.

## Stop EarthStick

Press `Ctrl+C` in the EarthStick console or close the console window. After `Ctrl+C` the console shows `Stopped.` and waits for a key press before closing.

## Self-test

From a command prompt in the EarthStick folder:

```text
py -3 EarthStick.py --selftest
```

(If the `py` launcher is not installed, use `python` instead of `py -3`.) The self-test needs no joystick and no ArcGIS Earth.

A successful run prints:

```text
EarthStick self-test PASS
```

## Important scope note

EarthStick moves the ArcGIS Earth **map camera**. It is not an aircraft controller or certified navigation system. Always validate the underlying map, imagery, GIS layers, coordinates, and offline packages for the intended use.
