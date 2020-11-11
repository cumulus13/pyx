@echo off
set MAX_RETRY=10
set /a COUNT_RETRY=1
easy_install %1
echo ERROR LEVEL %errorlevel%
if %errorlevel% == 1 goto reinstall
goto end

:reinstall
if %COUNT_RETRY%==%MAX_RETRY% goto end1
set /a COUNT_RETRY+=1
"c:\Program Files (x86)\Growl for Windows\growlnotify.exe" /r:EIX "ERROR LEVEL: %errorlevel%" /t:easy_install /n:EIX /a:EIX /i:c:\TOOLS\pyx\Bug.png
easy_install %1
goto end

:end
set /a COUNT_RETRY+=1
if %errorlevel% == 1 goto reinstall
goto end1

:end1

rem @echo off
rem  set /a x=0
rem  :while
rem  if %x% lss 5 (
rem    echo %x%
rem    pause>nul
rem    set /a x+=1
rem    goto :while
rem  )
rem  echo Test :D