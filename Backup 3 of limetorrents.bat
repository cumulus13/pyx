@echo off
SET me1=%CD%
CD /d "d:\PROJECTS\limetorrents"
"c:\SDK\Anaconda2\python.exe" "d:\PROJECTS\limetorrents\limetorrents.py" %*
CD /d "%me1%"
SET me1=