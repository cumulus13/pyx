@echo off
pip install %1
echo ERROR LEVEL %errorlevel%
if %errorlevel% == 1 goto reinstall
goto end

:reinstall
"c:\Program Files (x86)\Growl for Windows\growlnotify.exe" /r:PIPX "ERROR LEVEL: %errorlevel%" /t:pip /n:PIPX /a:PIPX /i:c:\TOOLS\pyx\Bug.png
pip install %1
goto end

:end
if %errorlevel% == 1 goto reinstall