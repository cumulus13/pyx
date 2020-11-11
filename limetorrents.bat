@echo off
SET me1=%CD%
CD /d "D:\PROJECTS2\limetorrents"
"c:\SDK\Anaconda2\python.exe" "D:\PROJECTS2\limetorrents\limetorrents.py" %*
CD /d "%me1%"
SET me1=