@echo off
SET me1=%CD%
CD /d "D:\PROJECTS2\nginxmaker"
"c:\SDK\Anaconda2\python.exe" "D:\PROJECTS2\nginxmaker\nginxmaker.py" %*
CD /d "%me1%"
SET me1=