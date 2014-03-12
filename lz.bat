@echo off
title %CD%
cls
echo.

if %1*==* goto usage
if %1== -s goto suffix
if %1== -p goto preffix

dir /b /s *%1*
goto end


:suffix
cls
echo.
if %2*==* goto usage
dir /b /s *%2
goto end

:preffix
cls
echo.
if %2*==* goto usage
dir /b /s %2*
goto end

:usage
cls
echo.
echo.
echo  usage : %0 [file data search]
echo        : %0 -s [suffix file data search]
echo        : %0 -p [prefix file data search]
echo.
echo.
goto end


:end