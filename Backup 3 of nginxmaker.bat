@echo off
SET me1=%CD%
CD /d "d:\PROJECTS\nginxmaker"
"c:\SDK\Anaconda2\python.exe" "d:\PROJECTS\nginxmaker\nginxmaker.py" %*
CD /d "%me1%"
SET me1=