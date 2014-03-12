@echo off
call d:\pyx\python32x.py
title %CD%
set PATH=%PATH_BCK%
title Python 3.2

if %1*==* goto one
c:\python32\python.exe %1

goto end

:one
set path=c:\python32;c:\python32\Lib;c:\python32\Lib\site-packages\PyQt4\bin;%path%
set PYTHONPATH=c:\Python32;
set PYTHON_PATH=c:\Python32;c:\PythonApp;
cls
echo.
echo.
echo.
python -V
goto end


:end