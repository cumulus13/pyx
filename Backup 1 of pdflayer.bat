@echo off
SET me1=%CD%
CD /d "c:\PROJECTS\pdflayer"
"C:\ProgramData\Anaconda2\python.exe" "c:\PROJECTS\pdflayer\pdflayer.py" %*
CD /d "%me1%"
SET me1=