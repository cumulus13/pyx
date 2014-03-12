@echo off
title %CD%
if %1*==* goto usage

"c:\Program Files\ZionEdit-2.2.4\zion.exe" %1
goto end

:usage
echo.
echo.
echo		Use : %0 [File]
echo.
echo.
goto end


:end

