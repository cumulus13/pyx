@echo off
title %CD%
cls
call mute
echo.
echo.
shutdown -r -t %1 -c "WARNING !.............,This Computer Will be Restart / Reboot in %1Second(s) without fast"
echo		This Computer Will be Restart / Reboot in %1 Second
echo.
echo.
goto end


:end
"d:\EXE\CloseAll.exe"