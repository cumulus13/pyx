@echo off
SET me1=%CD%
CD /d "d:\PROJECTS\google_url_convert"
"c:\SDK\Anaconda2\python.exe" "d:\PROJECTS\google_url_convert\guc.py" %*
CD /d "%me1%"
SET me1=