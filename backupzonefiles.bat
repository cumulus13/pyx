@echo off
del "d:\BACKUP_DATA\ZoneFiles.zip"
7z a "d:\BACKUP_DATA\ZoneFiles.zip" "C:\Documents and Settings\All Users\Application Data\JH Software\Simple DNS Plus\ZoneFiles"
goto end


:end