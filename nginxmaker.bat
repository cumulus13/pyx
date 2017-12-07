@echo off
set path_me=%cd%
cd /d f:\PROJECTS\REPOSITORY\nginxmaker
c:\SDK\Anaconda2\python.exe f:\PROJECTS\REPOSITORY\nginxmaker\nginxmaker.py %*
cd /d %path_me%
