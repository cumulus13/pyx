@echo off
title %CD%
cls
echo.
echo.
echo.

title iHarga - Ruby On Rails
set me=%cd%

if %1*==* goto usage
if %1==start goto start
if %1==stop goto stop
if %1==restart goto restart
if %1==direct goto redirect
if %1==redirect goto redirect
if %1==status goto status
goto end

:start
net start iharga
goto end

:stop 
net stop iharga
goto end

:restart
net stop iharga
net start iharga
goto end


:status
sc query iharga
goto end

:redirect
cd /d E:\InstantRails-2.0-win\rails_apps\iHarga
E:\InstantRails-2.0-win\ruby\bin\ruby.exe script\server
goto end

:usage
echo.
echo.
echo		use : %0 Start / Stop / Restart / direct / redirect 
echo.
echo.
goto end


:end
cd /d %me%

