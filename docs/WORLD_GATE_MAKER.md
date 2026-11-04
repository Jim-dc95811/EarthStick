# World Gate Maker 1.0 - User Manual

Printable copy: [World_Gate_Maker_User_Manual.pdf](World_Gate_Maker_User_Manual.pdf)

Make your own **World Gates**: pick two places, and World Gate Maker builds a pair of golden rings. Fly through the ring at one place with EarthStick and you come out at the other; the ring there brings you back.

![A World Gate named Home floating over Central Park, New York, at 520 ft](../images/world_gate_maker_central_park.jpg)

*Made with World Gate Maker: a "Home" gate over Central Park, partnered with a "Central Park" gate near home in Jacksonville.*

## What you need

- **EarthStick 1.3 or later** with its **Gates** folder ([EarthStick page](../README.md)).
- **ArcGIS Earth** desktop with the Automation API on (as for EarthStick).
- **Python 3** (as for EarthStick). World Gate Maker uses only the standard library: nothing to install.

## Start

1. Download [`World_Gate_Maker_v1.0.zip`](../releases/World_Gate_Maker_v1.0.zip), right-click it > **Extract All**.
2. Open the `World_Gate_Maker_v1.0` folder and double-click `World_Gate_Maker.bat`.

## Make a pair of gates

For **Place 1** and **Place 2**:

1. **Name** - what the place is called, for example `Home`, `Station 7`, `Central Park`. Keep names short (18 characters or fewer) so ArcGIS Earth shows them on one line.
2. **Latitude / Longitude** - type them, or use Google Maps: right-click the spot, click the numbers at the top of the menu to copy them, then press **From Clipboard**. The line underneath shows how they were read - check it.
3. **Ground elev (ft)** - in ArcGIS Earth, put the mouse pointer on the spot and read **elev** in the status bar at the bottom. Type that number.

Then:

4. **Height above ground (ft)** - how high the middle of each ring floats above the ground (default 500 ft).
5. **Ring size** - Small (100 m across), Medium (250 m, the default) or Large (450 m, the size of the World Gates pack).
6. Press **MAKE GATES**. The first time, choose the **Gates** folder inside your EarthStick folder; World Gate Maker remembers it.

It saves `Gate_<Place 1>_<Place 2>.kmz` and shows the eye alt to fly at for each ring.

## Fly them

1. Drag the new `.kmz` from the Gates folder onto ArcGIS Earth so you can see the rings.
2. **Restart EarthStick** - it reads the Gates folder when it starts. The console lists the new gates.
3. Fly to a ring, line up on its **gold** side, match the **eye alt** shown under its name, and fly through the middle.

## How the rings are set up

- Each ring is **named for where it takes you**: the ring at Place 1 carries Place 2's name, and the ring at Place 2 carries Place 1's name.
- Each ring **faces the other place**, so you fly toward home to go home.
- **Gold front, red back** - from the red side nothing happens.
- You arrive **300 m past the other ring**, heading away from it, so you never bounce straight back.
- Names and eye alt numbers show only when you are near (within about 4 miles), so far-away views stay clean.

## Messages

- **"The two places need different names"** - each ring is named for its destination, so the names must differ.
- **"Height above ground must be at least ... ft"** - the bottom of the ring would touch the ground. Raise the height or pick a smaller ring.
- **"The places are only ... m apart"** - the places are too close for that ring size.
- **"... is long"** - a name over 18 characters may split onto two lines in ArcGIS Earth. Shorten it if it does.
- **"... is not named 'Gates'"** - EarthStick only reads the Gates folder beside `EarthStick.py`. Choose that folder.

## Turning gates off

Move the `.kmz` out of the Gates folder (and remove it from ArcGIS Earth), then restart EarthStick.

## Self-test

```text
py -3 World_Gate_Maker.py --selftest
```

Checks coordinate reading, ring names and directions, heights, the safety limits and the saved file.
