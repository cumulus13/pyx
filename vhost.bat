@echo off
title %CD%
if %1*==* goto one
if %1==edit goto editme

:one
cat "e:\wampserver\bin\apache\Apache2.2.11\conf\extra\httpd-vhosts.conf"
echo.
echo.
echo        use %0 Edit [ for Edit/Add/Delete VHost]
echo.
echo.
goto end

:editme
if %2*==* goto editx
if %2==--apacherestart goto editme2
if %2==--apacher goto editme2
goto end

:editx
start scite "e:\wampserver\bin\apache\Apache2.2.11\conf\extra\httpd-vhosts.conf"
rem sc stop wampapache
rem sc start wampapache
rem sc config wampapache start= demand
rem apache.py restart
goto end

:editme2
if %2==--apacherestart goto editme2
if %2==--apacher goto editme2
start scite "e:\wampserver\bin\apache\Apache2.2.11\conf\extra\httpd-vhosts.conf"
sc stop wampapache
sc start wampapache
rem sc config wampapache start= demand
rem apache.py restart
goto end


:end
