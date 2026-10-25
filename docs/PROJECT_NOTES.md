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
4. a helicopter control model needed independent altitude -> v0.5 red trigger zoom in and black thumb zoom out

At each step, the existing good behavior was preserved.

## First successful flight

The first v0.5 flight test demonstrated continuous combined control: forward motion, strafe, heading changes, tilt changes, throttle-controlled speed, rapid climb/zoom-out, descent/zoom-in, and immediate hover when the controls were released.

That is the project baseline.

## Operational context

EarthStick becomes especially useful when ArcGIS Earth is already carrying operational layers such as offline imagery, parcels, hydrants, towers, roads, boundaries, and other point/line/polygon overlays. The joystick does not replace those datasets; it changes how the operator moves through them.

## Keep it simple

The TCA has many buttons. EarthStick does not need to use them all.

A control gets assigned only when it solves a real navigation problem. Unused buttons are a feature, not a defect.
