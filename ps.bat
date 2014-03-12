@echo off
title %CD%
if %1*==* goto usage
if %1== -aux goto aux
if %1== -F goto F
if %1== -V goto V


:aux
tasklist 
goto end

:F
tasklist /V
goto end

:V
tasklist /SVC
goto end

:usage
echo.
echo.
echo		usage : %0 -aux [for list all service simple print]
echo		        %0 -F	[for list all service with add info]
echo			%0 -V	[for list all service with full print]
echo.
echo.
goto end

:end
