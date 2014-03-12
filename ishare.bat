
@rem ----- ExeScript Options Begin -----
@rem ScriptType: console,invoker
@rem DestDirectory: temp
@rem Icon: default
@rem OutputFile: d:\pyx\ishare.exe
@rem Comments: Control Easy Web Sharing
@rem CompanyName: licface
@rem FileDescription: Only use with Easy Web Sharing
@rem FileVersion: 1.0.0.1
@rem LegalCopyright: licface
@rem ProductName: Easy Web Sharing Control
@rem ProductVersion: 1.0.0.1
@rem ----- ExeScript Options End -----
@echo off
title %CD%

if %1*==* goto usage
if %1==start goto start
if %1==stop goto stop
if %1==restart goto restart
if %1==auto goto auto
if %1==enable goto enable
if %1==disable goto disable
if %1==status goto status
if %1==gui goto gui
if %1==help goto help

goto end

:usage
echo.
echo.
echo    use %0 start/stop/restart/auto/enable/disable/status/help
echo.
echo.
sc queryex "Easy File Sharing Web Service"
echo.
goto end

:start
sc config "Easy File Sharing Web Service" start= demand
sc start "Easy File Sharing Web Service"
sysloggen -q -t:192.168.128.1 -p:516 -s:5 -f:0 -m:"Service Easy File Sharing Web Service is SUCCESSFULL Start NOW !" 
goto end

:stop
sc stop "Easy File Sharing Web Service"
sc config "Easy File Sharing Web Service" start= demand
sysloggen -q -t:192.168.128.1 -p:516 -s:5 -f:0 -m:"Service Easy File Sharing Web Service is SUCCESSFULL Stop NOW !" 
goto end

:restart
sc stop "Easy File Sharing Web Service"
sc config "Easy File Sharing Web Service" start= demand
goto start

:auto
sc config "Easy File Sharing Web Service" start= auto
sysloggen -q -t:192.168.128.1 -p:516 -s:5 -f:0 -m:"Service Easy File Sharing Web Service is Set to AUTOSTART !" 
goto end

:enable
sc config "Easy File Sharing Web Service" start= enable
sysloggen -q -t:192.168.128.1 -p:516 -s:5 -f:0 -m:"Service Easy File Sharing Web Service is Set to ENABLE !" 
goto end

:disable
sc config "Easy File Sharing Web Service" start= disable
sysloggen -q -t:192.168.128.1 -p:516 -s:5 -f:0 -m:"Service Easy File Sharing Web Service is Set to DISABLE !" 
goto end

:status
sc queryex "Easy File Sharing Web Service"
goto end

:gui
isharegui.py
goto end

:end

