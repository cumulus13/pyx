@echo off
title %CD%
c:\cygwin\bin\ls -a -l %1 | more
goto end


:end
echo.
echo.
