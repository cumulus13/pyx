@echo off
title %CD%
if %1*==* goto one
if %1==-x goto withexit
if %1==--x goto withexit
if %1==-exit goto withexit
if %1==--exit goto withexit

dir /b "%1\*.mp3" > list.txt
dir /b "%1\*.wma" >> list.txt
start scite "%1\list.txt"
goto end


:one
dir /b *.mp3 > list.txt
dir /b *.wma >> list.txt
start scite list.txt
goto end

:withexit
dir /b *.mp3 > list.txt
start scite list.txt
exit
goto end



:end
