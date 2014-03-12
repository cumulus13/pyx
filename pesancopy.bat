@echo off
title %CD%
echo.
echo.
echo.
if not exist "u:\PESAN3.txt"  goto error
copy "e:\test\PESAN3.txt" u:\
copy "e:\test\PESAN3.txt" "e:\test\PESAN3-Sudah.txt"
if not exist "u:\"  goto error
copy "e:\test\PESAN3-Sudah.txt" u:\
echo.
echo.
goto end

:error
echo.
echo.
echo      Drive dan File Tidak ditemukan !!!!!!
echo.
echo.
goto end


:end
