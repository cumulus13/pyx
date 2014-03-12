@echo off
icacls %1 /grant XSERVER:(F)
icacls %1 /grant Everyone:(F)
goto end


:end