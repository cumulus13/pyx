@echo off
title %CD%
set one=%1
cls
title %cd%
echo.
echo.
dir /d %*
::echo.
::echo %errorlevel%
echo.
echo                    		Parent Directory : %cd%
echo.
rem echo                    		Child  Directory : %1
goto end

:awal
echo.
echo		Carefully !!!, Continue .....? Maybe Error Occure press any Key or Control + C for Abort
echo.
pause >> null
echo.
dir %*
goto end


:end

