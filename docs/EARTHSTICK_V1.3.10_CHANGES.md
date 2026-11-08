# EarthStick 1.3.10 - The trigger drops gates (2026-11-08)

**Jim's request (2026-11-07):** "make the mouse click function button 2, and make the gate dropper button 1" - he flies two-handed (stick in the right hand, regular mouse in the left), so the trigger, the easiest button to reach, should drop gates; clicking objects moves to Button 2. Released at Jim's word on 2026-11-08 ('release 1.3.10'), after the swap had been built as 1.3.7 TEST on 1.3.6.

| Button | 1.3.6 - 1.3.9 | 1.3.10 |
|---|---|---|
| Trigger (Button 1) - press | click the object under the crosshair | **Gate Dropper**: mark a place / drop the pair |
| Trigger (Button 1) - hold 2 s | - | **undo** the last drop (or clear mark 1) |
| Button 2 - press | Gate Dropper | **click the object under the crosshair** |
| Button 2 - hold 2 s | undo | - |

Everything else is 1.3.9: Ready to Fly launcher, one copy at a time, the tractor beam respects mouse moves, flying, gates, Gate Dropper behaviour (only the button moved). Code: `TRIGGER_BUTTON = 2`, `DROP_BUTTON = 1`, startup text, self-test check that the two buttons differ and avoid 3/4.

## Proof

- Self-test PASS.
- Rigs replay / unplugged_at_start / proxy / port_conflict: identical to 1.3.9. Wormhole `--system-files` ALL PASS. Gate Dropper rig with the drop button set to the trigger (bit 0): ALL PASS (mark, drop, map layer, fly-through, hold-to-undo). Mouse rig: 0 of 150 updates pulled back.

## Files

`releases/EarthStick_v1.3.10.zip` SHA-256 `18229d3ebf8c7dbb1c6acf4e080ed50803c75263dd7fc5234c85fcf399c8a4c3` (folder `EarthStick_v1.3.10`, 20 files); `System Files/EarthStick.py` `6720cf690f3f133732bf735f68bca96e6d9da01363ec9bac37f8edf0f4404266`. `gate_dropper.py`, `Ready_To_Fly.ps1`, `Make_Taskbar_Shortcut.bat`, gates and beacons unchanged from 1.3.9.
