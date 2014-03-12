@echo off
call d:\pyx\python23x.py
title %CD%
set PATH=%PATH_BCK%
title Python 2.3

if %1*==* goto one
c:\python23\python.exe %1

goto end

:one
set path=c:\python23;c:\python23\Lib;%path%
set PYTHONPATH="c:\Python23;c:\PythonApp\python-vcbrowser;c:\PythonApp\pyHed;c:\PythonApp"
cls
echo.
echo.
echo.
python -V
goto end


:end