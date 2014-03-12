@echo off
title %CD%
if %1*==* goto usage
if %1==-r goto dir
if %1==-R goto dir

rem c:\cygwin\bin\cp.exe -v "%1" "%2"
c:\cygwin\bin\cp.exe -v %1 %2
if %2*==* goto usage
goto end

:dir
rem c:\cygwin\bin\cp.exe -r -v "%2" "%3"
c:\cygwin\bin\cp.exe -r -v %1 %2
if %2*==* goto usage
goto end

:usage
echo.
echo.
echo      Syntax Error !!!
echo.
goto end

:end
