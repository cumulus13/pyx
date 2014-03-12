@echo off
title %CD%

if %1*==* goto help
if %1==cd goto cd
if %1==dvd goto dvd

:dvd
start C:\EXE\tooler\Tooler.exe wysuntackecdromu H
goto end

:cd
start C:\EXE\tooler\Tooler.exe wysuntacLecdromu E
goto end

:help
echo.
echo		use : %0 cd      for eject cdrom
echo		      %0 dvd     for eject dvdrom
echo.


:end

