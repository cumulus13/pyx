:------------------------- WARNING ! ----------------------
: Be VERY careful making changes to this file.  This file 
: will be updated by the update_path.exe script.
:-----------------------------------------------------------
@echo off
title %CD%
PATH "D:\Flash Rails\ruby\bin";%PATH%
CD /d "D:\Flash Rails\ruby_apps"
rem cmd.exe /K dir
echo.
ruby -v
goto end


:end