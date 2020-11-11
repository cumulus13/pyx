@echo off
SET me1=%CD%
CD /d "d:\PROJECTS\htmlc"
"c:\sdk\Anaconda2\python.exe" "d:\PROJECTS\htmlc\htmlc.py" %*
CD /d "%me1%"
SET me1=