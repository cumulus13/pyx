@echo off
SET me1=%CD%
CD /d "D:\PROJECTS2\yts"
"c:\sdk\Anaconda2\python.exe" "D:\PROJECTS2\yts\yts.py" %*
CD /d "%me1%"
SET me1=