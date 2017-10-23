@echo off
if %1*==* goto help
if %1==stop goto stop
if %1==start goto start
if %1==restart goto restart
goto end

:start
echo starting VNCServer Service ...
sc start vncserver > NUL
echo running GomTray ...
"c:\Program Files\GRETECH\GOMTray\GomTray.exe"
echo running aWARemote Server ...
"c:\Program Files\aWARemote Server\aWARemote Server.exe"
goto end

:stop
echo stopping VNCServer Service ...
sc stop vncserver > NUL
echo stopping GomTray ...
px -k "GomTray.exe" > NUL
echo stopping aWARemote Server ...
px -k "aWARemote Server.exe" > NUL
goto end

:restart
echo stopping VNCServer Service ...
sc stop vncserver > NUL
echo stopping GomTray ...
px -k "GomTray.exe" > NUL
echo stopping aWARemote Server ...
px -k "aWARemote Server.exe" > NUL
goto start

:help
echo.
echo use %0 [start/stop/restart]
goto end

:end