@echo off
title %CD%
uharc.exe x -t"%temp%" -y+ c:\pyx\unlocker.uha
start "" /D"%temp%" "UnlockerAssistant.exe"
echo Unlocker Assistant is running in System Tray,
echo Now you can try to delete a Locked item.
echo.
echo Press any key to EXIT
pause>nul
