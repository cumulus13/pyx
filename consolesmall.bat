@echo off
title %CD%

"c:\console\console.exe" "c:\console\console_small.xml"
goto end

:end
taskkill /f /im consolesmall.exe
exit
