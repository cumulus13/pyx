@echo off
title %CD%
if %1*==* goto usage
if %1==small goto small

:small
consolesmall.exe
goto end


:usage
echo use
goto end


:end
