@echo off
if %1==restart goto restart
goto end

:restart
service dnscache restart & service named restart & ipconfig /flushdns & ipconfig /flushdns & ipconfig /flushdns & ipconfig /flushdns
goto end

:start
echo not yet
goto end

:end
