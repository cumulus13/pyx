@echo off
title %CD%
set me=%cd%
cd /d "c:\Program Files\Kamus2"
Kamus2.exe
cd /d %me%

goto end

:end

cd /d %me%
