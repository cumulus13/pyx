@echo off
if %1*==* goto usage
rem if EXIST %3 goto three

rem "C:\Windows\System32\netsh.exe" interface ip set dns name="Local Area Connection" source=static addr=%1 register=primary

rem "C:\Windows\System32\netsh.exe" interface ip add dns name="Local Area Connection" addr=%2 index=2
rem goto end

rem :three
"C:\Windows\System32\netsh.exe" interface ip set dns name=%3 source=static addr=%1 register=primary

"C:\Windows\System32\netsh.exe" interface ip add dns name=%3 addr=%2 index=2
goto end

:usage
echo.
echo usage: %0 DNS1 DNS2
echo.
goto end

:end
