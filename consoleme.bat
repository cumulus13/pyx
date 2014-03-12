@echo off
title %CD%

if %1*==* goto 

"c:\console\console.exe" "c:\Console\console_small.xml" -c  "/k %1 %2"

goto end


:end