@echo off
title %CD%
echo.
echo.
echo.
if not exist "p:\PESAN3.txt"  goto error
copy "e:\test\PESAN3.txt" "e:\test\PESAN3-Sudah.txt"
copy "p:\PESAN3.txt" "e:\test\PESAN3.txt" 
if not exist "p:\"  goto error
copy "e:\test\PESAN3-Sudah.txt" p:\
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