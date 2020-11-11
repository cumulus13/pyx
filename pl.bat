@echo off
SET me1=%CD%
CD /d "D:\PROJECTS2\processlist"
"c:\SDK\Anaconda2\python.exe" "D:\PROJECTS2\processlist\pl.py" %*
CD /d "%me1%"
SET me1=