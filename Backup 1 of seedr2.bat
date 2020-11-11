@echo off
SET me1=%CD%
REM CD /d "d:\PROJECTS\seedr2"
REM echo %~f2
"c:\sdk\Anaconda2\python.exe" "d:\PROJECTS\seedr2\seedr.py" %*
CD /d "%me1%"
SET me1=