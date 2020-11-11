@echo off
if %1*==* goto usage
if %1==add goto add
rem if EXIST %3 goto three

rem "C:\Windows\System32\netsh.exe" interface ip set dns name="Local Area Connection" source=static addr=%1 register=primary

rem "C:\Windows\System32\netsh.exe" interface ip add dns name="Local Area Connection" addr=%2 index=2
rem goto end

rem :three

rem netsh interface ip set dns name=%3 source=static addr=%1 register=primary
netsh interface ip set dnsserver %3 static %1 primary
if NOT %2==0 (
	netsh interface ip add dnsserver %3 %2 index=2
)
rem netsh interface ip add dns name=%3 addr=%2 index=2
goto end

:add
if %3==1 goto add2
netsh interface ip add dns name=%4 addr=%2 index=%3
goto end

:add2
rem netsh interface ip set dns name=%4 source=static addr=%2 register=primary
netsh interface ip set dnsserver %4 static %2 primary
goto end

:usage
echo.
echo usage: %0 DNSIP1 DNSIP2 DEVICE (add primary and index2)
echo        %0 add DNSIP INDEX DEVICE (add index)
echo.
goto end

:end
