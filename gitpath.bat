@echo off
title %CD%

set reset=%PATH%

set PATH=c:\msysgit\msysgit\bin;%PATH%
set PATH=c:\msysgit\msysgit\;%PATH%
goto end

if %1==reset goto reset

:reset
PATH ;
set PATH=%reset%
goto end


:end