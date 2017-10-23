@echo off
title %CD%

if %1*==* goto usage
if %1==start goto start
if %1==restart goto restart
if %1==stop goto stop
if %1==automatic goto automatic
if %1==status goto status

goto end


:usage
echo.
echo.
echo            use %0 start        [To Start Apache Server]
echo                %0 stop         [To Stop Apache Server]
echo                %0 restart      [To Restart Apache Server]
echo                %0 automatic    [To Set Automatic Start Apache Server]
echo.
echo.
goto end

:start
sc config wampapache start= demand
sc start wampapache
goto end

:stop 
sc stop wampapache
sc config wampapache start= demand
goto end

:restart
net stop wampapache
net start wampapache
goto end

:automatic
sc config wampapache start= auto
goto end

:status
sc query wampapache
goto end

:end
