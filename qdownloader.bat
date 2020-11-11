@echo off
SET me1=%CD%
CD /d "D:\PROJECTS2\qdownloader"
"c:\SDK\Anaconda2\python.exe" "D:\PROJECTS2\qdownloader\qdownloader.py" %*
CD /d "%me1%"
SET me1=