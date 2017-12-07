@echo off
title %CD%

set me=%cd%

if %1*==* goto usage
if %1==pf goto pf


cd /d "%1"
goto end


:pf
cd /d "c:\Program Files"
goto end

:one
cd /d %1:\
goto end

:usage
echo.
echo.
echo           use:  go [Drive to Go]
echo.
echo.
echo                 script by BL4CK1D
goto end2

:end
title		"%1"

:end2
echo                             You are in: "%CD%"
title		"%CD%"
