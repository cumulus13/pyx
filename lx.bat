@echo off
title %CD%
cls
echo.
echo.
dir *.%1 | more
goto end


:end