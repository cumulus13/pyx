@echo off
SET me1=%CD%
CD /d "x:\PROJECTS\meownime"
"c:\sdk\Anaconda2\python.exe" "x:\PROJECTS\meownime\meownime.py" %*
CD /d "%me1%"
SET me1=