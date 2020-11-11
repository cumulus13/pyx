@echo off
SET me1=%CD%
CD /d "D:\PROJECTS2\sourceforge_downloader"
"c:\sdk\Anaconda2\python.exe" "D:\PROJECTS2\sourceforge_downloader\sourceforge.py" %*
CD /d "%me1%"
SET me1=