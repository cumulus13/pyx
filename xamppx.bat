@echo off
title %CD%
cls
echo.
echo.
title XAMPP Server Services

if %1*==* goto usage
if %1==start goto start
if %1==startall goto startall
if %1==stop goto stop
if %1==stopall goto stopall
if %1==help goto usage
if %1==restart goto restart
if %1==restartall goto restartall
if %1==status goto status
if %1==st goto status
if %1==with--tomcat goto tomcat
if %1==readme goto readme

if %1==tomcatstop goto tomcatstop
if %1==stoptomcat goto tomcatstop
if %1==tomcatstart goto tomcatstart
if %1==starttomcat goto tomcatstart
if %1==tomcatrestart goto tomcatrestart
if %1==restarttomcat goto tomcatrestart

if %1==apachestop goto  apachestop
if %1==stopapache goto apachestop
if %1==apachestart goto  apachestart
if %1==startapache goto apachestart
if %1==apacherestart goto apacherestart
if %1==retstartapache goto apacherestart

if %1==mysqlstop goto  mysqlstop
if %1==stopmysql goto mysqlstop
if %1==mysqlstart goto  mysqlstart
if %1==startmysql goto mysqlstart
if %1==mysqlrestart goto mysqlrestart
if %1==restartmysql goto mysqlrestart

:start
sc config mysql start= demand
sc config apache2.2 start= demand
sc config xampptomcat start= demand
sc start mysql 
sc start apache2.2 
goto end

:stop
sc stop mysql 
sc stop apache2.2 
sc stop  xampptomcat
sc config mysql start= demand
sc config apache2.2 start= demand
sc config xampptomcat start= demand
goto end

:restart
net stop mysql 
net stop apache2.2
sc config mysql start= demand
sc config apache2.2 start= demand
sc config xampptomcat start= demand
goto start

:tomcat
sc start mysql 
sc start apache2.2 
sc start xampptomcat
sc config mysql start= demand
sc config apache2.2 start= demand
sc config xampptomcat start= demand
sc config xampptomcat start= demand
goto end

:startall
sc config mysql start= demand
sc config apache2.2 start= demand
sc config xampptomcat start= demand
sc start mysql 
sc start apache2.2 
sc start xampptomcat
goto end

:stopall
sc config mysql start= demand
sc config apache2.2 start= demand
sc config xampptomcat start= demand
sc stop mysql 
sc stop apache2.2 
sc stop xampptomcat
goto end

:restartall
sc config mysql start= demand
sc config apache2.2 start= demand
sc config xampptomcat start= demand
net stop mysql 
net stop apache2.2 
net stop xampptomcat
goto startall

:status
sc query mysql 
sc query apache2.2 
sc query xampptomcat
goto end

:tomcatstop
sc config xampptomcat start= demand
sc stop xampptomcat
goto end

:tomcatstart
sc config xampptomcat start= demand
sc start xampptomcat
goto end

:apachestop
sc config apache2.2 start= demand
sc stop apache2.2
goto end

:apachestart
sc config apache2.2 start= demand
sc start apache2.2
goto end

:mysqlstop
sc config mysql start= demand
sc stop mysql
goto end

:mysqlstart
sc config mysql start= demand
sc start mysql
goto end

:apacherestart
net stop apache2.2
goto apachestart

:mysqlrestart
net stop mysql
goto mysqlstart

:tomcatrestart
net stop xampptomcat
goto tomcatstart

:readme
type D:\xampp\readme_en.txt;xampp-changes.txt;passwords.txt;readme-addon-tomcat.txt | more
goto end

:usage
echo.
echo.
echo        use: %0 start / stop / restart / startall / stopall / restartall /help            : Control start, stop, restart service or all service
echo             %0 with--tomcat                            : Start with Tomcat Service
echo             %0 starttomcat / tomcatstart               : Only start Tomcat
echo             %0 stoptomcat / tomcatstop                 : Only stop Tomcat
echo             %0 startapache / apachestart               : Only start Apache
echo             %0 stopapache / apachestop                 : Only stop Apache
echo             %0 restartapache / apacherestart           : Only restart Apache
echo             %0 startmysql / mysqlstart                 : Only start Mysql
echo             %0 stopmysql / mysqlstop                   : Only stop Mysql
echo             %0 restartmysql / mysqlrestart             : Only restart Mysql
echo             %0 help                                    : Help This
echo             %0 readme                                  : README XAMPP or use can use 'man xampp'
echo.
echo.
goto end

:end
title %cd%
