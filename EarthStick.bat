@echo off
cd /d "%~dp0"
title EarthStick 1.0
where py >nul 2>&1
if %errorlevel%==0 (
    py -3 EarthStick.py
) else (
    python EarthStick.py
)
pause
