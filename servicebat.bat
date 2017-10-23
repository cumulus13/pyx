@echo off
title %CD%
if %1*==* goto usage
if %1==start goto start
if %1==stop goto stop
if %1==restart goto restart
if %1==enable goto enable
if %1==disable goto disable
if %1==auto goto auto
if %1==cname goto cname
goto end

:enable
rem if %3*==* goto usage
rem if %3== auto goto auto2
sc config "%2" start= demand
sc query "%2"
echo.
echo.
echo           To Start service use :  %0 Start %2
echo.
echo.
goto end

:disable
sc config "%2" start= disable
sc query "%2"
goto end

:auto1
sc config "%2" start= auto
sc query "%2"
echo.
echo.
echo      to start service use %0 Start %2
echo.
echo.
goto end

:auto2
sc config "%3" start= auto
sc query "%3"
goto end

:start
sc start "%2"
rem sc query "%2"
goto end

:stop
sc stop "%2"
rem sc query "%2"
goto end

:restart
sc stop "%2"
goto start2
goto end

:start2
sc start "%2"
sc query "%2"
goto end

:cname
sc config %2 DisplayName= %3
goto end


:usage
cls
echo.
echo.
echo        use %0 [Option] [name service]  auto
echo.
echo               option = [start/stop/restart]
echo.
echo                        [enable/disable/auto]
echo.
echo                        [cname] change name of reg service
echo.
echo.
goto end




:usage2
cls
echo.
echo.
echo        use %0 [Option] [name service]  auto
echo               option = [start/stop/restart]
echo                        [enable/disable/auto]
echo                        [cname] change name of reg service
echo.
echo.
goto end


:end