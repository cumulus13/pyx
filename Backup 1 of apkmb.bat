@echo off
SET me1=%CD%
CD /d "d:\PROJECTS\apkmb"
"c:\sdk\Anaconda3\python.exe" "d:\PROJECTS\apkmb\apkmb.py" %*
CD /d "%me1%"
SET me1=