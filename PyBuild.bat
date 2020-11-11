@echo off

SET move=1
SET DELFIRST=1

SET ARGV1=%1
SET ARGV2=%2

REM  echo ARGV1=%ARGV1%
REM  echo ARGV2=%ARGV2%

if DEFINED ARGV1 (
	if %ARGV1%x==--no-movex SET move=0
	if %ARGV1%x==--no-deletex SET DELETEFIRST=0
	REM echo move=%move%
)

if DEFINED ARGV2 (
   if %ARGV2%x==--no-deletex SET DELETEFIRST=0
   if %ARGV2%x==--no-movex SET move=0
)

REM  echo move=%move%
REM  echo DELETEFIRST=%DELETEFIRST%
goto main

:usage
echo.
echo Usage: %0 --no-delete Don't Delete dist and build directory
echo           --no-move  Don't Move dist to PYTHON_MODULES dir
goto end

:main
if %DELFIRST% == 1 (
	echo cleanup first ...
	echo remove build/ dist/ ...
	rmdir /s /q build
	rmdir /s /q dist
)

echo bdist_wheel for python3 ...
c:\SDK\Anaconda3\python.exe setup.py bdist_wheel
c:\SDK\Anaconda3\python.exe setup.py sdist
rmdir /s /q build

echo bdist_wheel for python2 ...
c:\SDK\Anaconda2\python.exe setup.py bdist_wheel
rem c:\SDK\Anaconda2\python.exe setup.py sdist

if %move% == 1 (
	echo move module to y:\PYTHON_MODULES  ...
	move /y dist\* y:\PYTHON_MODULES
)

if %DELFIRST% == 1 (
	echo cleanup last ...
	echo remove build/ ...
	rmdir /s /q build
	REM rmdir /s /q dist
)

goto end

:end