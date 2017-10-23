@echo off
title %CD%

if %1*==* goto one

control "c:\WINDOWS\System32\%1.cpl"
goto end

:one
dir c:\WINDOWS\System32\*.cpl | more
rem dir d:\pyx\%1*.bat | more
goto end


:end
