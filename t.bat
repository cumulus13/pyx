@echo off
title %CD%
if %1*==* goto start
title "%1"
goto end


:start
title %cd%
goto end


:end
