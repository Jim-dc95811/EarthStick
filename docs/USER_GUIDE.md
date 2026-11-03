# EarthStick 1.3 User Guide

A printable copy of this guide is available as [EarthStick_User_Guide.pdf](EarthStick_User_Guide.pdf).

## Purpose

EarthStick gives a Thrustmaster TCA Sidestick Airbus Edition direct control of the ArcGIS Earth camera. The goal is free movement inside a functioning map: imagery, labels, roads, GIS layers, and offline content remain part of the environment while you fly the camera.

The defining behavior is **neutral = hover**. When the movement controls return to neutral, EarthStick stops moving the camera.

New in 1.3: **World Gates** - golden rings in the sky; fly through one and you arrive somewhere else on Earth (see *World Gates* below).

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

1. Download [`EarthStick_v1.3.zip`](../releases/EarthStick_v1.3.zip) and extract it. It contains a folder named `EarthStick_v1.3` holding `EarthStick.py`, `EarthStick.bat` and a `Gates` folder with the World Gates pack.
2. Open ArcGIS Earth first, with the Automation API enabled.
3. Open the `EarthStick_v1.3` folder and double-click `EarthStick.bat`. A console window titled **EarthStick 1.3** opens.
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

![The red crosshair in the middle of the ArcGIS Earth window, beside a camera object over the SR-200 / I-95 interchange](../images/earthstick_trigger_click_crosshair.jpg)

*The red crosshair (right) and a camera object (left). Fly until the camera sits under the crosshair, hover, then pull the trigger.*

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

## World Gates: flying through wormholes

![Eight golden World Gates around Atlanta's airport](../images/world_gates_atl_hub_arcgis_earth.jpg)

*The Atlanta hub: eight gates in a circle around Hartsfield-Jackson, all at the same height.*

A gate is a golden ring floating in the sky. Fly through it and EarthStick moves you to its destination in an instant. You arrive still flying, facing the landmark.

### Fly your first trip

1. Open the **World Gates** file in ArcGIS Earth: drag `Gates\World_Gates_JAX_ATL.kmz` (in the EarthStick folder) onto the map, so you can see the rings.
2. Start EarthStick. The console lists the gates it armed: `Wormholes: 16 gate(s) armed: ATL, JAX, NYC, ...`
3. Fly to a ring, line up on its **gold** side (from the red side nothing happens), match the altitude shown under its name using **eye alt** at the bottom of ArcGIS Earth, and fly through the middle.
4. The view jumps to the destination and the console says `Wormhole: through the ... gate.` You arrive still flying, already facing the landmark.

### The World Gates pack (included)

- **Jacksonville:** one gate, **ATL**, over Jacksonville International (eye alt 1,500 ft), facing north-west toward Atlanta.
- **Atlanta hub:** you arrive in the middle of a 3 km circle of eight gates around Hartsfield-Jackson, all at eye alt 2,530 ft (1,500 ft above the airport). Turn and pick: NYC (north-west), London (north), Paris (north-east), Rome (east), JAX - home (south-east), Rio (south), Sydney (south-west), Tokyo (west).
- **Destinations:** you arrive about 600 m from the Statue of Liberty, Tower Bridge, the Eiffel Tower, the Colosseum, Tokyo Tower, the Sydney Opera House or Christ the Redeemer, facing it. The **ATL** gate behind you takes you back to the hub to connect home or onward.

![Approaching the Paris gate](../images/world_gates_paris_ring_arcgis_earth.jpg)

*Each gate's name sits beside its own ring, with the eye alt to fly at underneath.*

### Rules of the gates

- **Gold side only.** Each ring has a gold front and a red back. Fly in from the gold side; from the red side, from below, from above or beside it, nothing happens.
- **Match the altitude.** The number under each name is the **eye alt** (shown at the bottom of ArcGIS Earth, measured from sea level) of the ring's centre. Rings are 450 m (about 1,500 ft) across, so within a few hundred feet is fine.
- **Keep moving.** A gate fires while the joystick is moving the camera. Hovering or moving the map with the mouse does not trigger it.
- **One trip per pass.** After a jump, gates rest for 2 seconds.
- **Any speed works.** EarthStick checks the whole path between its updates, so even a fast pass cannot skip through a ring.

### Turning gates on and off

EarthStick reads the gate files in the **Gates** folder beside `EarthStick.py` **when it starts**. ArcGIS Earth cannot tell EarthStick which layers are switched on, so the folder is the switch:

- **On:** put a gate file (`.kmz`) in the Gates folder, open the same file in ArcGIS Earth so you can see the rings, and restart EarthStick.
- **Off:** move the file out of the Gates folder and restart EarthStick. With an empty or missing Gates folder, EarthStick flies exactly as 1.2.
- After adding or removing a gate file, always **restart EarthStick** - it only reads the folder at startup.

Several gate files can be used at once. A gate's partner is looked up in its own file first, so two files may reuse names such as ATL or JAX.

### Making your own gates

Gate files are ordinary KMZ files with the ring drawn in gold and the gate details stored inside. For now they are made with the `make_gate_kmz.py` script in the [ArcGIS Earth Unlocked toolbox](https://github.com/Jim-dc95811/ArcGIS-Earth-Unlocked/tree/main/tools) (for advanced users); a simpler way to make gates is planned. A gate can lead to a partner gate (a two-way route) or to a fixed spot with no way back (a one-way "trap door" - fly home the long way).

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
