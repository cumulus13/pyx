@echo off
title %CD%

 c:\qyx\SyslogGen.exe -q -t:192.168.128.1 -p:522 -f:0 -s:0 -m:%1
 goto end
 
 :end