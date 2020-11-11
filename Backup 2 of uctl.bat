@echo off
SET me1=%CD%
CD /d "d:\PROJECTS\utorrentctl"
"c:\SDK\Python37\python.exe" "d:\PROJECTS\utorrentctl\utorrentctl.py" %*
CD /d "%me1%"
SET me1=