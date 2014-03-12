@echo off
title %CD%

if %1*==* goto usage
if %1==1 goto one
if %1==2 goto dua



:one
"C:\Program Files\GatherBird\CopyLargeFiles25\CopyLargeFiles.exe" 
goto end

:dua
"C:\Program Files\GatherBird\CopyLargeFiles25\DotNetCopyLargeFiles.exe"
goto end

:usage
echo.
echo.
echo      usage: %0 1 [CopyLarge Original]
echo                  %0 2 [CopyLarge DotNet]
echo.
echo.
goto end

:end
