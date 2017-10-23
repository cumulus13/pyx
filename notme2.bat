@echo off

sc stop "Active@ Disk Monitor"
sc stop "LMIGuardianSvc"
sc stop "LogMeIn"
sc stop "LMIMaint"
sc stop "hamachi2svc"
sc stop "FLEXnet Licensing Service"
sc stop bluebirdservice
sc stop fdnetsvc
sc stop fdfusion
sc stop "SyslogODBC"
sc stop freesshdservice
sc stop "DUMeterSvc"
sc stop "OO CleverCache"
taskkill /f /im "diskmonitor.exe"
taskkill /f /im "ooccctrl.exe"
taskkill /f /im "hamachi-2.exe"
taskkill /f /im "DUMeter.exe"
call d:\pyx\hgserver.bat
taskkill /f /im "notifier.exe"
taskkill /f /im netmeter.exe
taskkill /f /im HWinPlus.exe
taskkill /f /im ooccag.exe
taskkill /f /im DUMeterSvc.exe
taskkill /f /im FNPLicensingService.exe
taskkill /f /im MagicDisc.exe
sc start sdnsplus
sc start "Easy File Sharing Web Service"
sc start apache2.2
goto end


:end