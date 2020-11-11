@echo off
title %CD%
if %1*==* goto usage
if %1==start goto start
if %1==enable goto enable
if %1==stop goto stopx
if %1==auto goto auto
if %1==run goto run
goto end

:run
if EXIST "c:\Program Files\VMware\VMware Workstation\vmware.exe" (
	"c:\Program Files\VMware\VMware Workstation\vmware.exe"
) else (
	"c:\Program Files (x86)\VMware\VMware Workstation\vmware.exe"
)
goto end

:auto
sc config  VMAuthdService start= auto
sc config  VMnetDHCP start= auto
sc config  "VMware NAT Service" start= auto
goto end

:start
if %2*==* goto startx
if %2==net goto net1
goto end

:enable
sc config  VMAuthdService start= demand
sc config  VMnetDHCP start= demand
sc config  "VMware NAT Service" start= demand
goto end


:startx
rem sc config  VMAuthdService start= demand
rem sc config  VMnetDHCP start= demand
rem sc config  "VMware NAT Service" start= demand

sc config VMAuthdService start= demand
sc config VMnetDHCP start= demand
sc config "VMware NAT Service" start= demand

net start VMAuthdService
net start VMnetDHCP
net start  "VMware NAT Service"
start /B /D "c:\Program Files (x86)\VMware\VMware Workstation" vmware.exe
echo.
echo.
echo      VMAuthdService          =  Start
echo      VMnetDHCP               =  Start
echo      VMware NAT Service      =  Start
echo.
rem vmwarex.py
goto end

:net1
sc config  VMAuthdService start= demand
sc config  VMnetDHCP start= demand
sc config  "VMware NAT Service" start= demand

net start VMAuthdService
net start VMnetDHCP
net start  "VMware NAT Service"
echo.
echo.
echo      VMAuthdService          =  Start
echo      VMnetDHCP               =  Start
echo      VMware NAT Service      =  Start
echo.
goto end

:stopx
rem if %2==net goto net2
sc config  VMAuthdService start= disabled
sc config  VMnetDHCP start= disabled
sc config  "VMware NAT Service" start= disabled

net stop VMAuthdService
net stop VMnetDHCP
net stop  "VMware NAT Service"
echo.
echo.
echo      VMAuthdService          =  Stop
echo      VMnetDHCP               =  Stop
echo      VMware NAT Service      =  Stop
echo.
taskkill /f /im vmware.exe
goto end

:net2
sc config  VMAuthdService start= disabled
sc config  VMnetDHCP start= disabled
sc config  "VMware NAT Service" start= disabled

net stop VMAuthdService
net stop VMnetDHCP
net stop  "VMware NAT Service"
echo.
echo.
echo      VMAuthdService          =  Stop
echo      VMnetDHCP               =  Stop
echo      VMware NAT Service      =  Stop
echo.
goto end

:usage
echo.
echo.
echo			Usage : %0 Start [ to Start service and Vmware]
echo		                %0 Stop   [ to Stop service and Vmware]
echo		                %0 Run    [ Run Vmware only]
echo		                %0 Enable [ Enable Vmware]
echo.
echo.
goto end
















:end
rem vmwarex.py
