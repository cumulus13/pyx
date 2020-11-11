@echo off
SET me1=%CD%
CD /d "X:\PROJECTS\deez"
"d:\virtualenv\py-deezer\Scripts\python.exe" "D:\PROJECTSX\deez\deez.py" %*
CD /d "%me1%"
SET me1=