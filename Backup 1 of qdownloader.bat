@echo off
SET me1=%CD%
CD /d "c:\PROJECTS\qdownloader"
"c:\programdaTA\Anaconda2\python.exe" "c:\PROJECTS\qdownloader\qdownloader.py" %*
CD /d "%me1%"
SET me1=