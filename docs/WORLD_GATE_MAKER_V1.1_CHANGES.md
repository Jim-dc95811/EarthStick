# World Gate Maker 1.1 - Square gates (2026-11-05)

## Why

Jim, flying round gates: it was hard to tell where a ring's way in was and whether you were lined up. Square gates with legs ("like a glass-top side table turned sideways") fixed that in the World Gates pack (v21, EarthStick 1.3.4: "That is the effect. Brilliant."). 1.1 gives your own gates the same look.

Live test (Jim, 2026-11-05): made a Jacksonville <-> Seattle pair (Medium, 1,000 ft above ground), flew to Seattle and back - "my safe return home". Jim then asked for the screen wording to say gate instead of ring before posting.

## What changed

- **Square gates with legs.** Each gate is a gold square facing the approach, sized to fit inside EarthStick's trigger circle (half-side = radius / sqrt 2, so every point inside the square fires), with four gold legs running straight back from the corners. The red back is a square 10 m behind (no legs).
- **Legs grow with the gate:** 1.42 x the trigger radius (Small 71 m, Medium 178 m, Large 320 m - Large matches World Gates v21).
- **Wording:** "Gate size" instead of "Ring size"; sizes now show the square's width (Small 70 m, Medium 180 m, Large 320 m - same trigger sizes as 1.0); the heading line and messages say gate.
- **Self-test:** new checks for the square and four legs, square corners inside the trigger circle, and leg length and direction.

## What did not change

- Everything EarthStick reads (gate name, partner, position, height, size, facing) is identical to 1.0 for the same inputs, so 1.0 and 1.1 gates fly the same.
- Names, eye-alt labels, the near-only display, the safety limits, file names and the Gates folder.
- Gates made with 1.0 keep working; remake them with 1.1 to get the square look (it asks before replacing a file).

## Files

- `releases/World_Gate_Maker_v1.1.zip` (folder `World_Gate_Maker_v1.1/`) SHA-256 `9dd731c0bbc5d9ca6acc19e294a35d95055f09b30af8581b6f4d0b26a2d802e9`
- `gate_maker/World_Gate_Maker.py` SHA-256 `7c018f7aea5e1789791f86429071517e48433ba88f344b116ccd106d0286fbf5`
- 1.0 zip kept for existing links.
