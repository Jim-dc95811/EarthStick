# EarthStick 1.3 - change document

**Released:** 2026-11-02
**Type:** feature release. One new feature: World Gates (wormholes).
**Download:** [`archive/EarthStick_v1.3.zip`](../archive/EarthStick_v1.3.zip)

**Flying is unchanged.** Controls, constants, speed and zoom laws, trigger-click and both recovery paths are identical to 1.2. With no gate files, EarthStick sends exactly the same camera positions as 1.2.

## What changed

### World Gates

Jim Gaddy's idea: a golden ring hovering in the sky, labelled with a destination. Fly into it and the map position changes to that destination; a return gate waits there to bring you home.

- Gate files (KMZ) go in a **Gates** folder beside `EarthStick.py` and are read at startup. Open the same file in ArcGIS Earth to see the rings.
- Fly through a ring from its **gold** side, at the altitude shown under its name, and the camera jumps to the destination, still flying, facing the landmark. The red side is the back; from there, above, below or beside the ring, nothing happens.
- One trip per pass (2-second rest after a jump). Gates fire only while the joystick is moving the camera.
- A gate leads to a partner gate or to a fixed spot (one-way). Partners are found in the same file first, so several gate files can share names.
- Console: the armed gates are listed at startup and each jump is reported (`Wormhole: through the Paris gate.`).

### World Gates pack (included)

`Gates/World_Gates_JAX_ATL.kmz`: Jacksonville International -> Atlanta hub (eight gates in a 3 km circle around Hartsfield-Jackson at eye alt 2,530 ft) -> New York, London, Paris, Rome, Tokyo, Sydney and Rio de Janeiro landmarks, each with a gate back to Atlanta, and Atlanta -> Jacksonville. Gold front, red back; each name beside its own ring with the eye alt below it.

## How it was developed (2026-11-02, all live in ArcGIS Earth by Jim)

1. Two golden test rings, NYC over downtown Jacksonville and JAX over the Statue of Liberty - look approved.
2. **First live jump, 19:41:** through the NYC ring over the St. Johns River, out over New York Harbor. Then home again.
3. Jim: "Above the city's airport we could have a series of rings taking you around the world" - and "a gate between Jax and ATL, where I can then transfer to my international flights... just like in real life."
4. Flights Jacksonville -> Atlanta -> London -> Atlanta -> Rio -> Atlanta -> Tokyo -> Atlanta -> Paris, refining the layout on the way: red back sides (Jim), labels moved beside their own rings after a label sat one floor up and sent Jim to London instead of New York, bigger 450 m rings, and finally eight equal-height gates in a circle around the airport (Jim: "someone in the middle could just spin and pick 1 of 8 ways to go"), widened to 3 km.
5. **Measured:** ArcGIS Earth's eye alt is height above sea level (Jim crossed the London ring at eye alt ~3,570 ft; its centre was 3,726 ft above sea level, 2,700 ft above the Atlanta field).

## Verification

- **Live:** Jim Gaddy flew every stage above in ArcGIS Earth with the Thrustmaster TCA Sidestick, 2026-11-02 (Jim: "insane experience", "magnifique").
- **Regression:** with no gate files, the scripted 335-step flight produces byte-identical camera writes to 1.2. Trigger-click regression unchanged.
- **Wormhole flight test:** a scripted flight through a gate makes exactly one jump, lands at the partner with the correct position, altitude and heading, keeps tilt, and does not bounce back.
- **World Gates layout check:** from the Atlanta hub centre, each of the eight compass headings passes through its own gate and no other; the arrival heading points between gates.
- **Self-test** extended: forward crossing, backwards (no jump), above, beside, partner arrival, one-way gates.

## Checksums

| File | 1.2 SHA-256 | 1.3 SHA-256 |
|---|---|---|
| `EarthStick.py` | `63dd9b55af8aa8273dee212ed2da41ea73395752da898b8a09877d6f9bbefe5a` | `df0e48dda1da08a7439b118bb5f44d731f6c215e4e86d4f7f223fae9dbde26fe` |
| `EarthStick.bat` | `dbae78421544ae029e29d71f2f6d573fc64b65ec1453accc013de404935dbe8c` | `ea8ce6e193870065f7d0a8183eb7feab9ee7c7c51e3a85a5f3c3a3efcf587d27` |
| `Gates/World_Gates_JAX_ATL.kmz` | - | `3611b6c3094eb68034b45ba16bb4b1eaac2d91c8f6b3f946fa37a9ad0c001a0a` |
| release zip | `ad114b6197037f8851db459b244f98befee70066b458369ea993b0dcd6f224a5` | `EarthStick_v1.3.zip` `0e8c394748f428eef42fed5aa1da5e5d317557082505ad4ca52e4d271ce0731f` |

The 1.0, 1.1 and 1.2 zips stay in `releases/` so existing links keep working.
