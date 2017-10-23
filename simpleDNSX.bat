@echo off
title %CD%
cls
echo.
echo.
echo.
echo                ###############################################################
echo                #                 Simple DNS Service Control                  #
echo                #                         Scr1pt by                           #
echo                #                          BL4CK1D                            #
echo                #                                                             #
echo                ###############################################################
echo.


if %1*==* goto usage
if %1==start goto start
if %1==stop goto stop
if %1==restart goto restart
if %1==status goto status
if %1==-r goto reload
if %1==-r %2 %3 goto Deprecated
if %1==-u goto removes
if %1==-o %2 reloadfile
if %1==-x Shutdown
if %1== gui goto gui

:status
echo.
sc query sdnsplus
goto end2

:gui
"C:\Program Files\Simple DNS Plus\sdnsplus.exe"
rem adds on
goto end

:reload
"C:\Program Files\Simple DNS Plus\sdnsplus.exe" -r 
goto end

:Deprecated
if %2*==* goto usage
"C:\Program Files\Simple DNS Plus\sdnsplus.exe" -r %2 %3
goto end

:removes
"C:\Program Files\Simple DNS Plus\sdnsplus.exe" -u %2
goto end

:reloadfile
"C:\Program Files\Simple DNS Plus\sdnsplus.exe"  -o %2
goto end

:Shutdown
"C:\Program Files\Simple DNS Plus\sdnsplus.exe"  -x
goto end


:start
sc config sdnsplus start= demand
sc start sdnsplus 
rem "C:\Program Files\Simple DNS Plus\sdnsplus.exe"
rem dnslocal off
rem adds on
goto end

:stop
sc stop sdnsplus
sc config sdnsplus start= disabled
taskkill /f /im sdnsplus.exe
cls
rem dnslocal on
goto end

:usage
echo.
echo			Usage : %0 start /stop / restart / status [DNS Service Control]
echo		                %0 -r    [Reload All Zones]
echo		                %0 -r    [zone-name]  [file-name] [Deprecated. For backwards compatibility only. Use -z option instead]
echo		                %0 -u    [zone-name] [Unloads / removes a zone.]
echo		                %0 -o    [file] [Reloads options file (sdnsplus.config.xml)]
echo		                %0 -x    [Shutdown DNS Server] 
echo				%0 gui   [Gui Control]
echo.
goto end

:end
cls
echo.
echo.
goto end2

:end2
exit
