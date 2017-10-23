@echo off
title %CD%

if %1*==* goto usage
if %1==edit goto edit
if %1==read goto read

:read
cls
echo.
echo.
cat "E:\InstantRails-2.0-win\apache\conf\httpd.conf"
goto end

:edit
cls
echo.
echo.
echo.
start /B c:\Ruby\scite\SciTE.exe "E:\InstantRails-2.0-win\apache\conf\httpd.conf"
goto end

:usage
echo.
echo.
echo	use : %0 read / edit
echo.
echo.
goto end

:end


