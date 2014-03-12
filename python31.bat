@echo off
call d:\pyx\python31x.py
title %CD%
set PATH=%PATH_BCK%
title Python 3.1

if %1*==* goto one
c:\python31\python.exe %1

goto end

:one
set path=c:\python31;c:\python31\Lib;c:\python31\Lib\site-packages\PyQt4\bin;%path%
set PYTHONPATH=c:\Python31;
set PYTHON_PATH=c:\Python31;c:\PythonApp;
cls
echo.
echo.
echo.
python -V
goto end


:end