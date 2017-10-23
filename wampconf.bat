@echo off
title %CD%

if %1*==* goto usage
if %1==edit goto edit
if %1==read goto read

:read
cls
echo.
echo.
cat "e:\wampserver\bin\apache\Apache2.2.11\conf\httpd.conf"
goto end

:edit
cls
echo.
echo.
echo.
start /b c:\Ruby\scite\SciTE.exe "e:\wampserver\bin\apache\Apache2.2.11\conf\httpd.conf"
goto end

:usage
echo.
echo.
echo	use : %0 read / edit
echo.
echo.
goto end

:end


