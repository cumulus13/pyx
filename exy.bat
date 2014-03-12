@echo off
title %CD%
if %1*==* goto me
if %1==-h goto error

explorer "%1"
goto end

:me
explorer %cd%
echo.
echo.
echo         use -h for help
goto end

:error
echo.
echo.
echo        use %0 [File/Directory]
echo.
echo.
goto end


:end
taskkill /f /im ex.exe
goto fin


:fin

