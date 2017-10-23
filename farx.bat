@echo off

if %1*==* goto one
start call "c:\Program Files\Far2\Far.exe" %1
goto end

:one 
start call "c:\Program Files\Far2\Far.exe" %CD%
goto end

:end