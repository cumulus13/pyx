@echo off
SET me1=%CD%
CD /d "d:\PROJECTS\neonime"
"C:\SDK\Anaconda2\python.exe" "d:\PROJECTS\neonime\neonime.py" %*
CD /d "%me1%"
SET me1=