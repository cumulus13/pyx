@echo off
if %1==wallpaper goto wallpaper
goto end

:wallpaper
echo Still Develop, the file must convert to BMP format before ... !
reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v Wallpaper /t REG_SZ /d %1 /f
RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters

:end