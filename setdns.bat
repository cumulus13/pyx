@echo off
if %1*==* goto usage

"C:\Windows\System32\netsh.exe" interface ip set dns name="Local Area Connection" source=static addr=%1 register=primary

"C:\Windows\System32\netsh.exe" interface ip add dns name="Local Area Connection" addr=%2 index=2
goto end

:usage
echo.
echo usage: %0 DNS1 DNS2
echo.
goto end

:end