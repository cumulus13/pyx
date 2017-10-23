@echo off
title %CD%

if %1*==* goto nol
if %1==start goto start
if %1==stop goto stop


:start
"C:\Program Files\Simple DNS Plus\sdnsplus.exe"
"C:\Program Files\MagikInfo Inc\MagikDHCP Server\DHCP.exe"
"e:\wamp\wampmanager.exe"
goto end

:nol
echo.
echo.
echo		usage : %0 start  [to start server] [default]
echo		        %0 stop   [to stop server]
echo.
echo.
goto start

:stop
taskkill /f /im sdnsplus.exe

taskkill /f /im DHCP.exe

taskkill /f /im wampmanager.exe

goto end


:end

