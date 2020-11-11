@echo off
SET me1=%CD%
CD /d "d:\PROJECTS\softpedia_downloaders"
"c:\sdk\Anaconda2\python.exe" "d:\PROJECTS\softpedia_downloaders\softpedia.py" %*
CD /d "%me1%"
SET me1=