@echo off
title %CD%
set PATH=%PATH_BCK%
title PythonNet with Python23

if %1*==* goto one
c:\PythonNet\python.exe %1

goto end

:one
set path=c:\PythonNet;%path%
set PYTHONPATH="c:\PythonNet"
cls
echo.
echo.
echo.
python -V
goto end


:end