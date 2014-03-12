@echo off
title %CD%

if %1*==* goto usage
if %1==start goto start
if %1==stop goto stop
if %1==restart goto restart
if %1==disable goto disable
if %1==enable goto enable
if %1==status goto status


:start
sc config PRTG7CoreService start= demand
sc config PRTG7ProbeService start= demand
sc start PRTG7CoreService
sc start PRTG7ProbeService
goto end

:stop
sc stop PRTG7CoreService
sc stop PRTG7ProbeService
sc config PRTG7CoreService start= disabled
sc config PRTG7ProbeService start= disabled
goto end

:restart
sc start PRTG7CoreService
sc start PRTG7ProbeService
goto start

:enable
sc config PRTG7CoreService start= demand
sc config PRTG7ProbeService start= demand
goto end

:disable
sc config PRTG7CoreService start= disabled
sc config PRTG7ProbeService start= disabled
goto end

:status 
sc query PRTG7CoreService 
sc query PRTG7ProbeService
goto end


:usage
echo.
echo.
echo		use : %0 start		[Start Service  ]
echo.
echo		      %0 stop			[Stop Service   ]
echo.
echo		      %0 restart        	[Restart Service]
echo.
echo		      %0 enable		[Enable All Service if it Disabled]
echo.
echo		      %0 disable		[Disable All Service]
echo.
echo		      %0 status		[Show Status Service]
echo.
goto end


:end


