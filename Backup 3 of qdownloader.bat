@echo off
SET me1=%CD%
CD /d "d:\PROJECTS\qdownloader"
"c:\SDK\Anaconda2\python.exe" "d:\PROJECTS\qdownloader\qdownloader.py" %*
CD /d "%me1%"
SET me1=