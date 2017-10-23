@echo off
title %CD%
if %1*==* goto usage
if %1== -aux goto aux
if %1== -F goto F
if %1== -V goto V

c:\cygwin\bin\ps.exe %*
goto end
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
rem echo.
rem echo.
rem echo		usage : %0 -aux [for list all service simple print]
rem echo		        %0 -F	[for list all service with add info]
rem echo			%0 -V	[for list all service with full print]
rem echo.
rem echo.
c:\cygwin\bin\ps.exe -h
goto end

:end
