@echo off
title %CD%
if %1*==* goto one
if %1==-x goto withexit
if %1==--x goto withexit
if %1==-exit goto withexit
if %1==--exit goto withexit

:one
dir /b *.mp3 > list.txt
goto end

:withexit
dir /b *.mp3 > list.txt
exit
goto end



:end
