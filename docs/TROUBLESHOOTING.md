# EarthStick Troubleshooting

## Start here: separate hardware from EarthStick

Before changing EarthStick, run `joy.cpl` and verify the T.A320 controller itself responds correctly.

If the controller fails in the Thrustmaster/Windows control panel, EarthStick cannot repair that problem.

## EarthStick says no joystick is connected

Check:

1. TCA Sidestick USB cable is connected directly to the PC.
2. Windows Device Manager shows the controller.
3. `joy.cpl` lists `T.A320 Pilot` or the appropriate TCA device.
4. The controller works in its Properties/Test Input screen.
5. Restart EarthStick after reconnecting the controller.

## EarthStick says T.A320 Pilot was not found uniquely

The WinMM API may report a generic device name even though `joy.cpl` reports `T.A320 Pilot`.

v0.5 includes a fallback for one unique attached controller with at least four axes, 17 buttons, and POV support.

If more than one connected controller matches that profile, EarthStick refuses to guess. Disconnect unrelated game controllers and retry.

## Slider0 cannot be identified

EarthStick v0.5 expects one throttle-like WinMM axis among Z, U, or V.

If it reports that Slider0 cannot be identified uniquely:

1. verify the throttle moves in the Thrustmaster control panel
2. close other controller remapping software
3. disconnect unrelated controllers
4. restart the TCA Sidestick and EarthStick

Do not change the axis mapping in code until the actual Windows mapping is established.

## EarthStick waits forever for ArcGIS Earth

Expected line:

`Waiting for ArcGIS Earth Automation API at http://localhost:8000 ...`

Check:

1. ArcGIS Earth desktop is open.
2. Settings -> Advanced -> Enable Automation API is ON.
3. The API base URL is still the default `http://localhost:8000`.
4. Try the ArcGIS Earth Swagger page: `http://localhost:8000/swagger/index.html`.
5. If you intentionally changed ArcGIS Earth's API port, EarthStick v0.5 will not automatically discover it; `BASE_URL` is currently fixed in code.

## Connected, but the camera does not move

Check the EarthStick console status line.

Move one control at a time:

- X should change for left/right stick
- Y should change for forward/back
- RZ should change for twist
- THR should change for the throttle slider
- POV up/down should change tilt in Earth

If X/Y/RZ/THR do not change, return to `joy.cpl`.

## Throttle changes in joy.cpl but not in EarthStick

v0.3 specifically fixed this problem by detecting whether Slider0 is exposed through WinMM Z, U, or V.

The EarthStick startup console prints the detected Slider0 WinMM axis.

If THR still does not change from 0.00 to 1.00 across slider travel, capture the console and the Thrustmaster Test Input screen before modifying code.

## Movement is too fast or too slow

v0.5 uses the v0.4 20x translation-speed multiplier proven in live testing.

First use the throttle slider. Do not change constants until you establish whether the problem exists at low altitude, high altitude, or both, because top speed is altitude-aware.

## Camera drifts when controls are released

EarthStick has an 0.08 centered-axis dead zone.

If it drifts:

1. observe X, Y, and RZ in the EarthStick console while hands-off
2. verify the controller centers in the Thrustmaster control panel
3. recalibrate/repair the controller first if the hardware values do not center

Do not increase the dead zone unless the hardware test establishes a real center-noise problem.

## Button 4 / Button 3 zoom direction is backwards

Tested mapping:

- Button 4 red top button -> zoom in / descend
- Button 3 black thumb -> zoom out / climb

Confirm `joy.cpl` still reports those button numbers before changing EarthStick.

## Button 1 index trigger does not seem to work

During hardware mapping, the gun-style index-finger trigger appeared inactive until it was squeezed more firmly. A firm squeeze registered as **Button 1**.

Button 1 has no function in standalone EarthStick v0.5.

In PRAVE/ME + EarthStick v0.2 TEST it toggles ME/FLY and requests RTH from FLY.

## Mouse movement seems to be overwritten

Wait until EarthStick is idle, navigate with the mouse, then move the joystick again. EarthStick periodically re-syncs the camera while idle and re-syncs when joystick activity begins.

## Console says buttons are unused

This is a known stale cosmetic line in standalone v0.5. Buttons 3 and 4 are used for zoom. The tested behavior is authoritative; the string is documented and intentionally left unchanged until a future standalone version is explicitly approved.

## Python is not found

`EarthStick.bat` tries:

1. `py -3 EarthStick.py`
2. otherwise `python EarthStick.py`

Install Python 3 and ensure either the Python launcher (`py`) or `python` is available in PATH.

## Controller works but an emulator/remapper is also installed

During development, Windows showed other controller/emulator devices alongside the T.A320. EarthStick attempts to identify the T.A320, but multiple similar virtual devices can make identification ambiguous.

For troubleshooting, disable or disconnect unrelated controller emulators temporarily and retest.

---

# PRAVE/ME + EarthStick v0.2 TEST Troubleshooting

## `COM12` not found / GPS is completely absent

This does **not** have to stop FLY.

A live 2026-10-25 test intentionally ran with `COM12` absent and produced repeated messages similar to:

`ERROR could not open port 'COM12'`

`RECONNECT waiting 5.0 seconds`

At the same time:

- the EarthStick v0.5 controller remained detected
- ArcGIS Earth API remained connected
- Button 1 could switch into FLY
- joystick flight remained operational

So if the serial/GPS subsystem fails but the T.A320 and ArcGIS Earth API are healthy, use FLY as designed.

## Button 1 from FLY will not return to ME

This is expected when no **fresh** accepted GPS position exists.

The integrated v0.2 TEST build requires the latest accepted RMC to be no more than 5 seconds old for Button 1 RTH.

If GPS is missing or stale:

- the RTH request is blocked
- camera position is not changed
- mode remains FLY

Do not modify the code to force an old cached position unless that behavior is deliberately redesigned and versioned later.

## GPS came back but the camera did not jump home

Expected behavior.

GPS recovery deliberately does **not** auto-recenter while in FLY. This prevents the camera from being yanked away from an inspection location simply because the receiver recovered.

After a fresh GPS fix is available, deliberately squeeze Button 1 again to request ME/RTH.

## No joystick detected in the integrated program

PRAVE/ME is designed to remain useful without EarthStick. If the T.A320 is absent, flight is unavailable but PRAVE/ME should continue operating.

Use the existing keyboard `T` fallback for ME tracking control if needed.

## Integrated flight feels slow/choppy

The coordinator was specifically designed so the PRAVE serial `readline()` timing cannot throttle the accepted EarthStick 30 Hz camera loop.

If flight becomes slow/choppy:

1. verify the console reports EarthStick v0.5 detected
2. verify ArcGIS Earth API is responsive
3. distinguish camera/API delay from serial reconnect messages
4. do not combine the serial loop and flight loop into one blocking loop

Any code change to this architecture requires a new integration version.
