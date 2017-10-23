@echo off
title %CD%
set one=%1
cls
title %cd%
echo.
echo.
C:\cygwin\bin\ls -s -h -S -r %1 
echo.
echo                    		Parent Directory : %cd%
echo.
rem echo                    		Child  Directory : %one%
goto end

:awal
echo.
echo		Carefully !!!, Continue .....? Maybe Error Occure press any Key or Control + C for Abort
echo.
pause >> null
echo.
dir %1
goto end


:end
