@echo off
title %CD%
if %1*==* goto usage
rar a %2.rar %1 c -zc:\license.txt -pblackid
goto end

:usage
echo.
echo.
echo		use %0 [name of archieve/file/folder]
echo.
echo.
goto end

:end


