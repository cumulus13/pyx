@echo off
SET me1=%CD%
CD /d "c:\PROJECTS\torrent_rename"
"c:\programdaTA\Anaconda2\python.exe" "c:\PROJECTS\torrent_rename\torrent_rename.py" %*
CD /d "%me1%"
SET me1=