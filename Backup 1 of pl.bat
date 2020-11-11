@echo off
SET me1=%CD%
CD /d "c:\PROJECTS\processlist"
"C:\ProgramData\Anaconda2\python.exe" "c:\PROJECTS\processlist\pl.py" %*
CD /d "%me1%"
SET me1=