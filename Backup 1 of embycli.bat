@echo off
SET me1=%CD%
CD /d "d:\PROJECTS\embycli"
"c:\sdk\Anaconda2\python.exe" "d:\PROJECTS\embycli\embycli.py" %*
CD /d "%me1%"
SET me1=