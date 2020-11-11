@echo off
SET me1=%CD%
CD /d "d:\PROJECTS\ydl"
"c:\sdk\Anaconda2\python.exe" "d:\PROJECTS\ydl\ydl.py" %*
CD /d "%me1%"
SET me1=