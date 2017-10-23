@echo off
title %CD%
if %1*==* goto error
mkdir "%1"
goto end

:error
cls
echo.
echo.
echo      use %0 [name of Directory]
echo.
echo.
goto end

:end