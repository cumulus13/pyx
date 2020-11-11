@echo off
SET me1=%CD%
CD /d "D:\PROJECTS2\ctrfoobar2000"
"c:\sdk\Anaconda2\python.exe" "D:\PROJECTS2\ctrfoobar2000\control.py" %*
CD /d "%me1%"
SET me1=