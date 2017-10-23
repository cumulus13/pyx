@echo off
if %1*==* goto usage
if %1==dhcp goto dhcp
if %1==dns goto dns
if %1==-l goto list
if %1==-s goto show
if %1==show goto show

netsh interface ip set address %4 static %1 %2 %3
goto end

:dns
if %2==add goto dnsadd
if %2==del goto dnsdel
netsh interface ip set dnsservers %3 static %2 primary
goto end

:dnsadd
if %5*==* goto dnsaddprimary
netsh interface ip add dnsservers %5 %3 index=%4
goto end

:dnsaddprimary
netsh interface ip add dnsservers %3 static %2 primary
goto end

:dnsdel
netsh interface ip del dnsservers %4 %3
goto end

:dhcp
netsh interface ip set address %2 dhcp
netsh interface ip set dnsservers %2 dhcp
goto end

:list
netsh  interface show interface
netsh  interface ip show interface
goto end

:show
if %2*==* goto show2
netsh interface ip show config %2
goto end

:show2
netsh interface ip show config
goto end

:usage
echo.
echo usage: %0 ip netmask gateway interface         change ip address manual/static
echo        %0 dhcp interface                       change ip and dns to DHCP
echo        %0 dns [add/del] ip [index] interface           change dns address manual
echo        %0 -l                                   List All Interfaces
echo        %0 -s/show show [interface]             show ip address interface
echo.
goto end

:end

