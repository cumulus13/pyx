@echo off

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
taskkill /f /im "DUMeterSvc.exe"
taskkill /f /im "FireDaemon.exe"
call d:\pyx\hgserver.bat
sc start "Easy File Sharing Web Service"
taskkill /f /im "notifier.exe"
sc stop "FLEXnet Licensing Service"
sc stop bluebirdservice
sc stop fdnetsvc
sc stop fdfusion
sc stop "SyslogODBC"
taskkill /f /im netmeter.exe
sc start apache2.2
sc start sdnsplus
goto end


:end