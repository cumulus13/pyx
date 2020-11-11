@echo off
SET me1=%CD%
CD /d "d:\PROJECTS\pdflayer"
"c:\SDK\Anaconda3\python.exe" "d:\PROJECTS\pdflayer\pdflayer.py" %*
CD /d "%me1%"
SET me1=