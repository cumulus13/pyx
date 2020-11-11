@echo off
SET me1=%CD%
CD /d "d:\PROJECTS\onesecmail"
"c:\sdk\Anaconda2\python.exe" "d:\PROJECTS\onesecmail\onesecmail.py" %*
CD /d "%me1%"
SET me1=