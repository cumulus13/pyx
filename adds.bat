@echo off
title %CD%
if %1*==* goto usage
if %1==on goto ON
if %1==off goto OFF
if %1==edit goto edit


:OFF
rem if EXIST "C:\WINDOWS\system32\drivers\etc\hosts2" goto warning1
copy "C:\WINDOWS\system32\drivers\etc\hosts" "C:\WINDOWS\system32\drivers\etc\adds\hostsx" 
copy "C:\WINDOWS\system32\drivers\etc\ns2\hosts" "C:\WINDOWS\system32\drivers\etc\hosts" > nul
echo.
echo.
echo		Adds Local Has been OFF.
echo.
echo.
echo		Do you want to Start DNS Local Setting [press Enter to Accept or Ctrl + C to Cancel]
echo.
pause > nul
echo
dnslocal on
goto end

:ON
rem if EXIST "C:\WINDOWS\system32\drivers\etc\hosts" goto warning2
del "C:\WINDOWS\system32\drivers\etc\hosts"
copy "C:\WINDOWS\system32\drivers\etc\adds\hosts" "C:\WINDOWS\system32\drivers\etc\hosts" 
rem copy "C:\WINDOWS\system32\drivers\etc\ns1\hosts" "C:\WINDOWS\system32\drivers\etc\hosts" > nul
echo.
echo.
echo		Adds Local Has been ON.
echo.
goto end

:warning1
echo.
echo.
echo		Adds Already OFF
echo.
goto end

:edit
"c:\Program Files\EditPlus 2\editplus.exe"  "C:\WINDOWS\system32\drivers\etc\adds\hosts"
goto ON

:warning2
echo.
echo.
echo		Adds Already ON
echo.
goto end

:usage
echo.
echo.
echo		Usage : %0 ON   [Start Service query of DNS Local
echo		        %0 OFF  [Stop Service query of DNS Local
echo.
echo.
goto end

:end
