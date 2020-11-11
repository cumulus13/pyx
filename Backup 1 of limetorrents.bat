@echo off
SET me1=%CD%
CD /d "c:\PROJECTS\limetorrents"
"c:\programdaTA\Anaconda2\python.exe" "c:\PROJECTS\limetorrents\limetorrents.py" %*
CD /d "%me1%"
SET me1=