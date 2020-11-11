@echo off
SET me1=%CD%
CD /d "D:\PROJECTS2\proxy_tester"
"c:\SDK\Anaconda2\python.exe" "D:\PROJECTS2\proxy_tester\proxy_tester.py" %*
CD /d "%me1%"
SET me1=