# Acknowledgements and Trademark Notice

EarthStick exists because several independent technologies expose clean interfaces that can be connected together.

## Esri / ArcGIS Earth

EarthStick uses the public **ArcGIS Earth Automation API** to read and update the camera.

Official documentation:

- https://doc.arcgis.com/en/arcgis-earth/automation-api/overview.htm
- https://doc.arcgis.com/en/arcgis-earth/automation-api/use-api.htm
- https://doc.arcgis.com/en/arcgis-earth/automation-api/set-camera.htm

ArcGIS, ArcGIS Earth, and Esri are trademarks or registered trademarks of Esri in the United States and other jurisdictions.

EarthStick is an independent project and is not affiliated with, sponsored by, or endorsed by Esri.

## Thrustmaster

EarthStick v0.5 was developed and tested with the **Thrustmaster TCA Sidestick Airbus Edition**.

Thrustmaster's hardware provides the physical X/Y axes, twist/rudder, throttle slider, POV hat, and buttons used by EarthStick.

Official product/support references:

- https://www.thrustmaster.com/en-us/products/tca-sidestick-airbus-edition/
- https://support.thrustmaster.com/en/kb/1764-en/

Thrustmaster and TCA product names are trademarks/product names of Guillemot Corporation S.A. and/or its affiliates.

EarthStick is an independent project and is not affiliated with, sponsored by, or endorsed by Thrustmaster or Guillemot Corporation.

## Airbus

The controller's commercial product name includes **Airbus** because the TCA Sidestick Airbus Edition is a Thrustmaster product inspired by Airbus flight controls.

Airbus names and marks belong to Airbus and their respective owners. EarthStick has no affiliation with or endorsement by Airbus.

## Microsoft Windows

EarthStick reads joystick state using the Windows multimedia joystick API (`winmm.dll`), including `joyGetDevCapsW` and `joyGetPosEx`.

Microsoft documentation:

- https://learn.microsoft.com/en-us/windows/win32/multimedia/joystick-reference
- https://learn.microsoft.com/en-us/windows/win32/api/joystickapi/nf-joystickapi-joygetposex

Microsoft identifies this joystick API as legacy and recommends Windows.Gaming.Input for new development when possible. EarthStick v0.5 retains WinMM because it is dependency-free from Python, exposes the needed controls, and is proven on the target hardware.

Windows and Microsoft are trademarks of Microsoft Corporation.

## Python

EarthStick is written in Python.

Standalone EarthStick v0.5 intentionally uses only the Python standard library; no third-party Python package is required by the standalone program.

The separate PRAVE/ME + EarthStick integration preserves the existing PRAVE/ME dependency on **pyserial** for serial input. That dependency belongs to the PRAVE/ME side of the integrated package and does not change standalone EarthStick v0.5.

Python is a trademark of the Python Software Foundation.

## Open-source license

The EarthStick source code and project documentation are distributed under the repository's MIT License unless otherwise noted.

Third-party product names, screenshots, maps, imagery, and trademarks remain the property of their respective owners and are used for identification, documentation, and demonstration only.
