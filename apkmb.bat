@echo off
SET me1=%CD%
CD /d "D:\PROJECTS2\apkmb"
"c:\sdk\Anaconda3\python.exe" "D:\PROJECTS2\apkmb\apkmb.py" %*
CD /d "%me1%"
SET me1=