@echo off
SET me1=%CD%
CD /d "D:\PROJECTS2\imdbcli"
"c:\sdk\Anaconda3\python.exe" "D:\PROJECTS2\imdbcli\imdbcli.py" %*
CD /d "%me1%"
SET me1=