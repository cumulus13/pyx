@echo off
SET me1=%CD%
CD /d "D:\PROJECTS\tubeoffline"
"c:\sdk\Anaconda2\python.exe" "D:\PROJECTS\tubeoffline\tubeoffline.py" %*
CD /d "%me1%"
SET me1=