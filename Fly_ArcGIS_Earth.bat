@echo off
rem ArcGIS Earth Flight launcher v1.1 (Jim, 2026-11-03; v1.1 2026-11-06: EarthStick.bat and the remembered
rem ArcGIS Earth path live in System Files): starts ArcGIS Earth, then EarthStick.
rem Keep this file in the EarthStick folder, next to System Files. EarthStick waits for ArcGIS Earth by itself.
rem No ( ) blocks around paths on purpose: a path like "Program Files (x86)" would break them.
setlocal
title ArcGIS Earth Flight launcher v1.1
cd /d "%~dp0"
call :find_earth
if not defined AE goto :not_found
if /i "%~1"=="/find" exit /b 0

tasklist /fi "imagename eq %AE_NAME%" 2>nul | find /i "%AE_NAME%" >nul
if not errorlevel 1 goto :earth_running
echo Starting ArcGIS Earth...
start "" "%AE%"
goto :start_stick
:earth_running
echo ArcGIS Earth is already running.

:start_stick
if not exist "%~dp0System Files\EarthStick.bat" goto :no_stick
echo Starting EarthStick - it waits until ArcGIS Earth is ready...
call "%~dp0System Files\EarthStick.bat"
exit /b 0

:no_stick
echo.
echo EarthStick.bat was not found in:
echo   "%~dp0System Files"
echo Keep Fly_ArcGIS_Earth.bat in the EarthStick folder, next to System Files.
pause
exit /b 1

:find_earth
set "AE="
set "AE_NAME="
if exist "%~dp0System Files\ArcGIS_Earth_path.txt" set /p AE=<"%~dp0System Files\ArcGIS_Earth_path.txt"
if defined AE if not exist "%AE%" set "AE="
if not defined AE for %%P in ("%ProgramFiles%\ArcGIS\Earth\ArcGISEarth.exe" "%ProgramFiles%\ArcGIS Earth\ArcGISEarth.exe" "%LOCALAPPDATA%\Programs\ArcGIS\Earth\ArcGISEarth.exe" "%LOCALAPPDATA%\ArcGIS\Earth\ArcGISEarth.exe") do if not defined AE if exist "%%~P" set "AE=%%~P"
if not defined AE echo Looking for ArcGIS Earth - first time only, this can take a minute...
if not defined AE for %%R in ("%ProgramFiles%" "%LOCALAPPDATA%" "%ProgramFiles(x86)%") do if not defined AE if exist "%%~R" for /f "delims=" %%F in ('where /r "%%~R" ArcGISEarth.exe 2^>nul') do if not defined AE set "AE=%%F"
rem second pass: any ArcGISEarth*.exe that is not an updater/uninstaller
if not defined AE for %%R in ("%ProgramFiles%" "%LOCALAPPDATA%" "%ProgramFiles(x86)%") do if not defined AE if exist "%%~R" for /f "delims=" %%F in ('where /r "%%~R" ArcGISEarth*.exe 2^>nul ^| findstr /i /v "update uninst setup install"') do if not defined AE set "AE=%%F"
if not defined AE exit /b 0
>"%~dp0System Files\ArcGIS_Earth_path.txt" echo %AE%
for %%N in ("%AE%") do set "AE_NAME=%%~nxN"
echo ArcGIS Earth: "%AE%"
exit /b 0

:not_found
echo.
echo Could not find ArcGIS Earth on this computer.
echo Fix: right-click your ArcGIS Earth shortcut, choose Properties, copy the Target
echo (it ends in .exe), and paste it as the only line of a text file named
echo   ArcGIS_Earth_path.txt
echo in this folder:
echo   "%~dp0System Files"
echo then run this again.
pause
exit /b 1
