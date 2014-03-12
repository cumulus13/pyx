@echo off
set NBCC=%CD%
if %1==* goto usage
if %1==start goto start
if %1==stop goto stop
if %1==restart goto restart
if %1==status goto status
goto end

:start
CHDIR /d c:\Apps\Hestia.0.0.00215.win32
c:\exe\ProcessMagic.exe -n c:\Apps\Hestia.0.0.00215.win32\Hestia.exe > nul
processx | grep Hestia.exe > c:\TEMP\hestia.status.log
CHDIR /d %NBCC%
goto end

:stop
c:\exe\processx.exe -k Hestia.exe > nul
echo null > c:\TEMP\hestia.status.log
CHDIR /d %NBCC%
goto end

:restart
c:\exe\processx.exe -k Hestia.exe > nul
echo null > c:\TEMP\hestia.status.log
CHDIR /d %NBCC%
goto start

:status
FINDSTR /R "Hestia.exe" c:\TEMP\hestia.status.log
goto end

:usage
echo.
echo   usage: %0 [start/stop/restart]
echo.
goto end

:end
rem CHDIR /d %NBC%