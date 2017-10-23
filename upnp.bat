@echo off
if %1*==* goto usage
if %1==start goto start
if %1==stop goto stop
if %1==auto goto auto
if %1==disable goto disable
if %1==status goto status
if %1==restart goto restart
if %1==config goto config
if %1==manual goto manual
goto end

:config
if %2*==* goto usage2
if %2==manual goto manual
if %2==auto goto auto
if %2==disable goto disable
goto end

:manualx
sc config limbo start= demand
sc config "PS3 Media Server" start= demand
sc config Serviio start= demand
sc config "TVersityMediaServer" start= demand
sc config tvMobiliService start= demand
sc config TwonkyMedia start= demand
sc config upnphost start= demand
rem sc config 
rem sc config 
goto end

:auto
sc config limbo start= auto
sc config "PS3 Media Server" start= auto
sc config Serviio start= auto
sc config "TVersityMediaServer" start= auto
sc config tvMobiliService start= auto
sc config TwonkyMedia start= auto
sc config upnphost start= auto
rem sc config 
rem sc config 
goto end

:disable
sc config limbo start= disabled
sc config "PS3 Media Server" start= disabled
sc config Serviio start= disabled
sc config "TVersityMediaServer" start= disabled
sc config tvMobiliService start= disabled
sc config TwonkyMedia start= disabled
sc config upnphost start= disabled
rem sc config 
rem sc config 
goto end

:start
sc start limbo
sc start "PS3 Media Server"
sc start Serviio
sc start "TVersityMediaServer"
sc start tvMobiliService
sc start TwonkyMedia
sc start upnphost
goto end

:stop
sc stop limbo
sc stop "PS3 Media Server"
sc stop Serviio
sc stop "TVersityMediaServer"
sc stop tvMobiliService
sc stop TwonkyMedia
sc stop upnphost
goto end

:restart
net stop limbo
net start limbo
net stop "PS3 Media Server"
net start "PS3 Media Server"
net stop Serviio
net start Serviio
net stop "TVersityMediaServer"
net start "TVersityMediaServer"
net stop tvMobiliService
net start tvMobiliService
net stop TwonkyMedia
net start TwonkyMedia
net stop upnphost
net start upnphost
goto end

:status
sc query limbo
sc qc limbo
sc query "PS3 Media Server"
sc qc "PS3 Media Server"
sc query Serviio
sc qc Serviio
sc query "TVersityMediaServer"
sc qc "TVersityMediaServer"
sc query tvMobiliService
sc qc tvMobiliService
sc query TwonkyMedia
sc qc TwonkyMedia
sc query upnphost
sc qc upnphost
goto end

:usage
echo.
echo.
echo Usage: %0 [start/stop/restart/status/config/manual/auto/disable]
echo        %0 config [manual/auto/disable]
echo.
goto end

:usage2
echo.
echo.
echo Usage: %0 config [manual/auto/disable]
echo.
goto end

:end