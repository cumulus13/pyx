@echo off
SET me1=%CD%
CD /d "c:\PROJECTS\nginxmaker"
"C:\ProgramData\Anaconda2\python.exe" "c:\PROJECTS\nginxmaker\nginxmaker.py" %*
CD /d "%me1%"
SET me1=