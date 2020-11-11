@echo off
SET me1=%CD%
CD /d "c:\SDK\Anaconda2\Scripts"
"c:\sdk\Anaconda2\python.exe" "c:\SDK\Anaconda2\Scripts\google_translate.py" %*
CD /d "%me1%"
SET me1=