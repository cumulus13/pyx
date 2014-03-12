@echo off
title %CD%
if %1*==* goto usage
if %1==-t goto total
if %1==-s goto size
if %1==-d goto detail

c:\cygwin\bin\du -s -h %1
goto end

:size
c:\cygwin\bin\du -h --max-depth=1 %2
goto end

:detail
c:\cygwin\bin\du -h -a --max-depth=1 %2
goto end


:total
c:\cygwin\bin\du -s -h %2
goto end

:usage
echo.
echo.
echo		use %0 -t [total of File or Directory]
echo               -s [total of size each folder]
echo               -d [detail of each folder]
echo		    %0 [File or Directory]
echo            Default is this directory
echo.
echo.
echo  please wait ..............
echo.
c:\cygwin\bin\du -s -h %CD%
goto end

:end
t