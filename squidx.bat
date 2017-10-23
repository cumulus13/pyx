@echo off
title %CD%

"C:\squid\sbin\squid.exe" -d 0 -f c:/squid/etc/squid.conf -X
goto end

:end
