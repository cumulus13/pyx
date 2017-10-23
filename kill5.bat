@echo off
title %CD%
if %1*==* goto start
if %1== halt goto halt
IF %1== reboot goto reboot

:start
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
sc config MerakSMTP start= disabled
sc config MerakPOP3 start= disabled
sc config MerakIM start= disabled
sc config MerakCalendar start= disabled
sc config MerakControl start= disabled
sc stop   MerakSMTP 
sc stop   MerakPOP3
sc stop   MerakIM 
sc stop   MerakCalendar
sc stop   MerakControl
echo.
echo			Server has been stop with Fully Function.
echo.
echo			SMTP         = Stop
echo			POP3         = Stop
echo			IM           = Stop
echo			GroupWare    = Stop
echo			Control      = Stop
echo.
sc config MCSMTP start= disabled
sc config MCPOP3 start= disabled
sc stop   MCSMTP 
sc stop   MCPOP3
taskkill /f /im "mcmail.exe"
echo.
echo			Server has been stop with Fully Function.
echo.
echo			SMTP         = Stop
echo			POP3         = Stop
echo.
taskkill /f /im "winamp.exe"
taskkill /f /im "sdnsgui.exe"
taskkill /f /im "sdnsmain.exe"
taskkill /f /im "mysqld.exe"
taskkill /f /im "httpd.exe"
taskkill /f /im "wampmanager.exe"
taskkill /f /im "btwdins.exe"
taskkill /f /im "cbsrv.exe"
taskkill /f /im "srvstart.exe"
taskkill /f /im "wperl.exe"
taskkill /f /im "sbiesvc.exe"
taskkill /f /im "hdsentinel.exe"
taskkill /f /im "unlockerassistant.exe"
taskkill /f /im "trayicon.exe"
taskkill /f /im "snmp.exe"
taskkill /f /im "snmptrap.exe"
taskkill /f /im "wwSecure.exe"
taskkill /f /im "Drives~1.exe"
taskkill /f /im "sbiectrl.exe"
taskkill /f /im "taskswitchxp.exe"
taskkill /f /im "rocketdock.exe"
taskkill /f /im "bttray.exe"
taskkill /f /im "btstac~1.exe"
taskkill /f /im vmware.exe
goto end

:halt
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
taskkill /f /im "winamp.exe"
taskkill /f /im "sdnsgui.exe"
taskkill /f /im "sdnsmain.exe"
taskkill /f /im "mysqld.exe"
taskkill /f /im "httpd.exe"
taskkill /f /im "wampmanager.exe"
taskkill /f /im "btwdins.exe"
taskkill /f /im "cbsrv.exe"
taskkill /f /im "srvstart.exe"
taskkill /f /im "wperl.exe"
taskkill /f /im "sbiesvc.exe"
taskkill /f /im "hdsentinel.exe"
taskkill /f /im "unlockerassistant.exe"
taskkill /f /im "trayicon.exe"
taskkill /f /im "snmp.exe"
taskkill /f /im "snmptrap.exe"
taskkill /f /im "wwSecure.exe"
taskkill /f /im "Drives~1.exe"
taskkill /f /im "sbiectrl.exe"
taskkill /f /im "taskswitchxp.exe"
taskkill /f /im "rocketdock.exe"
taskkill /f /im "bttray.exe"
taskkill /f /im "btstac~1.exe"
taskkill /f /im vmware.exe
sc config MerakSMTP start= disabled
sc config MerakPOP3 start= disabled
sc config MerakIM start= disabled
sc config MerakCalendar start= disabled
sc config MerakControl start= disabled
sc stop   MerakSMTP 
sc stop   MerakPOP3
sc stop   MerakIM 
sc stop   MerakCalendar
sc stop   MerakControl
echo.
echo			Server has been stop with Fully Function.
echo.
echo			SMTP         = Stop
echo			POP3         = Stop
echo			IM           = Stop
echo			GroupWare    = Stop
echo			Control      = Stop
echo.
sc config MCSMTP start= disabled
sc config MCPOP3 start= disabled
sc stop   MCSMTP 
sc stop   MCPOP3
taskkill /f /im "mcmail.exe"
echo.
echo			Server has been stop with Fully Function.
echo.
echo			SMTP         = Stop
echo			POP3         = Stop
echo.
shutdown -s -t 10 -f -c "KOMPUTER AKAN DIMATIKAN DALAM 10 detik LAGI !!!"
goto end

:reboot
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
taskkill /f /im "winamp.exe"
taskkill /f /im "sdnsgui.exe"
taskkill /f /im "sdnsmain.exe"
taskkill /f /im "mysqld.exe"
taskkill /f /im "httpd.exe"
taskkill /f /im "wampmanager.exe"
taskkill /f /im "btwdins.exe"
taskkill /f /im "cbsrv.exe"
taskkill /f /im "srvstart.exe"
taskkill /f /im "wperl.exe"
taskkill /f /im "sbiesvc.exe"
taskkill /f /im "hdsentinel.exe"
taskkill /f /im "unlockerassistant.exe"
taskkill /f /im "trayicon.exe"
taskkill /f /im "snmp.exe"
taskkill /f /im "snmptrap.exe"
taskkill /f /im "wwSecure.exe"
taskkill /f /im "Drives~1.exe"
taskkill /f /im "sbiectrl.exe"
taskkill /f /im "taskswitchxp.exe"
taskkill /f /im "rocketdock.exe"
taskkill /f /im "bttray.exe"
taskkill /f /im "btstac~1.exe"
taskkill /f /im vmware.exe
sc config MerakSMTP start= disabled
sc config MerakPOP3 start= disabled
sc config MerakIM start= disabled
sc config MerakCalendar start= disabled
sc config MerakControl start= disabled
sc stop   MerakSMTP 
sc stop   MerakPOP3
sc stop   MerakIM 
sc stop   MerakCalendar
sc stop   MerakControl
echo.
echo			Server has been stop with Fully Function.
echo.
echo			SMTP         = Stop
echo			POP3         = Stop
echo			IM           = Stop
echo			GroupWare    = Stop
echo			Control      = Stop
echo.
sc config MCSMTP start= disabled
sc config MCPOP3 start= disabled
sc stop   MCSMTP 
sc stop   MCPOP3
taskkill /f /im "mcmail.exe"
echo.
echo			Server has been stop with Fully Function.
echo.
echo			SMTP         = Stop
echo			POP3         = Stop
echo.
shutdown -r -t 10 -f -c "KOMPUTER AKAN DIRESTART DALAM 10 detik LAGI !!!"
goto end


:end