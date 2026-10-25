# EarthStick v0.5 First Flight Test

Date: 2026-10-25

## Test objective

Determine whether the TCA Sidestick + EarthStick bridge produces a practical direct-control navigation model in ArcGIS Earth, rather than merely proving that the camera can be moved programmatically.

## Preconditions

Confirmed before the flight test:

- T.A320 Pilot visible in Windows/Thrustmaster control panel
- X/Y full travel and centering verified
- RZ/twist full travel and centering verified
- Slider0 full travel verified
- POV directions verified
- red trigger confirmed as Button 4
- black thumb button confirmed as Button 3
- ArcGIS Earth Automation API connected
- v0.4 20x translation-speed increase accepted
- v0.5 altitude/zoom buttons added without changing the proven v0.4 movement controls

## Result

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

## Key finding

The decisive behavior is not any single axis. It is the combination of independent axes with a neutral stationary state.

The operator can fly to a location, release the controls, and study the map without continued drift or correction.

This was described during acceptance as acting like a helicopter: stop and hover in place unless told to do otherwise.

## Comparison lesson

A 3Dconnexion SpaceMouse had previously been tested for the same ArcGIS Earth navigation goal. In this specific workflow it was judged a poor fit because the interaction felt like manipulating a scene rather than piloting through it.

EarthStick's direct axis-to-camera model produced the desired behavior immediately once the speed and altitude controls were tuned.

This comparison reflects this project's field testing and should not be presented as a universal evaluation of SpaceMouse products.

## Baseline decision

v0.5 is the accepted behavior baseline. Do not change its control meanings, rates, dead zone, speed formula, or hover model without explicit discussion, a new version number, and another live ArcGIS Earth test.

## Flight image

See the prepared YouTube thumbnail `../assets/EarthStick_YouTube_Thumbnail.jpg`.
