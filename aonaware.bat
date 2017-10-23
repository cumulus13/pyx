@echo off
title %CD%
if %1*==* goto usage
if %1== start goto start
if %1== stop goto stop
if %1== restart goto restart
if %1== status goto status
goto end

:start
sc start "Aonaware Syslog Daemon"
goto end

:stop
sc stop "Aonaware Syslog Daemon"
goto end

:restart 
sc stop "Aonaware Syslog Daemon"
goto start

:status
sc query "Aonaware Syslog Daemon"
goto end

:usage
cls
echo.
echo.
echo      use : %0 [Start /Stop /Restart /Status]
echo.
goto end


:end
