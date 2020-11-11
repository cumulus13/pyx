@echo off
SET me1=%CD%
CD /d "D:\PROJECTS2\pdflayer"
"c:\SDK\Anaconda3\python.exe" "D:\PROJECTS2\pdflayer\pdflayer.py" %*
CD /d "%me1%"
SET me1=