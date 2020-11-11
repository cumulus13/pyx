@echo off
if %1*==* goto usage
if NOT %1*==* goto one
echo NO ACTION
goto EOF

:one
SETLOCAL ENABLEEXTENSIONS
set ATTR=%~a1
set DIRATTR=%ATTR:~0,1%
if /I "%DIRATTR%"=="d" (
	echo %1 is a folder
) else (
	echo %1 not a folder
)
goto EOF
:usage
if DEFINED TEMP2 echo DEFINED
echo please read script
goto EOF
:EOF

