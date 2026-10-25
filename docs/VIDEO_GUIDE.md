# EarthStick Video Guide

## Recommended title

**ArcGIS Earth SpaceMouse vs API Joystick Control**

Other strong options:

- **Fly ArcGIS Earth Like a Helicopter | EarthStick Joystick Control**
- **ArcGIS Earth + Thrustmaster: True 3D Flight Control**
- **EarthStick - Helicopter-Style Control for ArcGIS Earth**

## Thumbnail

Prepared 1280x720 comparison thumbnail:

`assets/EarthStick_YouTube_Thumbnail.gif`

Primary comparison text:

**ARCGIS EARTH**  
**SPACEMOUSE VS API JOYSTICK**

Bottom line:

**HELICOPTER-STYLE CONTROL - EARTHSTICK v0.5**

## Recommended video structure

### 1. Show the result first - 10 to 20 seconds

Open with actual flight footage.

Demonstrate, without explanation yet:

- forward flight
- strafe
- twist/heading
- tilt
- fast climb/zoom-out
- stop and hover

The viewer should understand the benefit before seeing setup screens.

### 2. State the idea

Suggested wording:

> ArcGIS Earth already has a camera Automation API. The Thrustmaster sidestick already has the physical controls. EarthStick connects the two and turns ArcGIS Earth into a helicopter-style 3D navigation environment.

### 3. Show the hardware

Show the Thrustmaster TCA Sidestick Airbus Edition.

Briefly point out:

- main X/Y stick
- twist
- throttle slider
- POV hat
- red trigger
- black thumb button

Do not waste time explaining the unused buttons.

### 4. Prove Windows input

Run `joy.cpl` and show the T.A320 controller Properties/Test Input screen.

Quickly demonstrate:

- X/Y
- RZ
- Slider0
- POV
- Button 4 red trigger
- Button 3 black thumb

### 5. Enable ArcGIS Earth Automation API

Show the ArcGIS Earth Advanced settings and enable Automation API.

Mention default localhost port 8000.

### 6. Start EarthStick

Show the folder containing:

- `EarthStick.py`
- `EarthStick.bat`

Double-click the BAT file and show:

`ArcGIS Earth: connected`

### 7. Control demonstration

One control at a time:

- forward/back
- strafe
- twist
- POV tilt
- throttle slow to fast
- red trigger zoom in
- black thumb zoom out

Then combine them.

### 8. Demonstrate hover

This deserves its own moment.

Fly to a target, release the controls, and point out that the default state is stopped in place.

Suggested line:

> The key is what happens when I do nothing: it stops and hovers exactly where I left it.

### 9. Show real map layers

Use the same kind of operational content already proven in ArcGIS Earth: imagery, road overlays, parcels, hydrants, towers, county boundaries, or other useful layers.

The point is not just that the camera flies. The point is that the operator can fly through a real GIS workspace.

### 10. Close with the repository

Show:

https://github.com/Jim-dc95811/EarthStick

Mention:

- MIT licensed
- Python standard library only
- Windows
- ArcGIS Earth Automation API
- tested with Thrustmaster TCA Sidestick Airbus Edition

## Suggested YouTube description

EarthStick adds helicopter-style joystick navigation to ArcGIS Earth desktop on Windows.

Using a Thrustmaster TCA Sidestick Airbus Edition and ArcGIS Earth's built-in Automation API, EarthStick provides direct control of forward/back movement, strafe, heading, camera tilt, travel speed, and altitude/zoom.

The important behavior is neutral = hover. Release the controls and the camera stops where you left it.

Current controls:
- Stick forward/back: fly forward/reverse
- Stick left/right: strafe
- Twist: heading
- Slider0: speed
- POV up/down: tilt
- Red trigger / Button 4: zoom in
- Black thumb / Button 3: zoom out

No third-party Python packages are required.

GitHub:
https://github.com/Jim-dc95811/EarthStick

ArcGIS Earth is a product of Esri. TCA Sidestick Airbus Edition and Thrustmaster are trademarks/product names of their respective owners. EarthStick is an independent open-source project and is not affiliated with or endorsed by Esri, Thrustmaster, or Airbus.

## Suggested tags

ArcGIS Earth, ArcGIS, Esri, SpaceMouse, 3Dconnexion, joystick, Thrustmaster, TCA Sidestick, Airbus joystick, GIS, 3D GIS, mapping, helicopter control, camera control, Automation API, offline maps, first responder GIS
