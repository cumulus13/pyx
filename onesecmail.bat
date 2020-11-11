@echo off
SET me1=%CD%
CD /d "D:\PROJECTS2\onesecmail"
"c:\sdk\Anaconda2\python.exe" "D:\PROJECTS2\onesecmail\onesecmail.py" %*
CD /d "%me1%"
SET me1=