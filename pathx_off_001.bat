@echo off
title %CD%

if %1==--help goto usage
if %1==--h goto usage
if %1==-h goto usage
if %1==/? goto usage
if %1==? goto usage
if %1==help goto usage
if %1*==* goto one
if %1==reset goto reset


:one
set pathbefore=%path%
set pathone = %1
set PATH=%1;%PATH%
"c:\exe\addpathx.exe" post %1

goto end

:reset
PATH ;
set PATH=%pathbefore%;%PATH%
"c:\exe\winpath.exe" -r %1
goto end

:usage
echo.
echo.
echo		use %0 [Want To Path]
echo		    %0 reset	=	Reset Path Before The First
echo.
echo.
goto end



:end
