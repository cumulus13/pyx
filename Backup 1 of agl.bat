@echo off
SET me1=%CD%
CD /d "c:\PROJECTS\aglink\aglink"
"c:\SDK\Anaconda2\python.exe" "c:\PROJECTS\aglink\aglink\agl.py" %*
CD /d "%me1%"
SET me1=