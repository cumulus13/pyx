@echo off
title %CD%

sc query "WinAgents EventLog Translation Service"

if %1==start goto start
if %1==stop goto stop
if %1==restart goto restart
if %1==set goto set

goto end


:start
sc start "WinAgents EventLog Translation Service"
goto end

:stop
sc stop "WinAgents EventLog Translation Service"
goto end

:restart
sc stop "WinAgents EventLog Translation Service"
goto start

:set
if %2==auto goto auto 
if %2==manual goto manual 
if %2==disable goto disable 
goto end

:auto
sc config set "WinAgents EventLog Translation Service" start= auto
goto end

:manual
sc config set "WinAgents EventLog Translation Service" start= demand
goto end

:disable
sc config set "WinAgents EventLog Translation Service" start= disabled
goto end

:end