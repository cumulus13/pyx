@echo off
title %CD%
echo.

"c:\TOOLS\DevKit32\bin\cat.exe" %1 | more
goto end


:end
