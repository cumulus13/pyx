@echo off
if %1*==* goto one
echo %1|clip
goto end

:one
echo "%cd%" | clip
goto end


:end