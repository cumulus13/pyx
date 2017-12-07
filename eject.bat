@echo off
title %CD%

rem if %1*==* goto help
rem if %1==cd goto cd
rem if %1==dvd goto dvd

rem :dvd
start C:\TOOLS\exe\Tooler.exe wysuntackecdromu %1
rem goto end

rem :cd
rem start C:\exe\Tooler.exe wysuntacLecdromu H
rem goto end

rem :help
rem echo.
rem echo		use : %0 cd      for eject cdrom
rem echo		      %0 dvd     for eject dvdrom
rem echo.


rem :end

