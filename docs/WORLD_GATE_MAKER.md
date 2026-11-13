# World Gate Maker 2.0 - User Manual

<!-- install-blurb:start -->
> ### Installing World Gate Maker - read this first
>
> 1. **Open the tool's folder.** Easiest is **Google Drive** (the link at the top of the project page): the folder is already unpacked - just open it, nothing to extract. If instead you downloaded the **zip** from GitHub, right-click it > **Extract All** first, then open the new folder. (Double-clicking files while they are still inside a zip does not work.)
> 2. **Double-click `World_Gate_Maker.bat`** - the only .bat in the folder. This manual sits right next to it. The **System Files** folder holds the program - leave it alone.
> 3. **Blue "Windows protected your PC" box?** Click **More info**, then **Run anyway**. It only asks the first time. (Or, before extracting: right-click the zip > **Properties** > tick **Unblock** > **OK**.)
> 4. **Python - nothing to install by hand.** If Python is missing, the window asks **Install Python now? [Y/N]**: type **Y** and press Enter. It installs just for you (no admin needed). On an older PC this can take several minutes and Windows Defender may make the PC look frozen - **do not close the window**.
> 5. **Needs EarthStick:** start EarthStick 2.0 at least once first - it tells World Gate Maker where its **Gates** folder is. With EarthStick running, new gates appear in it within seconds (no restart).
> 6. To see the gates you need **ArcGIS Earth** (free from Esri: https://www.esri.com/en-us/arcgis/products/arcgis-earth/downloads).
>
> Something stops it? The window says what to do in plain words, and keeps a log in `System Files\Ready_To_Fly_log.txt`. On a work computer that blocks installs, ask IT to install Python 3 from python.org.
<!-- install-blurb:end -->


Printable copy: [World_Gate_Maker_User_Manual.pdf](World_Gate_Maker_User_Manual.pdf)

Make your own **World Gates**: pick two places, and World Gate Maker builds a pair of golden gates. Fly through the gate at one place with EarthStick and you come out at the other; the gate there brings you back.

**New in 2.0** (8 Nov 2026 - the whole family moved to 2.0): World Gate Maker saves into **the EarthStick you actually fly**, the line under *Save into* says which one, and with EarthStick 2.0 running your new gates are armed and shown on the map within seconds - **no restart, no dragging**.

**New in 1.1:** the gates are **squares with four legs** running back from the corners - the same look as the World Gates pack in EarthStick 1.3.4. One glance shows where the way in is and which way the gate points.

![A square World Gate named jax seen from the side over Seattle: the gold square and its legs make a box that points the way in](../images/world_gate_maker_v1.1_seattle_arrival.jpg)

*Jacksonville to Seattle with World Gate Maker 1.1: just arrived in Seattle, with the "jax" gate home seen from the side - the legs show the way in at a glance.*

![Back home in Jacksonville, lined up on the square Seattle gate with the green RING HEIGHT light on at 1,020 ft](../images/world_gate_maker_v1.1_home_ring_height.jpg)

*Safe return home: lined up on the "Seattle" gate in Jacksonville, at the gate's height (1,020 ft) - EarthStick 1.3.4's green **RING HEIGHT** light is on.*

![A World Gate named Home floating over Central Park, New York, at 520 ft](../images/world_gate_maker_central_park.jpg)

*Made with World Gate Maker 1.0 (when gates were rings): a "Home" gate over Central Park, partnered with a "Central Park" gate near home in Jacksonville.*

## What you need

- **EarthStick** with its **Gates** folder ([EarthStick page](../README.md)) - **start EarthStick 2.0 at least once** before using World Gate Maker: EarthStick leaves a small note (`%LOCALAPPDATA%\ArcGIS Earth Unlocked\last_earthstick.txt`) saying where its Gates folder is, and World Gate Maker reads it. Gates made for EarthStick 1.3 or later work in any of them.
- **ArcGIS Earth** desktop with the Automation API on (as for EarthStick).
- **Python 3** - since 1.2.1 `World_Gate_Maker.bat` installs it for you if it is missing (answer **Y**; no admin needed). World Gate Maker uses only the standard library: nothing else to install.

## Start

1. Download [`World_Gate_Maker_v2.0.zip`](../releases/World_Gate_Maker_v2.0.zip), right-click it > **Extract All**.
2. Open the `World_Gate_Maker_v2.0` folder and double-click `World_Gate_Maker.bat`. (Beside it: this manual as a PDF. `System Files` holds the program - leave it alone.)

**Where it saves (2.0).** Under *Save into* World Gate Maker shows the Gates folder it will use, and a line that says why:

- **EarthStick 2.0 running now - its Gates folder** (green): the EarthStick you are flying. Best case: your gates appear in it within seconds.
- **EarthStick 2.0 flown last** (green): the EarthStick you flew last time; the gates are ready next time you fly.
- **Newest EarthStick found nearby** (green): no note yet (EarthStick 2.0 never started), so it picked the newest EarthStick folder next to World Gate Maker.
- **EarthStick not found** (red): start EarthStick once, then reopen World Gate Maker - or press **Choose...** and pick the Gates folder inside your EarthStick folder.

**Choose...** only accepts an EarthStick Gates folder. Picking the EarthStick folder itself or its *System Files* folder is fine - it switches to the Gates folder for you; any other folder is refused.

## What's in the zip

![What's in the World Gate Maker folder: World_Gate_Maker.bat opens the gate maker, System Files holds the program, and it makes a Gate_ kmz file in EarthStick's Gates folder](../images/world_gate_maker_whats_in_the_zip.png)

## Make a pair of gates

For **Place 1** and **Place 2**:

1. **Name** - what the place is called, for example `Home`, `Station 7`, `Central Park`. Keep names short (18 characters or fewer) so ArcGIS Earth shows them on one line.
2. **Latitude / Longitude** - type them, or use Google Maps: right-click the spot, click the numbers at the top of the menu to copy them, then press **From Clipboard**. The line underneath shows how they were read - check it.
3. **Ground elev (ft)** - in ArcGIS Earth, put the mouse pointer on the spot and read **elev** in the status bar at the bottom. Type that number.

Then:

4. **Height above ground (ft)** - how high the middle of each gate floats above the ground (default 500 ft).
5. **Gate size** - the width of the square: Small (70 m), Medium (180 m, the default) or Large (320 m, the size of the World Gates pack). The legs grow with it: 71 m, 178 m and 320 m.
6. Press **MAKE GATES**. The file goes into the Gates folder shown under *Save into*.

It saves `Gate_<Place 1>_<Place 2>.kmz` and shows the eye alt to fly at for each gate.

## Fly them

1. **EarthStick 2.0 running?** Nothing to do: within a few seconds it shows **NEW GATES ARMED · Gate_...** and puts the gates on the map. (Older EarthStick, or EarthStick not running: start it, or close its window and start it again - it reads the Gates folder when it starts; then drag the new `.kmz` from the Gates folder onto ArcGIS Earth to see the gates.)
2. The **Saved** message tells you which of the two applies.
3. Fly to a gate, line up on its **gold** side, match the **eye alt** shown under its name, and fly through the middle. Lined up straight, the four legs make an even X; if they lean, you are off to that side or too high or low.
4. With **EarthStick 1.3.4 or later**, a green **RING HEIGHT** light comes on when you are at the gate's height, and on the last 1,500 m the tractor beam pulls you onto it (**LOCKED ON**). The beam grabs you when you are within the gate's grab zone above or below its middle: Small ±164 ft, Medium ±410 ft, Large ±738 ft. Higher or lower than that, it lets you fly past. Hold Button 3 or 4 to break free.

## How the gates are set up

- Each gate is **named for where it takes you**: the gate at Place 1 carries Place 2's name, and the gate at Place 2 carries Place 1's name.
- Each gate **faces the other place**, so you fly toward home to go home.
- **Gold front, red back** - from the red side nothing happens. The legs point out the back (the way you leave).
- You arrive **300 m in front of the other gate**, heading away from it, so you never bounce straight back.
- Names and eye alt numbers show only when you are near (within about 4 miles), so far-away views stay clean.

## Messages

- **"The two places need different names"** - each gate is named for its destination, so the names must differ.
- **"Height above ground must be at least ... ft"** - the bottom of the gate would touch the ground. Raise the height or pick a smaller gate.
- **"The places are only ... m apart"** - the places are too close for that gate size.
- **"... is long"** - a name over 18 characters may split onto two lines in ArcGIS Earth. Shorten it if it does.
- **"... is not an EarthStick Gates folder"** (Choose...) - open your EarthStick folder (the one with `Fly_ArcGIS_Earth.bat`) and pick the **Gates** folder inside it.
- **"This Gates folder no longer exists"** - the EarthStick folder was moved or deleted. Choose the Gates folder of the EarthStick you use now.

## Turning gates off

Delete the `.kmz` from the Gates folder (or move it out). EarthStick 2.0 disarms it within a few seconds and, if it put the file on the map, takes it off; otherwise remove it from ArcGIS Earth's Data list yourself. (Older EarthStick: restart it.)

## Self-test

From a command prompt in the World Gate Maker folder's **System Files**:

```text
py -3 World_Gate_Maker.py --selftest
```

Checks coordinate reading, gate names and directions, heights, the safety limits, the square and its legs, and the saved file.
