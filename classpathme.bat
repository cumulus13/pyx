@echo off
title %CD%
if %1*==* goto error

set classpath=%cd%\%1;%classpath%


:error
echo.
echo.
echo        Sintax Error !
echo.
echo        usage : %0 [Name Of File]
echo.
goto end


:end
