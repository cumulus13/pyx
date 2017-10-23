@echo off
title %CD%
7z x %1 -o%2
"c:\Apps\Snarl_CMD_1.0\Snarl_CMD.exe" snShowMessage 20 "7zx [7z x]" "DONES" "f:\ICONS\7z.png"
goto end

:end
