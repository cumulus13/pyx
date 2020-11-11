@echo off
if %1*==* goto usage
if %1==open goto open
if %1==close goto close
if %1==bypass goto bypass

goto end

:open
netsh advfirewall firewall add rule name=open_%2_%3 localport=%2 dir=%3 protocol=%4 action=allow
goto end

:close
netsh advfirewall firewall add rule name=open_%2_%3 localport=%2 dir=%3 protocol=%4 action=block
goto end

:bypass
netsh advfirewall firewall add rule name=open_%2_%3 localport=%2 dir=%3 protocol=%4 action=bypass
goto end

:usage
echo.
echo usage: fwc [open/close/bypass] PORT [IN/OUT] [TCP/UDP]
echo.
:goto end

:end
echo EL=%errorlevel%