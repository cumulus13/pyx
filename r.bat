@echo off
title %CD%

if %1*==* goto usage
if %1==-d goto directory
if %1==-a goto all

tree /A %1
goto end

:directory
tree /A %2
goto end

:all
tree /A /F %2
goto end

:usage
echo.
echo     use: %0 -d [Directory Only]
echo            -a [All with subdirectory]
echo.
goto end

:end