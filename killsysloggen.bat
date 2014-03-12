@echo off
title %CD%
taskkill /f /im SyslogGen.exe
goto end

:end