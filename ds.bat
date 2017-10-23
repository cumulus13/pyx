@echo off
if %1*==* goto one
"c:\Program Files\Disk Savvy Ultimate\bin\disksavvy.exe" -analyze -dir %*
rem if errorlevel = 1 goto two 
goto end

:two
rem echo two
"c:\Program Files\Disk Savvy Ultimate\bin\disksavvy.exe" -analyze -dir "%1\" %*
goto end

:one
rem echo one
"c:\Program Files\Disk Savvy Ultimate\bin\disksavvy.exe" -analyze -dir %CD%\
goto end

:end
