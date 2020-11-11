@echo off
SET me1=%CD%
CD /d "d:\PROJECTS\pipl"
"c:\sdk\Anaconda2\python.exe" "d:\PROJECTS\pipl\pipl.py" %*
CD /d "%me1%"
SET me1=