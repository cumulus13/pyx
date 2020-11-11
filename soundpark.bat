@echo off
SET me1=%CD%
CD /d "D:\PROJECTS2\soundpark"
"c:\sdk\Anaconda2\python.exe" "D:\PROJECTS2\soundpark\soundpark.py" %*
CD /d "%me1%"
SET me1=