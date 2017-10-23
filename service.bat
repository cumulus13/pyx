@echo off
if %1*==* goto usage
if %2*==* goto usage
if %2==stop goto stop
if %2==start goto start
if %2==restart goto restart
if %2==status goto status
goto end

:start
if %1==hamachi2svc goto hamachi_start
net start %1
goto end

:start1
net start %1
goto end

:stop
if %1==hamachi2svc goto hamachi_stop
if %1==nginx goto nginx
sc stop %1
goto end

:hamachi_stop
sc stop hamachi2svc
sc stop LMIGuardiansvc
goto end

:hamachi_start
sc start hamachi2svc
sc start LMIGuardiansvc
goto end

:nginx
px -k nginx.exe
rem echo %errorlevel%
if %errorlevel%==2 goto nginx2
goto end

:nginx2
taskkill /f /im nginx.exe
rem echo %errorlevel%
if %errorlevel%==128 goto nginx
goto end

:nginx3
net stop %1
px -k nginx.exe
if %errorlevel%==2 goto nginx4
rem echo %errorlevel%
net start %1
goto end

:nginx4
taskkill /f /im nginx.exe
rem echo %errorlevel%
if %errorlevel%==128 goto nginx5
net start %1
goto end

:nginx5
px -k  nginx.exe
rem echo %errorlevel%
if %errorlevel%==2 goto nginx4
net start %1
goto end

:restart
if %1==nginx goto nginx3
net stop %1
net start %1
goto end

:status
sc query %1
echo -------------------------------------------------------------------------------------
sc qc %1
goto end

:usage
echo
echo usage: %0 SERVICE start/stop/restart
echo.
goto end

:end
echo error = %errorlevel%
if %errorlevel%==2 goto start1
