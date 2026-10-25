# Project Notes - Why EarthStick Exists

## The problem

ArcGIS Earth is capable of a rich 3D camera experience, but the normal desktop interaction model is still primarily mouse-driven.

A 3Dconnexion SpaceMouse was tested first because it is a commonly suggested class of controller for 3D applications. In this project's testing, that interaction model was a poor fit for the desired operational behavior. The camera felt like a scene being manipulated rather than a vehicle being piloted, and neutral/hover behavior was not natural enough for close inspection.

That is a statement about this workflow and this user's testing, not a universal judgment about SpaceMouse products.

## The breakthrough

The Thrustmaster TCA Sidestick exposed exactly the independent controls the job needed:

- X/Y stick axes
- twist/rudder axis
- throttle slider
- POV hat
- discrete buttons

ArcGIS Earth already exposed the other half of the solution: a documented local camera Automation API.

EarthStick is the small bridge between those two existing capabilities.

## The interaction goal

The design target was not "make ArcGIS Earth respond to a joystick."

The design target was:

> Make ArcGIS Earth behave like a helicopter moving through a 3D operational map.

That means:

- forward means forward in the current heading
- side movement is true strafe
- twist changes heading without forcing translation
- tilt is independent
- altitude is independent
- speed is independent
- neutral means stop and hover

## Why the hover behavior matters

For map inspection, the most useful default is no motion.

A user should be able to fly to a hydrant, parcel, road, tower, incident feature, or terrain location and simply release the controls. The camera should stay there while the operator studies the map.

EarthStick therefore commands motion rather than maintaining momentum.

## Development sequence

The initial v0.1 build established direct camera control.

Testing then exposed one issue at a time:

1. Windows/WinMM reported the controller using a generic driver name -> v0.2 controller capability fallback
2. Slider0 was not on the assumed WinMM U axis -> v0.3 Z/U/V slider detection
3. translation top speed was far too slow -> v0.4 20x speed multiplier
4. a helicopter control model needed independent altitude -> v0.5 Button 4 zoom in and Button 3 zoom out

At each step, the existing good behavior was preserved.

## First successful flight

The first v0.5 flight test demonstrated continuous combined control: forward motion, strafe, heading changes, tilt changes, throttle-controlled speed, rapid climb/zoom-out, descent/zoom-in, and immediate hover when the controls were released.

That is the standalone project baseline.

## PRAVE/ME integration - the next operational step

PRAVE/ME already solved a different ArcGIS Earth problem: keeping the camera associated with a real moving ME/GPS position while also handling PRAVE vehicle information.

Running PRAVE/ME and EarthStick as two independent camera writers would create a conflict: one program would continuously say "center on ME" while the other said "fly over there."

The integration therefore does not simply launch both programs together. It introduces explicit camera ownership:

- **ME** = real-position tracking/recentering
- **FLY** = free EarthStick camera control

This produced a concise operating concept:

> **PRAVE/ME finds you. EarthStick lets you leave.**

The T.A320 Button 1 index-finger trigger becomes the physical switch between those states in the integrated program.

## Return-to-home analogy

Once the operator has flown away from the ME location, Button 1 can serve as a map-camera equivalent of a drone RTH control.

With a fresh GPS position available:

- squeeze once in FLY
- return the camera to current ME
- resume ME tracking

This is deliberately not a blind return to an old cached coordinate. If GPS is stale or missing, the request is blocked and FLY continues.

## Failure isolation matters

The first integrated live test intentionally ran with no GPS device at all. `COM12` did not exist.

The serial side repeatedly failed and retried while:

- the T.A320 remained detected
- ArcGIS Earth API remained connected
- Button 1 still toggled ME/FLY
- FLY remained operational

That result established an important design rule:

> **GPS failure cannot be allowed to take the substitute-drone camera down with it.**

Likewise, if the joystick is absent, PRAVE/ME should remain useful by itself.

## Operational context

EarthStick becomes especially useful when ArcGIS Earth is already carrying operational layers such as offline imagery, parcels, hydrants, towers, roads, boundaries, and other point/line/polygon overlays. The joystick does not replace those datasets; it changes how the operator moves through them.

PRAVE/ME adds the real-world anchor. FLY provides the free camera.

## Keep it simple

The TCA has many buttons. EarthStick does not need to use them all.

A control gets assigned only when it solves a real navigation problem. Button 1 finally received a job because ME/FLY/RTH is a real operational need. The remaining unused buttons stay unused.
