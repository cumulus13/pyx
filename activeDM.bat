@echo off
title %CD%
if %1*==* goto help
if %1==start goto start
if %1==restart goto restart
if %1==stop goto stop
if %1==disable goto disable
if %1==auto goto  auto
if %1==enable goto enable
if %1==status goto status

goto end

:status
sc queryex "Active@ Disk Monitor"
goto end

:start
sc start "Active@ Disk Monitor"
goto end

:stop
sc stop "Active@ Disk Monitor"
taskkill /f /im "diskmonitor.exe"
goto end

:restart
sc stop "Active@ Disk Monitor"
goto start

:auto
sc config "Active@ Disk Monitor" start= auto
goto end

:enable
sc config "Active@ Disk Monitor" start= enable
goto end

:disable
sc config "Active@ Disk Monitor" start= disabled
goto end

:help
echo.
echo   use: %0 [start/stop/disable/enable/auto/restart]
echo.
echo.
goto end

:end