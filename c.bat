@echo off
title %CD%
if %1*==* goto help
if %1== c goto blackid
if %1== i goto id
if %1== b goto black
if %1== y goto yellow
if %1== yb goto yellowwhite
goto end

:yellow
color E
goto end

:yellowwhite
color 1E
goto end

:black
color F8
goto end


:blackid
color A
goto end

:id
color F0
goto end

:help
echo.
echo.
echo              use c c == background blackid [Green  in Black]
echo                  c i == default color [Blackid in White]
echo                  c b == default color [White in Black]
echo.
echo              press any key for continue . . . . . . . . .  ^^
pause >> nul
goto end

:end
cls
echo.
echo.
echo.

