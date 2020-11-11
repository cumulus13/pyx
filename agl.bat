@echo off
SET me1=%CD%
CD /d "D:\PROJECTS2\aglink\aglink"
"c:\SDK\Anaconda2\python.exe" "D:\PROJECTS2\aglink\aglink\agl.py" %*
CD /d "%me1%"
SET me1=