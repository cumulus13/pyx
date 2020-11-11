@echo off
if %1*==* goto one
"C:\Program Files\Disk Savvy Enterprise\bin\disksavvy.exe" -analyze -dir %*
rem if errorlevel = 1 goto two 
goto end

:two
rem echo two
"C:\Program Files\Disk Savvy Enterprise\bin\disksavvy.exe" -analyze -dir "%1\" %*
goto end

:one
rem echo one
"C:\Program Files\Disk Savvy Enterprise\bin\disksavvy.exe" -analyze -dir "%CD%"\
goto end

:end
