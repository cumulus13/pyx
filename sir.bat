@echo off 
if %1*==* goto one

dir /o:d %1 | tail -n 50
goto end

:one
dir /o:D | tail -n 50 
goto end

:end
