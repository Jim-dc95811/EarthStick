# EarthStick 1.1 - change document

**Released:** 2026-10-31
**Type:** hardening release. Startup, connection and messages only.
**Download:** [`releases/EarthStick_v1.1.zip`](../releases/EarthStick_v1.1.zip)

**Flying is unchanged.** Every control and button mapping is identical to 1.0. So are the technical constants (30 Hz, deadzone 0.08, 55 deg/s heading, 45 deg/s tilt, 0.50 s idle resync, 0.75 s HTTP timeout), the throttle speed law, the zoom law, camera validation and both recovery paths. The API address is still `http://localhost:8000`.

## What changed

### 1. EarthStick waits for the joystick at startup

**1.0:** if the joystick was not plugged in when EarthStick started, it printed `EarthStick stopped: No Windows joystick is connected` and quit. That contradicted the Troubleshooting guide's advice to leave it running so it could retry, which was true only for an unplug during flight.

**1.1:** EarthStick says `Waiting for the joystick - plug it in or check joy.cpl.` and uses the same retry as a mid-flight reconnect. It continues as soon as the stick is detected. Ctrl+C still stops it.

### 2. The ArcGIS Earth connection ignores system proxies

**1.0:** EarthStick reached ArcGIS Earth at `localhost:8000` through Python's standard web library, which honors the computer's proxy setting even for `localhost`. On a PC with an agency or county proxy and no "bypass for local addresses" exception, every camera request went to the proxy and failed. EarthStick then waited at `Waiting for ArcGIS Earth Automation API...` forever.

**1.1:** the local ArcGIS Earth connection never uses a proxy. Nothing else about the connection changed.

### 3. The startup wait explains itself

**1.0:** while waiting for ArcGIS Earth, every error was retried silently, so a wrong program on port 8000 or a proxy problem looked like ArcGIS Earth simply was not open.

**1.1:** the reason is printed when it first appears and whenever it changes, with a reminder to check the Automation API setting. For example:

```text
  Still waiting: HTTP Error 404: Not Found
  Check that ArcGIS Earth is open with Automation API enabled (Settings > Advanced).
```

### 4. One prompt after an error

**1.0:** after a startup error, EarthStick asked for Enter and then `EarthStick.bat` asked for a key as well. **1.1** leaves the single prompt to the `.bat`.

The banner and window title show 1.1.

## Verification

- **Live acceptance:** Jim Gaddy flew EarthStick 1.1 with the Thrustmaster TCA Sidestick in ArcGIS Earth on 2026-10-31 and reported it working well.
- **Flight regression:** a scripted joystick drove 1.0 and 1.1 through forward flight, strafing, yaw, tilt in both directions, zoom in and out, mixed controls and idle periods, using a deterministic clock and a stand-in ArcGIS Earth camera API. All 335 camera writes were identical between the versions.
- **Startup with the joystick unplugged:** 1.0 stopped; 1.1 waited and flew once the joystick appeared.
- **Proxy configured:** 1.0 never connected; 1.1 connected and flew.
- **Another program on port 8000:** 1.0 waited silently; 1.1 showed the 404 reason once.
- **Built-in self-test** (`python EarthStick.py --selftest`) passes, and the release zip was extracted and tested before publication.
- **Verified in the test environment only:** the proxy and port-conflict cases.

## Checksums

| File | 1.0 SHA-256 | 1.1 SHA-256 |
|---|---|---|
| `EarthStick.py` | `d0db352b3fa44c1c94271309fc065e2da2dc897246a96bd3d38b2866c6ca41b3` | `84894c2f2d6c857ba71b2153126cb274254e3dbf23099ca1b821dbc2ca7400c7` |
| `EarthStick.bat` | `d707d1fc9b4bfbb13c5ae101f9957b4d9b248faef273fbee640cb47d27238e1c` | `e78fe1843674b5e1ffec5e60416e38032b757e203573cb52f5f6e271ec10c6c6` |
| release zip | `EarthStick_v1.0.zip` `8b399d70df582c448ed2bfdf532d5dcc17f579187f99a4d165bd06ef1cb0c292` | `EarthStick_v1.1.zip` `505295a68e041bec7ae921f2c71b5240816946a8d5bb5f48459f3b237819c52e` |

`releases/EarthStick_v1.0.zip` stays in the repository so existing links keep working. The PDF user guide was written for 1.0 and still applies to 1.1.
