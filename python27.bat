@echo off

title %CD%
set PATH=%PATH_BCK%
title Python 2.7

if %1*==* goto one
c:\python25\python.exe %1

goto end

:one
set path=c:\python27;c:\python27\Lib;c:\python27\Lib\site-packages\PyQt4\bin;%path%
set PYTHONPATH="c:\Python27;c:\PythonApp\python-vcbrowser;c:\PythonApp\pyHed;c:\PythonApp"
set PYTHON_PATH="c:\Python27;c:\PythonApp\python-vcbrowser;c:\PythonApp\pyHed;c:\PythonApp"
cls
echo.
echo.
echo.
python -V
goto end


:end