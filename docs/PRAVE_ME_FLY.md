# PRAVE/ME + EarthStick v0.2.0 TEST

## Purpose

This integration combines the existing PRAVE/ME tracker with the accepted standalone EarthStick v0.5 flight controls while preserving both cores.

The goal is not to make EarthStick dependent on PRAVE/ME. Standalone EarthStick remains its own program.

The integrated program provides a second choice for operators who want both:

- real-position ME/GPS recentering
- free helicopter-style ArcGIS Earth camera flight

## Core operating idea

The integrated program has two explicit camera states:

### ME

- fresh accepted RMC updates the ME position
- PRAVE/ME may recenter the ArcGIS Earth camera on ME
- EarthStick movement/zoom commands are suppressed
- current camera altitude, heading, tilt and roll are preserved by the PRAVE/ME recenter behavior

### FLY

- EarthStick v0.5 owns the ArcGIS Earth camera
- GPS is not required
- neutral controls = hover
- X/Y, twist, throttle, POV tilt, Button 4 zoom-in and Button 3 zoom-out retain the accepted v0.5 behavior
- PRAVE vehicle reception, drawings and logging can continue
- fresh ME/GPS position is remembered only for a future deliberate return

A useful shorthand is:

> **ME finds you. FLY lets you leave.**

## Trigger control

The T.A320 **Button 1 index-finger / gun-style trigger** is the physical ME/FLY control in this integration.

The button required a firmer squeeze than expected during the initial Windows `joy.cpl` mapping test.

Behavior:

- **ME -> Button 1 -> FLY**: stop ME recentering and begin free camera flight from the current camera location
- **FLY -> Button 1 -> ME**: request return to the current ME position if a fresh GPS fix exists

The toggle is edge-triggered. Holding the trigger does not repeatedly change modes.

The keyboard `T` key remains available as a fallback toggle.

## Return-to-ME / RTH behavior

Button 1 from FLY is intentionally similar to a drone Return-to-Home control, but the "home" position is the current valid ME/GPS position rather than a launch point stored indefinitely.

Fresh GPS is defined by this test build as an accepted RMC position received within the last **5 seconds**.

If the GPS is stale or missing:

- the return request is blocked
- the camera is not moved
- the program remains in FLY

The integration does not blindly return to an old cached coordinate.

## GPS failure rule

**FLY must never depend on GPS.**

If GPS or the entire serial input fails while in FLY:

- joystick flight continues
- hover continues
- heading/strafe/forward motion continue
- throttle continues
- POV tilt continues
- Button 4 zoom-in continues
- Button 3 zoom-out continues

If GPS later recovers, the camera is **not** automatically pulled back to ME. The operator must deliberately press Button 1 again.

This keeps a GPS failure from cascading into a camera-control failure.

## Single camera owner

The main engineering purpose of the coordinator is to stop two independent Python programs from issuing conflicting camera commands.

The preserved PRAVE serial/core logic and the preserved EarthStick v0.5 flight logic both feed one coordinator.

```text
PRAVE/RMC serial thread -----> latest ME position
          |                           |
          |                           v
          |                  ME / FLY coordinator
          |                           ^
          v                           |
PRAVE drawings/logging         EarthStick v0.5 input
                                      |
                                      v
                           ONE ArcGIS Earth camera writer
                                      |
                                      v
                               ArcGIS Earth
```

In ME, the coordinator performs PRAVE/ME recenter requests.

In FLY, the coordinator performs EarthStick v0.5 camera updates at the accepted 30 Hz rate.

## Preserved cores

The v0.2.0 TEST package contains:

- `AE_PRAVE_LIVE_v0_1_0_TEST.py` - preserved PRAVE/ME core
- `EarthStick.py` - exact accepted EarthStick v0.5 core
- `PRAVE_ME_FLY_v0_2.py` - coordinator / single camera owner
- `Run_PRAVE_ME_FLY.bat` - normal launcher
- `Run_SELF_TEST.bat` - parser/control/integration self-test
- `README.txt` - package instructions

Standalone EarthStick v0.5 remains unchanged in the repository root and standalone release ZIP.

## PRAVE configuration preserved

Current defaults in the preserved PRAVE core:

- serial input: `COM12`
- baud: `19200`
- icons: `C:\MyData\PRAVE_ME\Icons`
- ArcGIS Earth API: `http://localhost:8000`

The integrated program preserves the existing PRAVE dependency on `pyserial`.

## Live test - no GPS at all

Date: **2026-10-25**

Test condition:

- T.A320 connected
- EarthStick v0.5 detected
- ArcGIS Earth Automation API connected
- `COM12` did not exist
- therefore no GPS/RMC source existed at all

Observed console behavior:

- `EARTHSTICK_CONNECTED version=0.5`
- `MODE -> ME (startup)`
- `ARCGIS_EARTH_API_CONNECTED`
- serial open failure for `COM12`
- `RECONNECT waiting 5.0 seconds`
- repeated serial reconnect attempts while the rest of the program stayed alive

Operational result:

- FLY remained usable
- Button 1 toggled the joystick-enabled FLY state on/off through ME/FLY mode changes
- complete GPS/serial failure did not disable EarthStick

This live test verifies the failure-isolation architecture.

## What is not yet live-accepted

As of this documentation update, the following still require a live GPS/RMC test:

1. startup in ME with fresh GPS and normal recentering
2. Button 1 ME -> FLY while GPS is present
3. Button 1 FLY -> ME with immediate return to current ME
4. GPS loss while flying after a previously valid fix
5. blocked RTH while stale
6. GPS recovery without automatic camera return
7. deliberate Button 1 return after recovery

Software self-tests already cover the state-machine logic, but these items are not to be called field-proven until physically tested.

## No joystick connected

If the T.A320 is not detected at startup, PRAVE/ME remains available. EarthStick flight is simply unavailable.

The integrated design therefore fails independently in either direction:

- no GPS -> FLY can still work
- no joystick -> PRAVE/ME can still work

## Safety and scope

This is a map-camera workflow, not an aircraft/drone flight-control system and not a certified navigation or safety-of-life system. The RTH analogy describes camera behavior only.
