# EarthStick 1.0 Troubleshooting

## EarthStick says no joystick is connected

- Confirm the TCA Sidestick is plugged directly into USB.
- Run `joy.cpl` and verify Windows sees the controller.
- Verify the axes and buttons respond in the Windows test panel.
- Reconnect the joystick and leave EarthStick running; it will retry detection.

## EarthStick is waiting for ArcGIS Earth

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

## Run the self-test

```text
python EarthStick.py --selftest
```

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
