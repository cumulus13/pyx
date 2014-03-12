@echo off
set NBC=%CD%
if %1==* goto usage
if %1==start goto start
if %1==stop goto stop
if %1==restart goto restart
if %1==status goto status
goto end

:start
CHDIR /d c:\WT-NMP\bin\nginx-1.5.8
c:\exe\ProcessMagic.exe -n c:\WT-NMP\bin\nginx-1.5.8\nginx.exe > nul
processx | grep nginx.exe > c:\TEMP\nginx.status.log
CHDIR /d %NBC%
goto end

:stop
c:\exe\processx.exe -k nginx.exe > nul
echo null > c:\TEMP\nginx.status.log
CHDIR /d %NBC%
goto end

:restart
c:\exe\processx.exe -k nginx.exe > nul
echo null > c:\TEMP\nginx.status.log
CHDIR /d %NBC%
goto start

:status
FINDSTR /R "nginx.exe" c:\TEMP\nginx.status.log
goto end

:usage
echo.
echo   usage: %0 [start/stop/restart]
echo.
goto end

:end
rem CHDIR /d %NBC%