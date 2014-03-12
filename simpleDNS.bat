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
"H:\Program Files\Simple DNS Plus\sdnsplus.exe"
if %2== kill goto guikill
rem sysloggen -q -t:192.168.128.1 -p:516 -s:6 -f:0 -m:"Simple DNS Plus GUI Start NOW !" 
rem adds on
goto end

:guikill
taskkill /f /im "sdnsgui.exe"
goto end

:reload
"H:\Program Files\Simple DNS Plus\sdnsplus.exe" -r 
rem sysloggen -q -t:192.168.128.1 -p:516 -s:6 -f:0 -m:"Simple DNS Plus SUCCESSFULL Reload Data !" 
goto end

:Deprecated
if %2*==* goto usage
"H:\Program Files\Simple DNS Plus\sdnsplus.exe" -r %2 %3
goto end

:removes
"H:\Program Files\Simple DNS Plus\sdnsplus.exe" -u %2
rem sysloggen -q -t:192.168.128.1 -p:516 -s:6 -f:0 -m:"Simple DNS Plus: Host %2 SUCCESSFULL Remove !" 
goto end

:reloadfile
"H:\Program Files\Simple DNS Plus\sdnsplus.exe"  -o %2
rem sysloggen -q -t:192.168.128.1 -p:516 -s:6 -f:0 -m:"Simple DNS Plus: File %2 SUCCESSFULL Reload !" 
goto end

:Shutdown
"H:\Program Files\Simple DNS Plus\sdnsplus.exe"  -x
rem sysloggen -q -t:192.168.128.1 -p:516 -s:6 -f:0 -m:"Simple DNS Plus STOP / SHUTDOWN NOW !" 
goto end


:start
rem sc config sdnsplus start= demand
sc start sdnsplus 
rem "H:\Program Files\Simple DNS Plus\sdnsplus.exe"
rem dnslocal off
rem adds on
rem sysloggen -q -t:192.168.128.1 -p:516 -s:6 -f:0 -m:"Simple DNS Plus START NOW !" 
goto end

:stop
sc stop sdnsplus
rem sc config sdnsplus start= disabled
taskkill /f /im sdnsplus.exe
cls
rem dnslocal on
rem sysloggen -q -t:192.168.128.1 -p:516 -s:6 -f:0 -m:"Simple DNS Plus STOP NOW !" 
goto end

:restart
sc stop sdnsplus
rem sc config sdnsplus start= disabled
taskkill /f /im sdnsplus.exe
net stop dnscache
net start dnscache
cls
rem dnslocal on
goto start

:backup
if %2*==* goto backup2
del "D:\%2\ZoneFiles.zip"
7z a "D:\%2\ZoneFiles.zip" "C:\Documents and Settings\All Users\Application Data\JH Software\Simple DNS Plus\ZoneFiles"
goto end

:backup2
del "D:\BACKUP_DATA\ZoneFiles.zip"
7z a "D:\BACKUP_DATA\ZoneFiles.zip" "C:\Documents and Settings\All Users\Application Data\JH Software\Simple DNS Plus\ZoneFiles"
goto end

:usage
echo.
echo			Usage : %0 start /stop / restart / status (sDNS Service Control)
echo		                %0 -r  [Reload All Zones]
echo		                %0 -r  [zone-name] (file-name] (Deprecated. For backwards compatibility only. 
echo                                                               Use -z option instead)
echo		                %0 -u  [zone-name] (Unloads / removes a zone.)
echo		                %0 -o  [file]      (Reloads options file "sdnsplus.config.xml")
echo		                %0 -x              (Shutdown DNS Server])
echo                         %0 -b  [Folder]    (Backup Zone File)
echo                         %0 gui [kill]      (Gui Control)
echo.
goto end2

:end
cls
echo.
echo.
goto end2

:end2
