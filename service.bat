@echo off
if %1*==* goto usage
if %2*==* goto usage
if %1==nginx goto nginx
if %1==install goto install
if %2==stop goto stop
if %2==start goto start
if %2==restart goto restart
if %2==status goto status
goto end

:install
if %2==-h goto usage_install
if %2==--help goto usage_install
if %2*==* goto usage_install
nssm install %2 %3
nssm set %2 AppParameters %4
nssm set %2 Description %5
nssm set %2 DisplayName %6
nssm set %2 AppStdout "f:\LOGCENTER\%2.log"
SET INSTALL_START=demand
if %INSTALL_START%==auto goto auto
nssm set %2 Start SERVICE_DEMAND_START
if %INSTALL_START%==demand goto demand
goto end

:auto
nssm set %2 Start SERVICE_DELAYED_AUTO_START
rem nssm start %2
goto end

:demand
nssm set %2 Start SERVICE_DEMAND_START
rem nssm start %2
goto end

:usage_install
echo. 
echo usage: %0 install SERVICE_NAME EXE_PATH ARGUMENTS DESCRIPTION DISPLAY_NAME [AUTO/DEMAND]
echo.
goto end

:nginx
if not defined NGINX_PATH goto setNGINX_PATH
if %2==reload goto nginx_reload
if %2==restart goto nginx_restart
if %2==stop goto nginx_stop
if %2==quit goto nginx_quit
if %2==status goto status
if %2==start goto start
got end

:nginx_reload
set THIS=%CD%
cd /d %NGINX_PATH%
nginx.exe -s reload
cd /d %THIS%
set THIS=
goto end

:nginx_reopen
set THIS=%CD%
cd /d %NGINX_PATH%
nginx.exe -s reopen
cd /d %THIS%
set THIS=
goto end

:nginx_restart
set THIS=%CD%
cd /d %NGINX_PATH%
nginx.exe -s quit
sc stop nginx
px -k nginx.exe
cd /d %THIS%
set THIS=
rem if %error_level% == 2 goto end1
goto start

:nginx_stop
set THIS=%CD%
cd /d %NGINX_PATH%
nginx.exe -s quit
sc stop nginx
px -k nginx.exe
cd /d %THIS%
set THIS=
if %error_level% == 2 goto end1
goto end

:nginx_quit
set THIS=%CD%
cd /d %NGINX_PATH%
nginx.exe -s quit
sc stop nginx
px -k nginx.exe
cd /d %THIS%
set THIS=
if %error_level% == 2 goto end1
goto end

:setNGINX_PATH
set /P NGINX_PATH=Where is Nginx PATH DIR (DIR ONLY NOT FILE) [FULL PATH]: 
goto nginx

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

:nginx1
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
echo usage: %0 SERVICE_NAME start/stop/restart
echo usage: %0 install SERVICE_NAME EXE_PATH ARGUMENTS DESCRIPTION DISPLAY_NAME [AUTO/DEMAND]
echo.
goto end

:end
if %errorlevel%==9009 goto end1
echo error = %errorlevel%
if %errorlevel%==2 (
	echo Service is being starting ....
)
goto end1


:end1
