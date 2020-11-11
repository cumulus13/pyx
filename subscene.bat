@echo off
SET me1=%CD%
CD /d "d:\PROJECTSx\subscene"
"c:\sdk\Anaconda2\python.exe" "d:\PROJECTSx\subscene\subscene.py" %*
CD /d "%me1%"
SET me1=