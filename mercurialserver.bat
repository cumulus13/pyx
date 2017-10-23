@echo off
title %CD%
set back=%CD%
cd /d "e:\wampserver\www\HG_PROJECT\syslog_center2"
thg serve --web-conf=d:\xampp\hg\hgwebdir.conf
goto end


:end
cd /d %back%
exit /b

