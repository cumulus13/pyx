@echo off
title %CD%

7z l %1
echo.
pause > nul
7z t %1
echo.

goto end

:end