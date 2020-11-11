@echo off
title %CD%
echo.

"c:\TOOLS\msys64\usr\bin\cat.exe" %1 | more
goto end


:end
