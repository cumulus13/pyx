@echo off
title %CD%
if %1*==* goto help
if %1== g goto blackid
if %1== bw goto id
if %1== w goto white
if %1== y goto yellow
if %1== b goto blue
if %1== r goto red
if %1== yb goto yellowwhite
goto end

:yellow
color E
goto end

:blue
color 0B
goto end

:yellowwhite
color 1E
goto end

:black
color F8
goto end

:white
color 07
goto end

:blackid
color A
goto end

:id
color F0
goto end

:red
color 04
goto end

:help
echo.
echo.
echo              use c g == background blackid [Green  in Black]
echo                  c bw == default color [Black in White]
echo                  c w == default color [White in Black]
echo                  c y == default color [Yellow in Black]
echo                  c yb == default color [Yellow in Blue]
echo                  c b == default color [Blue in Black]
echo                  c r == default color [Red in Black]

echo.
rem echo              press any key for continue . . . . . . . . .  ^^
rem pause >> nul
goto end

:end
rem cls
echo.
echo.
echo.

