@echo off
title %CD%
if not exist p:\PESAN3.txt goto error
start scite "p:\PESAN3.txt"
rem pesancopy.bat
goto end

:error
echo.
echo                    File TIdak Ditemukan !!!
echo.
echo.
goto end

:end
