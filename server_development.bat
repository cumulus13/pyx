@echo off
if %1==start goto start
if %1==restart goto restart
if %1==stop goto stop
goto end

:start
sc start gitblit
sc start gitedit
sc start gitdownload
sc start scmcenter
sc start fileserver
sc start pypiserver
sc start "wing ftp server"
sc start apache249
sc start wampmysqld
sc start NAWebServer
sc start subsonic
sc start hgserver
goto end

:stop
sc stop gitblit
sc stop gitedit
sc stop gitdownload
sc stop scmcenter
sc stop fileserver
sc stop pypiserver
sc stop "wing ftp server"
sc stop apache249
sc stop NAWebServer
sc stop subsonic
sc stop hgserver
goto end

:restart
pyservice gitblit restart
pyservice  gitedit restart
pyservice  gitdownload restart
pyservice  scmcenter restart
pyservice  fileserver restart
pyservice  pypiserver restart
pyservice  "wing ftp server" restart
pyservice  apache249 restart
pyservice NAWebServer restart
pyservice subsonic restart
pyservice hgserver restart
goto end

:end
echo.
echo script by LICFACE
echo.
