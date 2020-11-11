@echo off
SET me1=%CD%
CD /d "d:\PROJECTS\aglink\aglink"
"c:\SDK\Anaconda2\python.exe" "d:\PROJECTS\aglink\aglink\agl.py" %*
CD /d "%me1%"
SET me1=