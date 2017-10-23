@echo off
title %CD%
echo.
echo                ###############################################################
echo                #            IceWrap Merak Email Server Control               #
echo                #                         Scr1pt by                           #
echo                #                          BL4CK1D                            #
echo                #                                                             #
echo                ###############################################################
echo.


if %1*==* goto usage
if %1==start goto start
if %1==stop goto stop
if %1==restart goto restart
if %1==auto goto auto
if %1==noim goto noim
if %1==nogroupware goto nogroupware
if %1==nomail goto nomail
if %1==withim goto withim
if %1==withgroupware goto withgroupware
if %1==withmail goto withmail
if %1==control goto control
if %1==help goto usage
if %1==h goto usage
if %1==-h goto usage
if %1==-help goto usage
if %1==--h goto usage
if %1==--help goto usage
if %1==status goto status


:auto
sc config MerakSMTP start= auto
sc config MerakPOP3 start= auto
sc config MerakIM start= auto
sc config MerakCalendar start= auto
sc config MerakControl start= auto
goto end

:start
sc config MerakSMTP start= demand
sc config MerakPOP3 start= demand
sc config MerakIM start= demand
sc config MerakCalendar start= demand
sc config MerakControl start= demand
sc start  MerakSMTP 
sc start  MerakPOP3
sc start  MerakIM 
sc start  MerakCalendar
sc start  MerakControl
cls
echo.
echo			Server has been start with Fully Function.
echo.
echo			SMTP         = Start
echo			POP3         = Start
echo			IM           = Start
echo			GroupWare    = Start
echo			Control      = Start
echo.
goto end

:stop
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
cls
echo.
echo			Server has been stop with Fully Function.
echo.
echo			SMTP         = Stop
echo			POP3         = Stop
echo			IM           = Stop
echo			GroupWare    = Stop
echo			Control      = Stop
echo.
goto end

:restart
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
cls
sc config MerakSMTP start= demand
sc config MerakPOP3 start= demand
sc config MerakIM start= demand
sc config MerakCalendar start= demand
sc config MerakControl start= demand
sc start  MerakSMTP 
sc start  MerakPOP3
sc start  MerakIM 
sc start  MerakCalendar
sc start  MerakControl
echo.
echo			Server has been restart with Fully Function.
echo.
echo			SMTP         = Restart
echo			POP3         = Restart
echo			IM           = Restart
echo			GroupWare    = Restart
echo			Control      = Restart
echo.
goto start

:NOIM
sc config MerakSMTP start= demand
sc config MerakPOP3 start= demand
sc config MerakIM start= disabled
sc config MerakCalendar start= demand
sc config MerakControl start= demand
sc start  MerakSMTP 
sc start  MerakPOP3
sc stop   MerakIM 
sc start  MerakCalendar
sc start  MerakControl
cls
echo.
echo			Server has been start with No IM Service Function.
echo.
echo			SMTP         = Start
echo			POP3         = Start
echo			IM           = Stop
echo			GroupWare    = Start
echo			Control      = Start
echo.
goto end

:NOGroupWare
sc config MerakSMTP start= demand
sc config MerakPOP3 start= demand
sc config MerakIM start= demand
sc config MerakCalendar start= disabled
sc config MerakControl start= demand
sc start  MerakSMTP 
sc start  MerakPOP3
sc start  MerakIM 
sc stop   MerakCalendar
sc start  MerakControl
cls
echo.
echo			Server has been start with No GroupWare Service Function.
echo.
echo			SMTP         = Start
echo			POP3         = Start
echo			IM           = Start
echo			GroupWare    = Stop
echo			Control      = Start
echo.
goto end

:NOMail
sc config MerakSMTP start= disabled
sc config MerakPOP3 start= disabled
sc config MerakIM start= demand
sc config MerakCalendar start= demand
sc config MerakControl start= disabled
sc stop   MerakSMTP 
sc stop   MerakPOP3
sc start  MerakIM 
sc start  MerakCalendar
sc stop   MerakControl
cls
echo.
echo			Server has been start with No Mail Service Function.
echo.
echo			SMTP         = Stop
echo			POP3         = Stop
echo			IM           = Start
echo			GroupWare    = Start
echo			Control      = Stop
echo.
goto end

:WithIM
sc config MerakSMTP start= disabled
sc config MerakPOP3 start= disabled
sc config MerakIM start= demand
sc config MerakCalendar start= disabled
sc config MerakControl start= disabled
sc stop   MerakSMTP 
sc stop   MerakPOP3
sc start  MerakIM 
sc stop   MerakCalendar
sc stop   MerakControl
cls
echo.
echo			Server has been start with Only IM Service Function.
echo.
echo			SMTP         = Stop
echo			POP3         = Stop
echo			IM           = Start
echo			GroupWare    = Stop
echo			Control      = Stop
echo.
goto end

:WithGroupWare
sc config MerakSMTP start= disabled
sc config MerakPOP3 start= disabled
sc config MerakIM start= disabled
sc config MerakCalendar start= demand
sc config MerakControl start= disabled
sc stop   MerakSMTP 
sc stop   MerakPOP3
sc stop   MerakIM 
sc start  MerakCalendar
sc stop   MerakControl
cls
echo.
echo			Server has been start with Only GroupWare Service Function.
echo.
echo			SMTP         = Stop
echo			POP3         = Stop
echo			IM           = Stop
echo			GroupWare    = Start
echo			Control      = Stop
echo.
goto end

:WithMail
if %2*==* goto WithMail2
if %2== --nocontrol goto WithMailnocontrol
sc config MerakSMTP start= demand
sc config MerakPOP3 start= demand
sc config MerakIM start= disabled
sc config MerakCalendar start= disabled
sc config MerakControl start= demand
sc start  MerakSMTP 
sc start  MerakPOP3
sc stop   MerakIM 
sc stop   MerakCalendar
sc start  MerakControl
cls
echo.
echo			Server has been start with Only Mail Service Function.
echo.
echo			SMTP         = Start
echo			POP3         = Start
echo			IM           = Stop
echo			GroupWare    = Stop
echo			Control      = Start
echo.
goto end

:WithMail2
sc config MerakSMTP start= demand
sc config MerakPOP3 start= demand
sc config MerakIM start= disabled
sc config MerakCalendar start= disabled
sc config MerakControl start= demand
sc start  MerakSMTP 
sc start  MerakPOP3
sc stop   MerakIM 
sc stop   MerakCalendar
sc start  MerakControl
cls
echo.
echo			Server has been start with Only Mail Service Function.
echo.
echo			SMTP         = Start
echo			POP3         = Start
echo			IM           = Stop
echo			GroupWare    = Stop
echo			Control      = Start
echo.
goto end

:WithMailnocontrol
sc config MerakSMTP start= demand
sc config MerakPOP3 start= demand
sc config MerakIM start= disabled
sc config MerakCalendar start= disabled
sc config MerakControl start= demand
sc start  MerakSMTP 
sc start  MerakPOP3
sc stop   MerakIM 
sc stop   MerakCalendar
sc stop MerakControl
cls
echo.
echo			Server has been start with Only Mail Service Function.
echo.
echo			SMTP         = Start
echo			POP3         = Start
echo			IM           = Stop
echo			GroupWare    = Stop
echo			Control      = Stop
echo.
goto end

:control
merakcntl.py
cls
goto end


:usage
echo.
echo			Usage : %0 start    	     [Start All Service]
echo		        	%0 stop     	     [Stop All Service]
echo			        %0 restart  	     [Restart All Service]
echo		        	%0 status     	     [Status All Service]
echo			        %0 noim     	     [Start Service but No IM Service]
echo			        %0 nogroupWare      [Start Service but No GroupWareService]
echo			        %0 nomail           [Start Service but No Mail Service]
echo			        %0 withim           [Only IM Service tobe Start]
echo			        %0 withgroupWare    [Only IM Service tobe Start]
echo			        %0 withmail         [Only IM Service tobe Start]
echo.
goto fin

:status
sc query MerakSMTP 
sc query MerakPOP3
sc query MerakIM
sc query MerakCalendar 
sc query MerakControl 
goto end

:end
echo.
echo                ###############################################################
echo                #            IceWrap Merak Email Server Control               #
echo                #                         Scr1pt by                           #
echo                #                          BL4CK1D                            #
echo                #                                                             #
echo                ###############################################################
echo.
goto fin

:fin
