@echo off
title %CD%
del "c:\WINDOWS\Prefetch\*.pf"
goto end


:end
dir "c:\WINDOWS\Prefetch"

