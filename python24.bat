@echo off
call d:\pyx\python24x.py
title %CD%
set PATH=%PATH_BCK%
title Python 2.4

if %1*==* goto one
c:\python25\python.exe %1

goto end

:one
set path=c:\python24;%path%
set PYTHONPATH="c:\Python24;c:\PythonApp\python-vcbrowser;c:\PythonApp\pyHed;c:\PythonApp"
cls
echo.
echo.
echo.
python -V
goto end


:end