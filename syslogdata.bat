@echo off
title %CD%
if %1*==* goto usage
if %1==repair goto one
if %1==delete goto del
if %1==create goto cre

:one
mysql -uroot -pblackid -D syslogcenter -e "DROP TABLE syslogdata"
mysql -uroot -pblackid -D syslogcenter -e "CREATE TABLE IF NOT EXISTS `syslogdata` (`Id` int(11) NOT NULL AUTO_INCREMENT,`Msg` text NOT NULL,`SenderIP` varchar(50) NOT NULL,`SenderPort_S` varchar(50) NOT NULL,`SenderPort_I` int(11) NOT NULL,`Priority` varchar(50) NOT NULL,`Severity` varchar(50) NOT NULL,`SeverityDesc` varchar(50) NOT NULL,`Facility` varchar(50) NOT NULL,`FacilityDesc` varchar(50) NOT NULL,`RawMsg` text NOT NULL,`ReceivedAt` datetime NOT NULL,PRIMARY KEY (`Id`))"
goto end

:del
mysql -uroot -pblackid -D syslogcenter -e "DROP TABLE syslogdata"
goto end

:cre
mysql -uroot -pblackid -D syslogcenter -e "CREATE TABLE IF NOT EXISTS `syslogdata` (`Id` int(11) NOT NULL AUTO_INCREMENT,`Msg` text NOT NULL,`SenderIP` varchar(50) NOT NULL,`SenderPort_S` varchar(50) NOT NULL,`SenderPort_I` int(11) NOT NULL,`Priority` varchar(50) NOT NULL,`Severity` varchar(50) NOT NULL,`SeverityDesc` varchar(50) NOT NULL,`Facility` varchar(50) NOT NULL,`FacilityDesc` varchar(50) NOT NULL,`RawMsg` text NOT NULL,`ReceivedAt` datetime NOT NULL,PRIMARY KEY (`Id`))"
goto end

:usage
echo.
echo use %0 : [repair / delete / create]
echo.
echo.
goto end

:end