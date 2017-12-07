@echo off
C:\EXE\snarlcmd.exe snShowMessageEx USBSafelyRemove 10 "Plugging" "Drive %DriveLetter%%Label% (%DeviceName% - %PhysicalDriveName% - %PnPName% Inserted(plugging)" beforestopping d:\ICONS\usbsafelyremove_transparant.png

"c:\Program Files\Growl for Windows\growlnotify.exe" /ai:d:\ICONS\usbsafelyremove_transparant.png  /a:"USBSafelyRemove" /n:"AfterPlugging" /t:USBSafelyRemove "Drive %DriveLetter%%Label% (%DeviceName% - %PhysicalDriveName% - %PnPName% Removed(Unplugging)"


:end
