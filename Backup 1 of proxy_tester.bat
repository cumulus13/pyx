@echo off
SET me1=%CD%
CD /d "c:\projects\proxy_tester"
"c:\SDK\Anaconda2\python.exe" "c:\projects\proxy_tester\proxy_tester.py" %*
CD /d "%me1%"
SET me1=