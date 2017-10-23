@echo off
if %1*==* goto usage
start /B call "c:\Program Files\Notepad++\notepad++.exe" %1
goto end

:usage
echo.
echo      use: %0 [file to edit/open]
echo.
goto end

:end