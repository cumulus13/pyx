@echo off
title %CD%
rem if %1*==* goto one
title %cd%
cls
echo.
echo.

if %1*==* goto help
if %1==-s goto suffix
if %1==-p goto preffix

dir *%1* 
goto end

:suffix
dir *%2
goto end

:preffix
dir %2*
goto end

:help
echo.
echo.
echo			use %0 -s input	= list with Suffix File
echo			       -p input	= list with Preffix File
echo			       default with center word like: beg[in]ning
echo.

:end
echo.
rem echo							"%cd%"
echo.
echo				For Help use option "-help"
echo.
