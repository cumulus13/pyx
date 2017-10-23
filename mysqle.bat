@echo off
title %CD%

"d:\xampp\mysql\bin\mysql.exe" -uroot -pblackid %1 -e "%2"
goto end


:end

