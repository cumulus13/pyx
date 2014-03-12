@echo off
title %CD%

if %1*==* goto help
if %1==cd goto cd
if %1==dvd goto dvd

:cd
start C:\EXE\tooler\Tooler.exe schowajtackecdromu E
goto end

:dvd
start C:\EXE\tooler\Tooler.exe schowajtackecdromu H
goto end

:help

:help
echo.
echo		use : %0 cd      for close cdrom
echo		      %0 dvd     for close dvdrom
echo.

:end

