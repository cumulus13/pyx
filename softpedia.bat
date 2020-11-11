@echo off
SET me1=%CD%
CD /d "D:\PROJECTS2\softpedia_downloaders"
"c:\sdk\Anaconda2\python.exe" "D:\PROJECTS2\softpedia_downloaders\softpedia.py" %*
CD /d "%me1%"
SET me1=