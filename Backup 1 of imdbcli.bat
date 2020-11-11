@echo off
SET me1=%CD%
CD /d "d:\PROJECTS\imdbcli"
"c:\sdk\Anaconda3\python.exe" "d:\PROJECTS\imdbcli\imdbcli.py" %*
CD /d "%me1%"
SET me1=