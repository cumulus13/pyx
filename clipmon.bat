@echo off
SET me1=%CD%
CD /d "X:\PROJECTS\clipboard_monitor"
"c:\sdk\Anaconda2\python.exe" "X:\PROJECTS\clipboard_monitor\clipmon.py" %*
CD /d "%me1%"
SET me1=