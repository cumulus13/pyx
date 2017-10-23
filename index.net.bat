@echo off
title %CD%
if %1*==* goto usage

start scite e:\wampserver\www3\index.net\index.html

goto end


:usage
echo.
echo.
echo			use %0 edit [ to Edit index.html file]
echo.
echo.
goto end

:end

