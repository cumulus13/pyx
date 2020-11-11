@echo off
SET me1=%CD%
CD /d "C:\PROJECTS\utorrentctl"
"c:\SDK\Python37\python.exe" "C:\PROJECTS\utorrentctl\utorrentctl.py" %*
CD /d "%me1%"
SET me1=