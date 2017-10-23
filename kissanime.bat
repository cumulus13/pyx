@echo off
if %1==update goto update
"c:\Python27\python.exe"  "f:\PROJECTS\REPOSITORY\kissanime\kissanime.py" %*
goto end

:update
set me=%CD%
cd /d "f:\PROJECTS\REPOSITORY\kissanime"
git pull origin master
cd /d %me%
goto end


:end