# World Gate Maker 1.2 - One obvious file (2026-11-06)

## Why

Jim's packaging rule for every tool: *one obvious .bat file to click, and everything else under a system folder.*

## What changed

- After Extract All the folder holds just `World_Gate_Maker.bat` and `System Files` (with `World_Gate_Maker.py` inside). The saved-settings file it makes now lands in System Files too.
- Finding EarthStick's Gates folder: World Gate Maker now also looks one folder higher (it lives one level deeper) and prefers the **newest** `EarthStick...` folder when several sit side by side - for example `Downloads\EarthStick_v1.3.5\Gates` next to `Downloads\World_Gate_Maker_v1.2`. Your own choice of folder is still remembered.
- Wording: "EarthStick only reads the Gates folder in the EarthStick folder" (EarthStick 1.3.5 keeps its program in System Files).
- Version text 1.2.

## What did not change

The gates themselves: same file, same look, same data as 1.1. Self-test: All checks passed.

## Files

- `archive/World_Gate_Maker_v1.2.zip` (folder `World_Gate_Maker_v1.2/`) SHA-256 `d06c88152c40f6d08b3df382948cebb0dbe1962cf1572be79c4c655e7e03549f`
- `gate_maker/System Files/World_Gate_Maker.py` SHA-256 `27041036557ae970de68fec4bed95c485f31c39db8aa9043ba00647cc4c14743`
- 1.0 and 1.1 zips kept for existing links.
