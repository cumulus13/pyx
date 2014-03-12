@echo off
if %1== off goto off
goto end



:off
start nircmd monitor off
goto end


:end
