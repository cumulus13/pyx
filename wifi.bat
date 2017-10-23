echo off

if %1*==* goto usage
if %1==restart goto restart
rem if %2*==* goto restart1
goto end

:restart
if %2==--hard goto restart2
	netsh wlan disconnect wi-fi
	netsh wlan connect %2 %2 %3
goto end

:restart2
	netsh interface set interface name="wi-fi" admin=DISABLED
	netsh interface set interface name="wi-fi" admin=ENABLED
	netsh wlan connect %3 %3 %4
goto end

rem :restart1
rem netsh wlan disconnect wi-fi
rem netsh wlan connect ROUTER ROUTER wi-fi
rem goto end

:usage
echo
echo usage: %0 restart [--hard/--soft] SSID DEV  
echo           --hardr  estart hard, disable enable then connecting
echo           --soft  restart soft, disconnect then connecting
echo.
goto end

:end

