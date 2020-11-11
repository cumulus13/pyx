@echo off
SET me1=%CD%
CD /d "c:\TOOLS\pyx"
"C:\ProgramData\Anaconda2\python.exe" "c:\TOOLS\pyx\mva.py" %*
CD /d "%me1%"
SET me1=