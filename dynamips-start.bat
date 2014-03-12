@echo off
title %CD%
rem Launch a local copy of dynamips 

rem set dynamips=%CD%\dynamips.exe
set dynamips=c:\Program Files\Dynamips\dynamips.exe
cd %TEMP%
rem start /belownormal "Dynamips"  cmd /c ""%dynamips%" -H 7200 & pause"
"c:\Program Files\Dynamips\dynamips.exe" -H 7200

