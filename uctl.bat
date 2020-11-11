@echo off
SET me1=%CD%
CD /d "D:\PROJECTS2\utorrentctl"
"c:\SDK\Python37\python.exe" "D:\PROJECTS2\utorrentctl\utorrentctl.py" %*
CD /d "%me1%"
SET me1=