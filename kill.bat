@echo off
title %CD%
if %1*==* goto usage

taskkill /f /im %1.exe
goto end


:usage
echo.
echo.
echo		use     : %0 [name of file]
echo		example : %0 winamp
echo.
echo.
goto end


:end

