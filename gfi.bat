@echo off
title %CD%
if %1*==* goto usage
if %1== help goto usage
if %1== start goto start
if %1== stop goto stop
if %1== status goto status
if %1== restart goto restart

goto end


:start 
sc start "EventsManager Processor Agent Service"
goto end


:stop
sc stop "EventsManager Processor Agent Service"
goto end

:restart
sc stop "EventsManager Processor Agent Service"
goto start

:status
sc query "EventsManager Processor Agent Service"
goto end


:usage
cls
echo.
echo.
echo       use : %0 [start /stop /restart /status]
echo.
goto end

:end





