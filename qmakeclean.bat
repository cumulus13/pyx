@echo off
title %CD%
del *.save
del *.pro
del Makefile
del *.Debug
del *.Release
rmdir /S /Q debug
rmdir /S /Q release
rmdir /S /Q bin
rmdir /S /Q obj
rmdir /S /Q tmp
goto end


:end
cls
echo.
echo.
echo      It's Very Clean...!
echo.
echo.