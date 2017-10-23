@echo off
title %CD%
echo.

"c:\msys2\usr\bin\cat.exe" %1 | more
goto end


:end
