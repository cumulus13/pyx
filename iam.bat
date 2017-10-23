@echo off
title %CD%
if %1*==* goto usage
if %1== --not-connection goto nc
if %1== --connection goto cn
if %1== --server-start goto ss
if %1== --server-stop goto sst
if %1== --server-status goto stu
goto end


:nc
processx -k bttray.exe
cls
processx -k winexpose.exe
cls
processx -k diskmonitor.exe
cls
processx -k netmeter.exe
cls
processx -k netspeed.exe
cls
processx -k borderskin.exe
cls
processx -k idman.exe
cls
processx -k ProxySwitcher.exe
cls
processx -k iemonitor.exe
cls
processx -k notifier.exe
cls
processx -k messageservicemonitor.exe
cls
sc stop "Active@ Disk Monitor"
taskkill /f /im "diskmonitor.exe"
sc stop "OO CleverCache"
taskkill /f /im "ooccctrl.exe"
sc stop "LMIGuardianSvc"
sc stop "LogMeIn"
sc stop "LMIMaint"
sc stop "hamachi2svc"
taskkill /f /im "hamachi-2.exe"
sc stop "DUMeterSvc"
taskkill /f /im "DUMeter.exe"
sc start apache2.2
sc start sdnsplus
call d:\pyx\hgserver.bat
sc start "Easy File Sharing Web Service"
cls

goto end

:ss
apache start & visualsvn  start & svnserver start & ews start & simpledns start & nasweb & call d:\pyx\mercurialserver.bat
goto end

:sst
apache stop & visualsvn  stop & svnserver stop & ews stop & simpledns stop & processx -k NetworkActivWebServerV3.5.exe & processx -k thg.exe
goto end

:stu
apache status & visualsvn status & svnserver status & ews status & simpledns status & process NetworkActivWebServer
goto end

:usage
echo.
echo.
echo     use : %0 --not-connection
echo               --connection
echo               --server-start
echo               --server-stop
echo               --server-status
echo.
echo.
goto end

:end
