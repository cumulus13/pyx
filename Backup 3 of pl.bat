@echo off
SET me1=%CD%
CD /d "d:\PROJECTS\processlist"
"c:\SDK\Anaconda2\python.exe" "d:\PROJECTS\processlist\pl.py" %*
CD /d "%me1%"
SET me1=