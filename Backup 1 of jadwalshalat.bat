@echo off
SET me1=%CD%
CD /d "c:\PROJECTS\jadwalshalat"
"c:\sdk\Anaconda2\python.exe" "c:\PROJECTS\jadwalshalat\jadwalshalat.py" %*
CD /d "%me1%"
SET me1=