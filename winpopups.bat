@echo off
title %CD%

if %1*==* goto usage

if %1==start goto start
if %1==stop goto stop
if %1==restart goto restart
if %1==status goto status
if %1==client goto client

:start
sc config "winpopup server" start= demand
sc start "winpopup server"
goto end

:stop
sc stop "winpopup server"
sc config "winpopup server" start= disabled
goto end

:restart
sc stop "winpopup server"
sc config "winpopup server" start= disabled
goto start

:status
echo.
echo.
sc query "Winpopup Server"
goto end


:client
Winpopup.py
goto end

:usage
echo.
echo.
echo		Use %0 Start   [Start Service  ]
echo		    %0 Stop    [Stop Service   ]
echo		    %0 Restart [Restart Service]
echo		    %0 Status  [Status Service ]
echo		    %0 Client  [Start Client   ]
echo.
echo.
goto end

:end
