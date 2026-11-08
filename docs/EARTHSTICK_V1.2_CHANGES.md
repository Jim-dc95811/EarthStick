# EarthStick 1.2 - change document

**Released:** 2026-11-01
**Type:** feature release. One new control: trigger-click.
**Download:** [`archive/EarthStick_v1.2.zip`](../archive/EarthStick_v1.2.zip)

**Flying is unchanged.** Every 1.1 control, constant, speed and zoom law, and both recovery paths are identical. The API address is still `http://localhost:8000`.

## What changed

### Trigger-click: open information boxes with the joystick

**1.1:** to open an object's information box (popup) you had to let go of the stick and use the mouse.

**1.2:** a red crosshair sits in the middle of the ArcGIS Earth window. Fly an object under it, hover, and pull the trigger (Button 1). EarthStick moves the Windows mouse pointer onto the object, clicks it, and puts the pointer back. To close the box, aim at open map and pull the trigger again.

Details:

- one click per pull, and a second pull within 0.8 s is ignored, so a bouncy trigger cannot become a double-click (which zooms in)
- the pointer glides onto the object and rests before and after the click; an instant click makes ArcGIS Earth zoom instead of selecting
- the crosshair is click-through, follows the ArcGIS Earth window, and hides while ArcGIS Earth is minimized
- if ArcGIS Earth is behind another window, the first click brings it forward and the second opens the object
- if the crosshair cannot be shown, the console says why and EarthStick flies as 1.1

### Package layout

The zip now holds a folder, `EarthStick_v1.2/`, containing `EarthStick.py` and `EarthStick.bat` (1.1 held the two files with no folder). The banner and window title show 1.2.

### Not included

A test build mapped Button 2 to close the information box with `Esc`. It did not work on the tested PC, and it is not needed because a trigger-click on open map closes the box, so it was left out. Buttons other than 1, 3 and 4 stay unassigned.

## Verification

- **Live acceptance:** Jim Gaddy flew EarthStick 1.2 with the Thrustmaster TCA Sidestick in ArcGIS Earth on 2026-11-01, opened object popups with the trigger ("works great"), and closed them by trigger-clicking open map.
- **Click recipe:** proven live in the trigger-click test builds (v0.1 and v0.2 zoomed in; v0.3's glide-and-rest click opened the popup).
- **Flight regression:** a scripted joystick drove 1.1 and 1.2 through forward flight, strafing, yaw, tilt, zoom in and out, mixed controls and idle periods, with a deterministic clock and a stand-in ArcGIS Earth camera API. All 335 camera writes were byte-identical.
- **Trigger regression:** scripted trigger pulls, including a bounce inside the lockout, produced one click per pull, and flying alongside the pulls matched 1.1.
- **Built-in self-test** (`py -3 EarthStick.py --selftest`) passes, including the new trigger gate checks; the release zip was extracted and tested before publication.
- **Verified on the tested PC only:** the crosshair position on other screen scalings and multi-monitor layouts.

## Checksums

| File | 1.1 SHA-256 | 1.2 SHA-256 |
|---|---|---|
| `EarthStick.py` | `84894c2f2d6c857ba71b2153126cb274254e3dbf23099ca1b821dbc2ca7400c7` | `63dd9b55af8aa8273dee212ed2da41ea73395752da898b8a09877d6f9bbefe5a` |
| `EarthStick.bat` | `e78fe1843674b5e1ffec5e60416e38032b757e203573cb52f5f6e271ec10c6c6` | `dbae78421544ae029e29d71f2f6d573fc64b65ec1453accc013de404935dbe8c` |
| release zip | `EarthStick_v1.1.zip` `505295a68e041bec7ae921f2c71b5240816946a8d5bb5f48459f3b237819c52e` | `EarthStick_v1.2.zip` `ad114b6197037f8851db459b244f98befee70066b458369ea993b0dcd6f224a5` |

`archive/EarthStick_v1.0.zip` and `archive/EarthStick_v1.1.zip` stay in the repository so existing links keep working.
