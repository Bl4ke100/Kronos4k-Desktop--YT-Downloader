@echo off
title KRONOS 4K - Application Builder
cd /d "%~dp0"

echo ============================================================
echo            KRONOS 4K - DESKTOP BUILDER
echo ============================================================
echo.
echo Choose your build mode:
echo   [1] Fast Directory Mode (RECOMMENDED - Instant ~1s Launch)
echo   [2] Single-File EXE Mode (Standalone Kronos4K.exe)
echo.
set /p choice="Select an option (1 or 2, default is 1): "

if "%choice%"=="2" (
    echo.
    echo Building Standalone Single EXE...
    python build_exe.py --mode onefile
) else (
    echo.
    echo Building Fast Desktop Directory Bundle...
    python build_exe.py --mode onedir
)

echo.
pause
