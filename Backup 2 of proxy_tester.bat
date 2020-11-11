@echo off
SET me1=%CD%
CD /d "d:\PROJECTS\proxy_tester"
"c:\SDK\Anaconda2\python.exe" "d:\PROJECTS\proxy_tester\proxy_tester.py" %*
CD /d "%me1%"
SET me1=