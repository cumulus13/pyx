@echo off
SET me1=%CD%
CD /d "d:\PROJECTS\soundpark"
"c:\sdk\Anaconda2\python.exe" "d:\PROJECTS\soundpark\soundpark.py" %*
CD /d "%me1%"
SET me1=