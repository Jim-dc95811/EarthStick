# EarthStick v0.5 Technical Notes

## 1. Purpose and standalone architecture

EarthStick is a small Windows/Python bridge between a Thrustmaster TCA Sidestick Airbus Edition and the ArcGIS Earth REST Automation API.

```text
TCA Sidestick -> Windows WinMM joystick API -> EarthStick.py -> HTTP -> ArcGIS Earth camera
```

It deliberately avoids mouse/keyboard emulation and avoids third-party Python packages in the standalone v0.5 program.

## 2. External interfaces

### 2.1 ArcGIS Earth Automation API

EarthStick uses Esri's documented camera endpoints:

- `GET /arcgisearth/camera`
- `PUT /arcgisearth/camera`

Default base URL:

`http://localhost:8000`

ArcGIS Earth exposes camera position x/y/z plus spatial reference and heading, tilt, and roll. EarthStick works in WKID 4326.

References:

- https://doc.arcgis.com/en/arcgis-earth/automation-api/overview.htm
- https://doc.arcgis.com/en/arcgis-earth/automation-api/use-api.htm
- https://doc.arcgis.com/en/arcgis-earth/automation-api/set-camera.htm

### 2.2 Windows joystick input

EarthStick uses the Windows multimedia joystick API through Python `ctypes`:

- `joyGetNumDevs`
- `joyGetDevCapsW`
- `joyGetPosEx`
- `JOYCAPS`
- `JOYINFOEX`

The code loads `winmm.dll` directly.

Microsoft describes this joystick interface as a legacy API and recommends Windows.Gaming.Input for new development when possible. EarthStick intentionally uses WinMM in v0.5 because it provides the required axes, buttons, and POV data with no external Python dependency and has been proven on the target controller.

## 3. Controller identification

The primary requested Windows name is:

`T.A320 Pilot`

During testing, `joy.cpl` displayed that product name while the WinMM API reported the generic string:

`Microsoft PC-joystick driver`

v0.2 added a fallback that identifies a unique attached controller with:

- at least 4 axes
- 17 buttons
- POV capability

This matches the tested TCA Sidestick characteristics.

## 4. Slider0 detection

The TCA throttle appeared as Slider0 in the Thrustmaster control panel, but WinMM may expose that physical slider on Z, U, or V.

v0.3 therefore inspects joystick capability flags and accepts exactly one present slider candidate among:

- Z -> `dwZpos`
- U -> `dwUpos`
- V -> `dwVpos`

If zero or multiple candidates are present, EarthStick stops rather than guessing.

## 5. Polling and update loop

Main constants in v0.5:

- joystick/camera loop: `30 Hz`
- axis dead zone: `0.08`
- yaw rate: `55 degrees/second`
- tilt rate: `45 degrees/second`
- idle camera resync: `0.50 seconds`
- HTTP timeout: `0.75 seconds`
- Earth radius used for translation: `6,378,137 m`

The standalone loop:

1. reads joystick state
2. applies dead zones and inversions
3. detects zoom buttons
4. re-syncs the camera from ArcGIS Earth when motion begins
5. updates altitude when a zoom button is held
6. computes current translation speed from throttle and altitude
7. converts heading-relative forward/right travel to latitude/longitude deltas
8. updates heading and tilt
9. PUTs the new camera to ArcGIS Earth
10. prints live status

## 6. Axis normalization

Centered axes are normalized to `-1.0 .. +1.0`.

A dead zone of 0.08 is applied, then the remaining travel is re-scaled so full physical travel still reaches +/-1.0.

Throttle is normalized to `0.0 .. 1.0`.

The tested controller required:

- twist inversion for intuitive right twist = increasing/right heading
- throttle inversion so physical forward throttle = faster movement

## 7. Translation math

EarthStick interprets stick Y as forward/back and stick X as right/left movement relative to the current heading.

For heading `h`:

```text
north = forward*cos(h) - right*sin(h)
east  = forward*sin(h) + right*cos(h)
```

Small-step meter offsets are converted to latitude/longitude using a spherical Earth approximation with radius 6,378,137 m.

Latitude is clamped to +/-89.9 degrees and longitude is wrapped to -180..180.

This is a camera-navigation calculation, not a geodetic survey engine.

## 8. Throttle and movement speed

Speed uses a quadratic throttle curve:

```text
speed = min_speed + (max_speed - min_speed) * throttle^2
```

where:

```text
min_speed = 0.5 m/s
base_max = clamp(max(8, altitude * 0.020), 8, 12000)
max_speed = base_max * 20
```

The `* 20` multiplier was introduced in v0.4 after direct ArcGIS Earth flight testing showed the earlier maximum was far too slow for useful wide-area travel.

The quadratic curve keeps the low throttle range usable for close inspection while allowing very rapid translation at the top end.

## 9. Zoom / altitude

v0.5 assigns:

- Button 4 red top button -> zoom in / descend
- Button 3 black thumb -> zoom out / climb

While held:

```text
zoom_rate = max(2.0 m/s, altitude * 0.75 per second)
```

Altitude is never allowed below 1 meter by EarthStick.

## 10. POV tilt

Only POV up/down is used.

- up sector -> positive tilt command
- down sector -> negative tilt command
- left/right sectors -> no EarthStick action

Tilt is clamped to ArcGIS Earth's documented `0..180` degree range.

## 11. Hover behavior

Hover is not a separate mode. It falls naturally out of the control model.

When all movement axes are inside the dead zone, POV tilt is neutral, and neither zoom button is held, EarthStick stops sending motion changes. ArcGIS Earth's camera remains at its last position.

## 12. Mouse coexistence

While EarthStick is idle it re-reads the ArcGIS Earth camera periodically. When joystick activity begins after idle, it also immediately re-reads the camera.

This prevents EarthStick from snapping back to an old internal camera state after the user navigates with the mouse.

## 13. Standalone error behavior

- no joystick -> stops with an error
- controller not uniquely identified -> stops rather than selecting an arbitrary device
- Slider0 axis not uniquely detected -> stops rather than guessing
- ArcGIS Earth unavailable at startup -> waits and retries
- transient PUT failure -> attempts to re-read the current camera
- unsupported spatial reference -> stops with diagnostic

## 14. Known v0.5 cosmetic strings

The proven v0.5 baseline contains two stale text strings:

1. startup says `Buttons are intentionally unused in this build.` even though Buttons 3 and 4 are now used for zoom
2. the non-4326 camera error says `EarthStick 0.3 expects WKID 4326`

These are cosmetic only and remain unchanged in the accepted baseline.

## 15. Tested control map

| Input | Standalone EarthStick v0.5 behavior |
|---|---|
| X | strafe |
| Y | forward/back |
| RZ | heading |
| Slider0 | speed |
| POV up/down | tilt |
| Button 4 | zoom in |
| Button 3 | zoom out |
| Button 1 | unused |

Button 1 was later physically mapped as the index-finger / gun-style trigger and is used only by the separate PRAVE/ME integration.

---

# PRAVE/ME + EarthStick v0.2.0 TEST Technical Notes

## 16. Integration objective

The integration solves a camera-ownership problem.

Two independent programs cannot safely command contradictory ArcGIS Earth camera positions at the same time. PRAVE/ME wants to keep X/Y centered on ME; EarthStick wants to move the camera freely.

The v0.2 integration therefore places both preserved cores behind one coordinator.

## 17. Preserved modules

The test package preserves:

- `AE_PRAVE_LIVE_v0_1_0_TEST.py`
- exact EarthStick v0.5 `EarthStick.py`

The new module is:

- `PRAVE_ME_FLY_v0_2.py`

The coordinator imports both cores rather than rewriting their internal algorithms.

## 18. Thread separation

The original PRAVE serial path can block on serial reading/reconnection. It must not be allowed to reduce EarthStick's accepted 30 Hz response.

The integration therefore separates:

- PRAVE serial/reconnect work in its own worker thread
- camera/joystick control in the 30 Hz coordinator loop

This preserves flight responsiveness even when the serial side is repeatedly failing/retrying.

The live no-GPS test with nonexistent `COM12` confirmed this isolation behavior operationally.

## 19. Single camera writer

The integration redirects PRAVE camera-center requests into coordinator state rather than allowing direct competing camera PUTs.

Camera ownership is explicit:

```text
ME  -> coordinator performs PRAVE/ME recenter requests
FLY -> coordinator performs EarthStick v0.5 camera updates
```

PRAVE point/ME drawing operations remain on the PRAVE side.

## 20. Button 1 edge toggle

Integration constant:

`ME_FLY_BUTTON = 1`

Button 1 is treated as an edge-triggered control. One squeeze changes state once; holding it does not repeatedly toggle ME/FLY.

Standalone EarthStick v0.5 does not assign Button 1.

## 21. GPS state and RTH freshness

Integration constant:

`GPS_RETURN_MAX_AGE_SECONDS = 5.0`

The coordinator retains the latest accepted PRAVE `RMCPosition` and its monotonic receive time.

A FLY -> ME Button 1 request is accepted only if that latest position is fresh under the 5-second threshold.

This prevents a GPS failure from causing return to an old cached position.

## 22. GPS recovery behavior

Publishing a new fresh GPS position while in FLY does not change `me_tracking_enabled` by itself.

Therefore receiver recovery cannot automatically pull the camera away from the operator's current inspection location.

A new deliberate Button 1 press is required.

## 23. No-GPS behavior

If no GPS position has ever been received:

- ME -> FLY remains allowed
- FLY camera control remains independent
- FLY -> ME through Button 1 is rejected because there is no fresh home position

The serial worker may continue reconnect attempts without changing the camera-owner state.

## 24. No-joystick behavior

The coordinator allows PRAVE/ME operation if EarthStick cannot be imported/detected.

In that condition:

- PRAVE/ME remains useful
- joystick flight is unavailable
- the legacy keyboard `T` mechanism remains the fallback tracking control

## 25. Dependencies

Standalone EarthStick v0.5 remains standard-library-only.

The integrated package inherits the existing PRAVE/ME dependency on `pyserial`.

Do not describe the integrated package as zero-dependency.

## 26. Integration self-test coverage

The current self-test checks, among other things:

- preserved PRAVE parser/core test
- preserved EarthStick v0.5 self-test
- EarthStick module version = 0.5
- EarthStick polling = 30 Hz
- accepted 20x speed math
- Button 1/3/4 bit masks
- ME -> FLY works without GPS
- FLY -> ME blocks missing/stale GPS
- GPS recovery alone does not auto-return
- neutral hover behavior
- Button 4 zoom-in
- Button 3 zoom-out

Software tests do not replace live ArcGIS Earth + serial + hardware acceptance.

## 27. Version rule

Standalone EarthStick v0.5 and integrated PRAVE/ME + EarthStick v0.2.0 TEST are separate version lines.

Any future code modification to either program must receive a new version number for that program. Do not silently change the v0.5 snapshot inside the integration package while continuing to call it v0.5.
