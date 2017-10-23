@echo off
title %CD%

if %1*==* goto usage
if %1==edit goto edit
if %1==read goto read
if %1==backup goto backup

:read
cls
echo.
echo.
cat "D:\xampp\apache\conf\httpd.conf"
goto end

:edit
cls
echo.
echo.
echo.
start /b c:\Ruby\scite\SciTE.exe "D:\xampp\apache\conf\httpd.conf"
goto end

:backup
xamppbackup.py
goto end

:usage
echo.
echo.
echo	use : %0 read / edit
echo.
echo.
goto end

:end


