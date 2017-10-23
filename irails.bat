@echo off
title %CD%
cls
echo.
echo.
title Instant Rails Server

if %1*==* goto usage
if %1==start goto start
if %1==stop goto stop
if %1==help goto usage
if %1==restart goto restart
if %1==status goto status

:start
sc config railsmysql start= demand
sc config apacherails start= demand
sc start railsmysql 
sc start apacherails 
goto end

:stop
sc stop railsmysql 
sc stop apacherails 
sc config railsmysql start= demand
sc config apacherails start= demand
goto end

:restart
sc stop railsmysql 
sc stop apacherails 
sc config railsmysql start= demand
sc config apacherails start= demand
goto start

:status
sc queryex  railsmysql
sc queryex  apacherails
goto end 

:usage
echo.
echo.
echo        use: %0 start / stop / restart / status / help
echo.
echo.
goto end

:end
