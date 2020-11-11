@echo off
SET me1=%CD%
CD /d "D:\PROJECTS2\ydl"
"c:\sdk\Anaconda2\python.exe" "D:\PROJECTS2\ydl\ydl.py" %*
CD /d "%me1%"
SET me1=