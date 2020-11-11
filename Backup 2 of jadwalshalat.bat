@echo off
SET me1=%CD%
CD /d "d:\PROJECTS\jadwalshalat"
"c:\sdk\Anaconda2\python.exe" "d:\PROJECTS\jadwalshalat\jadwalshalat.py" %*
CD /d "%me1%"
SET me1=