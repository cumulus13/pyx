@echo off
SET me1=%CD%
CD /d "d:\PROJECTS\anitoki"
"c:\sdk\Anaconda2\python.exe" "d:\PROJECTS\anitoki\anitoki.py" %*
CD /d "%me1%"
SET me1=