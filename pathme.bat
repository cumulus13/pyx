@echo off
title %CD%

if %1*==* goto one
if %1==+ goto add

rem "c:\EXE\ipathx.exe" %1\%3
path %1;%path%
path %cd%;%path%
goto end

:one
path %cd%;%path%
"c:\exe\addpathx.exe" post %cd%
goto end

:add
"c:\EXE\ipathx.exe" "%CD%\%2"
"c:\exe\addpathx.exe" post "%CD%\%2"
goto end

:end
