@echo off
SET me1=%CD%
CD /d "c:\PROJECTS\google_url_convert"
"c:\programdaTA\Anaconda2\python.exe" "c:\PROJECTS\google_url_convert\guc.py" %*
CD /d "%me1%"
SET me1=