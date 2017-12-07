@echo off
title %CD%
rem set one=%1
cls
title %cd%
echo.
echo.
"c:\TOOLS\DevKit32\bin\ls.exe" -X -p %*
echo.
echo                    		Parent Directory : %cd%
echo.
rem echo                    		Child  Directory : %1
goto end

rem :awal
rem echo.
rem echo		Carefully !!!, Continue .....? Maybe Error Occure press any Key or Control + C for Abort
rem echo.
rem pause >> null
rem echo.
rem dir %1
rem goto end


:end

