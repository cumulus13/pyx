@echo off
title %CD%

c:\cygwin\bin\chmod.exe -R -v 777 %1

goto end

:end
