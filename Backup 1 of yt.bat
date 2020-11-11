@echo off
SET me1=%CD%
CD /d "d:\PROJECTS\pyyoutube"
"c:\sdk\Anaconda2\python.exe" "d:\PROJECTS\pyyoutube\youtube.py" %*
CD /d "%me1%"
SET me1=