# EarthStick Video Guide

## Standalone EarthStick v0.5 video

### Recommended title

**ArcGIS Earth SpaceMouse vs API Joystick Control**

Other strong options:

- **Fly ArcGIS Earth Like a Helicopter | EarthStick Joystick Control**
- **ArcGIS Earth + Thrustmaster: True 3D Flight Control**
- **EarthStick - Helicopter-Style Control for ArcGIS Earth**

### Thumbnail

Prepared 1280x720 comparison thumbnail:

`assets/EarthStick_YouTube_Thumbnail.gif`

Primary comparison text:

**ARCGIS EARTH**  
**SPACEMOUSE VS API JOYSTICK**

Bottom line:

**HELICOPTER-STYLE CONTROL - EARTHSTICK v0.5**

### Recommended structure

1. Show actual flight immediately: forward, strafe, twist, tilt, climb, hover.
2. State the idea: ArcGIS Earth already exposes the camera API; the TCA already exposes the controls; EarthStick connects them.
3. Show the hardware.
4. Prove X/Y, RZ, Slider0, POV, Button 4 and Button 3 in `joy.cpl`.
5. Enable ArcGIS Earth Automation API.
6. Start `EarthStick.bat`.
7. Demonstrate one control at a time, then combined flight.
8. Stop and hover on a real map target.
9. Show operational map layers.
10. End on the repository.

### Key standalone line

> The key is what happens when I do nothing: it stops and hovers exactly where I left it.

---

## Follow-up video - PRAVE/ME + EarthStick

The integration creates a second, stronger demonstration because the joystick is now tied to a real-position tracking workflow.

### Suggested title

**ArcGIS Earth GPS Tracking + Joystick Flight | ME / FLY / Return Home**

Other options:

- **Turn ArcGIS Earth Into a Substitute Drone | GPS + EarthStick**
- **PRAVE/ME + EarthStick: Track Here, Fly Anywhere, Trigger Home**
- **ArcGIS Earth Return-to-Home Camera Control with a Flight Stick**

### Best demo sequence

1. Start with a valid ME/GPS fix and show the camera following ME.
2. Point to the console/state showing **ME**.
3. Show the physical index-finger trigger and identify it as Button 1.
4. Squeeze once: **ME -> FLY**.
5. Fly away from the current real position using the normal EarthStick v0.5 controls.
6. Stop and hover somewhere clearly displaced from ME.
7. Squeeze Button 1: return to current ME and resume tracking.
8. Trigger back to FLY and leave again.
9. While in FLY, interrupt GPS/serial.
10. Keep flying to prove GPS loss does not kill the substitute-drone camera.
11. Try RTH while GPS is stale/missing and show that it is blocked.
12. Restore GPS and show that the camera does **not** automatically yank home.
13. Trigger deliberately to return to ME.

Do not record steps 1/7/11-13 as proven behavior until the live valid-GPS acceptance test has actually been completed.

### Core message

> **ME finds you. FLY lets you leave.**

The trigger becomes a deliberate map-camera Return-to-Home control when fresh GPS is available.

### Important failure demo

The 2026-10-25 no-GPS test already established a strong proof point: even with `COM12` completely absent and PRAVE repeatedly retrying the port, EarthStick remained connected and FLY remained usable.

That is worth showing because it demonstrates the architecture rather than just the happy path.

## Repository

https://github.com/Jim-dc95811/EarthStick

Mention clearly:

- standalone EarthStick v0.5 is accepted and standard-library-only
- PRAVE/ME + EarthStick v0.2.0 is a separate TEST integration and inherits PRAVE's `pyserial` dependency
- both use ArcGIS Earth's documented local Automation API
- project is independent and not affiliated with or endorsed by Esri, Thrustmaster, Guillemot or Airbus
