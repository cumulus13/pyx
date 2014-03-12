@echo off
title %CD%

cd /d "c:\Program Files\Privoxy"
privoxy.exe
goto end

:end