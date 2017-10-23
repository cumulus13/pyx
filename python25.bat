@echo off
call d:\pyx\python25x.py
title %CD%
set PATH=%PATH_BCK%
title Python 2.5

if %1*==* goto one
c:\python25\python.exe %1

goto end

:one
set path=c:\python25;c:\python25\Lib;c:\python25\Lib\site-packages\PyQt4\bin;%path%
set PYTHONPATH="c:\Python25;c:\PythonApp\python-vcbrowser;c:\PythonApp\pyHed;c:\PythonApp"
set PYTHON_PATH="c:\Python25;c:\PythonApp\python-vcbrowser;c:\PythonApp\pyHed;c:\PythonApp"
cls
echo.
echo.
echo.
python -V
goto end


:end