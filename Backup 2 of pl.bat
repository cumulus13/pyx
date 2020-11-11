@echo off
SET me1=%CD%
CD /d "c:\PROJECTS\processlist"
"c:\SDK\Anaconda2\python.exe" "c:\PROJECTS\processlist\pl.py" %*
CD /d "%me1%"
SET me1=