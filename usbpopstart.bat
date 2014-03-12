@echo off
title %CD%

if %1*==* goto one
c:\qyx\SyslogGen.exe -q -t:192.168.128.1 -p:516 -f:14 -s:6 -m:"Device USB Detect and Plug and Play !"
goto end

:one
if %2*==* goto dua
c:\qyx\SyslogGen.exe -q -t:192.168.128.1 -p:516 -f:14 -s:6 -m:"%1"
goto end

:dua
c:\qyx\SyslogGen.exe -q -t:192.168.128.1 -p:516 -f:14 -s:6 -m:"%1 %2" 
goto end

goto end

:end