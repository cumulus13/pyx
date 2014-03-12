@echo off
title %CD%
echo.
echo.
echo		XAMPP Vhost Configuration.
echo.
echo.
if %1*==* goto one
if %1==edit goto editme
if %1==2 goto host1
if %1==1 goto host2

:host1
move "D:\xampp\apache\conf\extra\httpd-vhosts.conf" ..\..\BACKUP_CONF\httpd-vhosts_%time%.conf
copy "D:\xampp\apache\conf\extra\httpd-vhosts.conf.host1" "D:\xampp\apache\conf\extra\httpd-vhosts.conf"
goto end

:host2
move "D:\xampp\apache\conf\extra\httpd-vhosts.conf" ..\..\BACKUP_CONF\httpd-vhosts_%time%.conf
copy "D:\xampp\apache\conf\extra\httpd-vhosts.conf.host2" "D:\xampp\apache\conf\extra\httpd-vhosts.conf"
goto end


:one
echo.
echo.
echo        use %0 Edit [ for Edit/Add/Delete VHost    ]
echo.
echo            %0 1    [ for Vhost Type Host 1 - HDD 1]
echo.
echo            %0 2    [ for Vhost Type Host 2 - HDD 2]
echo.
echo.
echo.
echo.

cat "D:\xampp\apache\conf\extra\httpd-vhosts.conf"

goto end

:editme
if %2*==* goto editx
rem if %2==--apacherestart goto editme2
rem if %2==--apacher goto editme2
goto end

:editx
start scite "D:\xampp\apache\conf\extra\httpd-vhosts.conf"
rem sc stop wampapache
rem sc start wampapache
rem sc config wampapache start= demand
rem apache.py restart
goto end

:editme2
if %2==--apacherestart goto editme2
if %2==--apacher goto editme2
start scite "D:\xampp\apache\conf\extra\httpd-vhosts.conf"
rem sc stop wampapache
rem sc start wampapache
rem sc config wampapache start= demand
rem apache.py restart
goto end


:end
