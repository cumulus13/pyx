@echo off
SET me1=%CD%
CD /d "D:\PROJECTSX\neonime"
"c:\sdk\Anaconda2\python.exe" "D:\PROJECTSX\neonime\neonime.py" %*
CD /d "%me1%"
SET me1=