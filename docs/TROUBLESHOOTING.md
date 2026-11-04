# EarthStick 1.3.1 Troubleshooting

## EarthStick says no joystick is connected

- Confirm the TCA Sidestick is plugged directly into USB.
- Run `joy.cpl` and verify Windows sees the controller.
- Verify the axes and buttons respond in the Windows test panel.
- Reconnect the joystick and leave EarthStick running; it will retry detection. This works both at startup and during flight.

## EarthStick is waiting for ArcGIS Earth

EarthStick prints the reason under `Still waiting:`. `connection refused` usually means ArcGIS Earth is closed or the Automation API is off. An HTTP error such as `404` means another program is using port 8000.

- Open ArcGIS Earth desktop.
- Enable Automation API under Settings > Advanced.
- Confirm the local API address is `http://localhost:8000`.
- If ArcGIS Earth was restarted, leave EarthStick running; it will retry and re-synchronize automatically.

## Controls move in an unexpected direction

For the official tested TCA mapping:

- stick left = strafe left
- stick right = strafe right
- forward/back = forward/reverse
- twist changes heading in the accepted physical direction

First verify the controller itself in `joy.cpl`. Do not edit axis signs until the Windows input behavior is known.

## Travel is too slow

Increase Slider 0 and climb higher. Maximum travel speed scales with altitude.

## Travel is too sensitive near the target

Lower Slider 0. The squared throttle curve provides more resolution at low speeds.

## EarthStick temporarily stops responding after an API interruption

That is deliberate fault isolation. EarthStick pauses camera writes until it can read a fresh ArcGIS Earth camera again. The console reports reconnection when synchronization succeeds.

## Joystick was unplugged

Leave EarthStick running and reconnect it. EarthStick will retry discovery and then re-read the current ArcGIS Earth camera before movement resumes.

## Camera jumps after using the mouse

Release the joystick to neutral before using the mouse. EarthStick periodically synchronizes while idle and also re-reads the camera when movement begins.

## Trigger-click

- **No crosshair, and the console says `Trigger-click: unavailable`:** the reason follows in brackets. Flying still works. The usual cause is a Python install without Tkinter: rerun the python.org installer, choose **Modify**, and tick **tcl/tk and IDLE**.
- **No crosshair, but no error:** make sure ArcGIS Earth is open and not minimized. The crosshair hides while ArcGIS Earth is minimized.
- **The trigger zooms in instead of opening the box:** let go of the stick and hover before pulling the trigger, and pull it once. Check in `joy.cpl` that the trigger shows as Button 1.
- **The box will not close:** aim the crosshair at open map, away from the box, and pull the trigger. `Esc` on the keyboard or a normal mouse click outside the box also closes it.
- **The crosshair is not over the spot that gets clicked:** adjust `CENTER_OFFSET_X` / `CENTER_OFFSET_Y` near the top of `EarthStick.py` (screen pixels).

## World Gates

- **I fly through a ring and nothing happens:**
  - Check the console at startup for `Wormholes: N gate(s) armed`. If it says `none`, the gate file is not in the **Gates** folder beside `EarthStick.py`, or EarthStick was started before the file was put there - restart EarthStick.
  - Approach from the **gold** side; the red side is the back.
  - Match the altitude under the gate's name (eye alt). Too high or low and you pass over or under the centre area.
  - Keep the stick moving as you go through; a hovering camera does not trigger a gate.
- **I arrive somewhere unexpected:** look at which ring you actually went through - each name sits beside its own ring at the ring's centre height.
- **`Wormholes: skipped - ...`:** a gate in that file leads to a partner that is missing or ambiguous; the message names the file and gate.

## Run the self-test

From a command prompt in the EarthStick folder:

```text
py -3 EarthStick.py --selftest
```

(Use `python` instead of `py -3` if the `py` launcher is not installed.)

Expected result:

```text
EarthStick self-test PASS
```

## Python does not start from the BAT file

Open Command Prompt and run:

```text
py -3 --version
```

or:

```text
python --version
```

Install Python 3 if neither command works.

## One-click start and site beacons (1.3.1)

- **The launcher says it cannot find ArcGIS Earth:** right-click your normal ArcGIS Earth shortcut > **Properties**, copy the **Target** (ends in `.exe`), paste it as the only line of `ArcGIS_Earth_path.txt` in the EarthStick folder, and run it again. If ArcGIS Earth moves after an update, delete that file and it searches again.
- **The shortcut will not pin:** right-click it and choose **Show more options** first; **Pin to taskbar** is in that longer menu.
- **A site star opens its box but no beacon appears:** the beacon is drawn through the Automation API, so check that ArcGIS Earth's **Automation API** is on (Settings > Advanced) - EarthStick needs it too.
- **Too many beacons:** untick or delete them under **My Drawings** on the left of ArcGIS Earth.
- **Two gate packs at once (rings fire twice or the console lists 40+ gates):** keep only one `World_Gates_JAX_ATL_v*.kmz` in the `Gates` folder and restart EarthStick.
