@echo off
title %CD%
if %1*==* goto usage

"C:\Program Files\Sandboxie\Start.exe" %1

goto end

:usage
echo.
echo.
echo		use %0 [Name Program to Start]
echo.
echo.
goto end

:end
