@echo off
SET me1=%CD%
CD /d "D:\PROJECTS2\htmlc"
"c:\sdk\Anaconda2\python.exe" "D:\PROJECTS2\htmlc\htmlc.py" %*
CD /d "%me1%"
SET me1=