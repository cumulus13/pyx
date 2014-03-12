@echo off
title %CD%
echo.
echo.
echo		WampServer Vhost Configuration.
echo.
echo.

if %1*==* goto one
if %1==edit goto editme
if %1==2 goto host1
if %1==1 goto host2

:host1
del "E:\wampserver\bin\apache\Apache2.2.11\conf\extra\httpd-vhosts.conf"
copy "E:\wampserver\bin\apache\Apache2.2.11\conf\extra\httpd-vhosts.conf.host1" "E:\wampserver\bin\apache\Apache2.2.11\conf\extra\httpd-vhosts.conf"
goto end

:host2
del "E:\wampserver\bin\apache\Apache2.2.11\conf\extra\httpd-vhosts.conf"
copy "E:\wampserver\bin\apache\Apache2.2.11\conf\extra\httpd-vhosts.conf.host2" "E:\wampserver\bin\apache\Apache2.2.11\conf\extra\httpd-vhosts.conf"
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

cat "E:\wampserver\bin\apache\Apache2.2.11\conf\extra\httpd-vhosts.conf"

goto end

:editme
if %2*==* goto editx
if %2==--apacherestart goto editme2
if %2==--apacher goto editme2
goto end

:editx
start scite "E:\wampserver\bin\apache\Apache2.2.11\conf\extra\httpd-vhosts.conf"
rem sc stop wampapache
rem sc start wampapache
rem sc config wampapache start= demand
rem apache.py restart
goto end

:editme2
if %2==--apacherestart goto editme2
if %2==--apacher goto editme2
start scite "E:\wampserver\bin\apache\Apache2.2.11\conf\extra\httpd-vhosts.conf"
sc stop wampapache
sc start wampapache
rem sc config wampapache start= demand
rem apache.py restart
goto end


:end
