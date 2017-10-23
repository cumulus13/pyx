@echo off
title %CD%
echo.
echo                ###############################################################
echo                #                 PostgreSQL Service Control                  #
echo                #                         Scr1pt by                           #
echo                #                          BL4CK1D                            #
echo                #                                                             #
echo                ###############################################################
echo.


if %1*==* goto usage
if %1==start goto start
if %1==stop goto stop
if %1==restart goto restart
if %1==control goto control
if %1==help goto usage
if %1==h goto usage
if %1==-h goto usage
if %1==-help goto usage
if %1==--h goto usage
if %1==--help goto usage
if %1==status goto status


:start
sc config "postgresql-8.3" start= demand
sc start  "postgresql-8.3"
cls
echo.
echo			Service has been start with Fully Function.
echo.
echo			postgresql-8.3         = Start
echo.
goto end

:stop
sc stop   "postgresql-8.3"
sc config "postgresql-8.3" start= disabled
cls
echo.
echo			Service has been stop with Fully Function.
echo.
echo			postgresql-8.3         = Stop
echo.
goto end


:auto
sc config "postgresql-8.3" start= auto
cls
echo.
echo			Service has been set Auto Start with Fully Function.
echo.
echo			postgresql-8.3         = Auto Start
echo.

:restart
sc stop "postgresql-8.3" 
cls
echo.
echo			Service has been Restartr with Fully Function.
echo.
echo			postgresql-8.3         = Restart
echo.
goto start


:usage
echo.
echo			Usage : %0 start    	     [Start PostgreSQL Service]
echo		        	%0 stop     	     [Stop PostgreSQL Service]
echo			        %0 restart  	     [Restart PostgreSQL Service]
echo		        	%0 status     	     [Status Service]
echo.
goto fin

:status
sc query "postgresql-8.3"
goto end

:end
echo.
echo                ###############################################################
echo                #                 PostgreSQL Service Control                  #
echo                #                         Scr1pt by                           #
echo                #                          BL4CK1D                            #
echo                #                                                             #
echo                ###############################################################
echo.

goto fin

:fin
