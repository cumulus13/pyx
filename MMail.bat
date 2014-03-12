@echo off
title %CD%
echo.
echo                ###############################################################
echo                #               Macallan Email Server Control                 #
echo                #                         Scr1pt by                           #
echo                #                          BL4CK1D                            #
echo                #                                                             #
echo                ###############################################################
echo.


if %1*==* goto usage
if %1==start goto start
if %1==stop goto stop
if %1==restart goto restart
if %1==nomail goto nomail
if %1==withmail goto withmail
if %1==control goto control
if %1==help goto usage
if %1==h goto usage
if %1==-h goto usage
if %1==-help goto usage
if %1==--h goto usage
if %1==--help goto usage
if %1==status goto status
if %1==quick goto quick


:start
sc config MCSMTP start= demand
sc config MCPOP3 start= demand
sc start  MCSMTP 
sc start  MCPOP3
cls
echo.
echo			Server has been start with Fully Function.
echo.
echo			SMTP         = Start
echo			POP3         = Start
echo.
goto end

:stop
sc config MCSMTP start= disabled
sc config MCPOP3 start= disabled
sc stop   MCSMTP 
sc stop   MCPOP3
taskkill /f /im "mcmail.exe"
cls
echo.
echo			Server has been stop with Fully Function.
echo.
echo			SMTP         = Stop
echo			POP3         = Stop
echo.
goto end

:restart
sc config MCSMTP start= disabled
sc config MCPOP3 start= disabled
sc stop   MCSMTP 
sc stop   MCPOP3
cls
sc config MCSMTP start= demand
sc config MCPOP3 start= demand
sc start  MCSMTP 
sc start  MCPOP3
echo.
echo			Server has been restart with Fully Function.
echo.
echo			SMTP         = Restart
echo			POP3         = Restart
echo.
goto start


:NOMail
sc config MCSMTP start= disabled
sc config MCPOP3 start= disabled
sc stop   MCSMTP 
sc stop   MCPOP3
cls
echo.
echo			Server has been start with No Mail Service Function.
echo.
echo			SMTP         = Stop
echo			POP3         = Stop
echo.
goto end

:WithMail
sc config MCSMTP start= demand
sc config MCPOP3 start= demand
sc start  MCSMTP 
sc start  MCPOP3

cls
echo.
echo			Server has been start with Only Mail Service Function.
echo.
echo			SMTP         = Start
echo			POP3         = Start
echo.
goto end

:control
MCMail.py
goto end

:quick
MCMailw.py
cls
goto end

:auto
:restart
sc config MCSMTP start= auto
sc config MCPOP3 start= auto
goto end


:usage
echo.
echo			Usage : %0 start    	     [Start Mail Service]
echo		        	%0 stop     	     [Stop Mail Service]
echo			        %0 restart  	     [Restart Mail Service]
echo		        	%0 status     	     [Status Service]
echo			        %0 WithMail        [Service Will Autostart on Window StartUp]
echo			        %0 Quick       [Start With Quick Start Dashboard]
echo.
goto fin

:status
sc query MCSMTP 
sc query MCPOP3
goto end

:end
echo.
echo                ###############################################################
echo                #               Macallan Email Server Control                 #
echo                #                         Scr1pt by                           #
echo                #                          BL4CK1D                            #
echo                #                                                             #
echo                ###############################################################
echo.
goto fin

:fin
