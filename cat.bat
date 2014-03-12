@echo off
title %CD%
echo.

"c:\Git\bin\cat.exe" %1 | more
goto end


:end
