@echo off
if %2==stop goto stop
if %2==start goto start
got end

:stop
sc config %1 start= demand
sc stop %1
goto end

:start
sc config %1 start= demand
sc start %1
goto end

:end