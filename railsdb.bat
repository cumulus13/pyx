@echo off
title %CD%
cls
echo.
echo.
echo.

title Rails Mysql Database
cd /d "E:\InstantRails-2.0-win\mysql\bin"
mysqld.exe --verbose
goto end


:end