@echo off
title %CD%
set me=%cd%
cd /d "h:\Program Files\Kamus2"
Kamus2.exe
cd /d %me%

goto end

:end

cd /d %me%
