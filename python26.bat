@echo off
call d:\pyx\python26x.py
rem FTYPE Python.CompiledFile="C:\Python26\python.exe" "%1" %*
rem FTYPE Python.File="c:\Python26\python.exe" "%1" %*
rem FTYPE Python.NoConFile="C:\Python26\pythonw.exe" "%1" %*
title %CD%
set PATH=%PATH_BCK%
title Python 2.6

if %1*==* goto one
c:\python26\python.exe %1

goto end

:one
set path=c:\python26;c:\python26\Lib;c:\python26\Lib\site-packages\PyQt4\bin;%path%
set PYTHONPATH=c:\Python26;
set PYTHON_PATH=c:\Python26;c:\PythonApp;
cls
echo.
echo.
echo.
python -V
goto end


:end