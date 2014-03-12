@echo off
title %CD%
if %1*==* goto usage
if %1== usb goto usb
if %1== mydocument goto mydocument


:usb
copy  %2 p:\%3
if %3=="" goto usb2
goto end

:usb2
copy  %2 p:\
goto end

:mydocument
copy %2 "g:\Documents and Settings\Administrator\My Documents"
goto end

:usage
echo.
echo.
echo        use: %0 USB        [Copy Data to USB Device]
echo             %0 mydocument [Copy Data to MyDocument Data]
echo.
echo.
goto end

:end

