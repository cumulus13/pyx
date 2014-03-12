@echo off
title %CD%
set PATH=%PATH_BCK%
title IronPython 2.6

if %1*==* goto one

"c:\IronPython 2.6 for .NET 4.0\ipy.exe" %1

goto end

:one

set path="c:\IronPython 2.6 for .NET 4.0";%path%
set PYTHONPATH="c:\IronPython 2.6 for .NET 4.0"
cls
echo.
echo.
echo.

ipy -V

goto end


:end