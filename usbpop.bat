@echo off
title %CD%


if %1*==* goto one
c:\qyx\SyslogGen.exe -q -t:192.168.128.1 -p:523 -f:0 -s:6 -m:"%1 %2 %3 %4 %5 %6" 
goto end

:one
c:\qyx\SyslogGen.exe -q -t:192.168.128.1 -p:523 -f:0 -s:0 -m:"Device USB Detect and Plug and Play !"
goto end





goto end

:end