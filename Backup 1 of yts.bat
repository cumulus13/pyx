@echo off
SET me1=%CD%
CD /d "d:\PROJECTS\yts"
"c:\sdk\Anaconda2\python.exe" "d:\PROJECTS\yts\yts.py" %*
CD /d "%me1%"
SET me1=