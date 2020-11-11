@echo off
SET me1=%CD%
CD /d "d:\PROJECTS\sourceforge_downloader"
"c:\sdk\Anaconda2\python.exe" "d:\PROJECTS\sourceforge_downloader\sourceforge.py" %*
CD /d "%me1%"
SET me1=