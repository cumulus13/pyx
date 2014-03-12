@echo off
title %CD%
if %1*==* goto help
if %1==start goto start
if %1==stop goto stop
if %1==restart goto restart
if %1==disable goto disable
if %1==enable goto enable
if %1==auto goto auto
if %1==status goto status

goto end

:start
cls
echo.
sc config "Easy File Sharing Web Service" start= demand
sc start "Easy File Sharing Web Service"
goto end

:stop
cls
echo.
sc stop "Easy File Sharing Web Service"
goto end

:restart
cls
echo.
sc stop "Easy File Sharing Web Service"
goto start

:disable
cls
echo.
sc config "Easy File Sharing Web Service" start= disabled
goto end

:enable
cls
echo.
sc config "Easy File Sharing Web Service" start= enable
goto end

:auto
cls
echo.
sc config "Easy File Sharing Web Service" start= auto
goto end

:status
cls
echo.
sc queryex "Easy File Sharing Web Service"
goto end

:help
cls
echo.
echo                 -- Easy File Sharing Web Service - Control --
echo                 ---------------- by BLACKID -----------------
echo.
echo                 use: %0 [start/stop/restart/disable/enable/auto/status]
echo.
goto end

:end
