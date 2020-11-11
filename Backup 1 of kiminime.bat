@echo off
SET me1=%CD%
CD /d "d:\PROJECTS\kiminime"
"c:\sdk\Anaconda2\python.exe" "d:\PROJECTS\kiminime\kiminime.py" %*
CD /d "%me1%"
SET me1=