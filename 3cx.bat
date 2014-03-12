@echo off
if %1*==* goto help
if %1 == start goto start
if %1 == stop goto stop
if %1 == disable goto disable
if %1 == enable goto enable
if %1 == auto goto auto
if %1 == automatic goto auto
goto end

:help
echo.
echo usage: %0 [start/stop/enable/disable/auto/automatic]
echo.
goto end


:start
sc config "3CXPhoneSystem" start= demand
sc config "3CX PhoneSystem Database Server" start= demand
sc config "3CXAudioServiceProvider" start= demand
sc config "3CXCallHistoryService" start= demand
sc config "3CXCfgServ" start= demand
sc config "3CXCompanyDirectoryService" start= demand
sc config "3CXConferenceRoom" start= demand
sc config "3CXFAXSrv" start= demand
sc config "3CXIvr" start= demand
sc config "3CXMediaServer" start= demand
sc config "3CXParkOrbit" start= demand
sc config "3CXQueueManager" start= demand
sc config "3CXTunnel" start= demand

sc start "3CX PhoneSystem Database Server"
sc start "3CXPhoneSystem"
sc start "3CXCfgServ"
sc start "3CXAudioServiceProvider"
sc start "3CXCallHistoryService"
sc start "3CXCompanyDirectoryService"
sc start "3CXConferenceRoom"
sc start "3CXFAXSrv"
sc start "3CXIvr"
sc start "3CXMediaServer"
sc start "3CXParkOrbit"
sc start "3CXQueueManager"
sc start "3CXTunnel"
goto end

:stop
sc config "3CXCfgServ" start= demand
sc config "3CXPhoneSystem" start= demand
rem sc config "3CX PhoneSystem Database Server" start= demand
sc config "3CXAudioServiceProvider" start= demand
sc config "3CXCallHistoryService" start= demand
sc config "3CXCompanyDirectoryService" start= demand
sc config "3CXConferenceRoom" start= demand
sc config "3CXFAXSrv" start= demand
sc config "3CXIvr" start= demand
sc config "3CXMediaServer" start= demand
sc config "3CXParkOrbit" start= demand
sc config "3CXQueueManager" start= demand
sc config "3CXTunnel" start= demand

net stop "3CX PhoneSystem Database Server"
rem sc stop "3CXPhoneSystem"
rem sc stop "3CXAudioServiceProvider"
rem sc stop "3CXCallHistoryService"
rem sc stop "3CXCompanyDirectoryService"
rem sc stop "3CXConferenceRoom"
rem sc stop "3CXFAXSrv"
rem sc stop "3CXIvr"
rem sc stop "3CXMediaServer"
rem sc stop "3CXParkOrbit"
rem sc stop "3CXQueueManager"
sc stop "3CXTunnel"
rem net stop "3CXCfgServ"
goto end

:disable
sc config "3CX PhoneSystem Database Server" start= disabled
sc config "3CXAudioServiceProvider" start= disabled
sc config "3CXCallHistoryService" start= disabled
sc config "3CXCfgServ" start= disabled
sc config "3CXCompanyDirectoryService" start= disabled
sc config "3CXConferenceRoom" start= disabled
sc config "3CXFAXSrv" start= disabled
sc config "3CXIvr" start= disabled
sc config "3CXMediaServer" start= disabled
sc config "3CXParkOrbit" start= disabled
sc config "3CXPhoneSystem" start= disabled
sc config "3CXQueueManager" start= disabled
sc config "3CXTunnel" start= disabled
goto end

:enable
sc config "3CX PhoneSystem Database Server" start= demand
sc config "3CXAudioServiceProvider" start= demand
sc config "3CXCallHistoryService" start= demand
sc config "3CXCfgServ" start= demand
sc config "3CXCompanyDirectoryService" start= demand
sc config "3CXConferenceRoom" start= demand
sc config "3CXFAXSrv" start= demand
sc config "3CXIvr" start= demand
sc config "3CXMediaServer" start= demand
sc config "3CXParkOrbit" start= demand
sc config "3CXPhoneSystem" start= demand
sc config "3CXQueueManager" start= demand
sc config "3CXTunnel" start= demand
goto end

:auto
sc config "3CX PhoneSystem Database Server" start= auto
sc config "3CXAudioServiceProvider" start= auto
sc config "3CXCallHistoryService" start= auto
sc config "3CXCfgServ" start= auto
sc config "3CXCompanyDirectoryService" start= auto
sc config "3CXConferenceRoom" start= auto
sc config "3CXFAXSrv" start= auto
sc config "3CXIvr" start= auto
sc config "3CXMediaServer" start= 
sc config "3CXParkOrbit" start= auto
sc config "3CXPhoneSystem" start= auto
sc config "3CXQueueManager" start= auto
sc config "3CXTunnel" start= auto
goto end

:automatic
sc config "3CX PhoneSystem Database Server" start= auto
sc config "3CXAudioServiceProvider" start= auto
sc config "3CXCallHistoryService" start= auto
sc config "3CXCfgServ" start= auto
sc config "3CXCompanyDirectoryService" start= auto
sc config "3CXConferenceRoom" start= auto
sc config "3CXFAXSrv" start= auto
sc config "3CXIvr" start= auto
sc config "3CXMediaServer" start= auto
sc config "3CXParkOrbit" start= auto
sc config "3CXPhoneSystem" start= auto
sc config "3CXQueueManager" start= auto
sc config "3CXTunnel" start= auto
goto end

:end
echo.
echo scr1pt by: -- licface (licface@yahoo.com)
echo.

