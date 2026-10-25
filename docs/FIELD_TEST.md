# EarthStick Field Tests

## EarthStick v0.5 First Flight Test

Date: 2026-10-25

### Test objective

Determine whether the TCA Sidestick + EarthStick bridge produces a practical direct-control navigation model in ArcGIS Earth, rather than merely proving that the camera can be moved programmatically.

### Preconditions

Confirmed before the flight test:

- T.A320 Pilot visible in Windows/Thrustmaster control panel
- X/Y full travel and centering verified
- RZ/twist full travel and centering verified
- Slider0 full travel verified
- POV directions verified
- red top button confirmed as Button 4
- black thumb button confirmed as Button 3
- ArcGIS Earth Automation API connected
- v0.4 20x translation-speed increase accepted
- v0.5 altitude/zoom buttons added without changing the proven v0.4 movement controls

### Result

**Accepted.**

The recorded flight showed the controls combining into one continuous 3D navigation system:

- forward motion while changing heading
- lateral strafe without forced rotation
- independent tilt
- throttle-controlled travel speed
- close-in local maneuvering
- rapid climb/zoom-out to regional view
- descent/zoom-in
- immediate stop/hover when controls returned to neutral

### Key finding

The decisive behavior is not any single axis. It is the combination of independent axes with a neutral stationary state.

The operator can fly to a location, release the controls, and study the map without continued drift or correction.

This was described during acceptance as acting like a helicopter: stop and hover in place unless told to do otherwise.

### Comparison lesson

A 3Dconnexion SpaceMouse had previously been tested for the same ArcGIS Earth navigation goal. In this specific workflow it was judged a poor fit because the interaction felt like manipulating a scene rather than piloting through it.

EarthStick's direct axis-to-camera model produced the desired behavior immediately once the speed and altitude controls were tuned.

This comparison reflects this project's field testing and should not be presented as a universal evaluation of SpaceMouse products.

### Baseline decision

v0.5 is the accepted standalone behavior baseline. Do not change its control meanings, rates, dead zone, speed formula, or hover model without explicit discussion, a new version number, and another live ArcGIS Earth test.

---

## PRAVE/ME + EarthStick v0.2.0 TEST - No-GPS Failure Test

Date: 2026-10-25

### Test objective

Verify the most important integration failure rule before connecting a live GPS source:

> **A total GPS/serial failure must not disable EarthStick FLY control.**

### Test condition

- integrated `PRAVE_ME_FLY_v0_2.py` running
- T.A320 connected and detected as EarthStick v0.5 controller
- ArcGIS Earth Automation API connected
- no GPS input connected
- configured `COM12` did not exist

This was stronger than a weak or stale GPS test: the serial device itself was absent.

### Observed console state

The live console showed:

- `EARTHSTICK_CONNECTED version=0.5`
- `EarthStick: v0.5 controller detected`
- `MODE -> ME (startup)`
- `ARCGIS_EARTH_API_CONNECTED`
- repeated `ERROR could not open port 'COM12'`
- repeated `RECONNECT waiting 5.0 seconds`

Despite the serial failure, the program remained running and the joystick/API path remained alive.

### Operational result

**Passed for the no-GPS failure condition.**

- Button 1 index-finger trigger toggled between ME and FLY states.
- In this no-GPS condition, the trigger effectively enabled/disabled joystick camera ownership.
- FLY remained usable with no GPS device at all.
- Serial reconnect attempts did not stall or disable the EarthStick 30 Hz flight path.
- ArcGIS Earth camera flight remained independent of the failed GPS/serial subsystem.

### What this test proves

The integrated architecture successfully isolates the two subsystems:

- PRAVE/ME may be unavailable and retrying
- EarthStick can still fly ArcGIS Earth

This is the intended failure behavior.

### What this test does not yet prove

The following still need a physical live-GPS test before the integration is accepted as fully proven:

- fresh GPS ME recentering through the coordinator
- ME -> FLY while GPS is valid
- Button 1 RTH from FLY to current ME
- stale-GPS RTH rejection after a previously valid fix
- GPS recovery without automatic camera recenter
- deliberate RTH after GPS recovery

Do not convert software self-test results for those cases into claims of live field validation.
