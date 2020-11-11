@echo off
SET me1=%CD%
CD /d "d:\PROJECTS\dcmd"
"c:\sdk\Anaconda2\python.exe" "d:\PROJECTS\dcmd\dcmd.py" %*
CD /d "%me1%"
SET me1=