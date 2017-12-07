@echo off
takeown /f	%1
icacls %1 /grant root:(F)
icacls %1 /grant Everyone:(F)
goto end


:end
