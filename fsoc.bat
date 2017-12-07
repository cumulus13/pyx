@echo off
if %1*==* goto usage

set ftypename=%1
set extension=%2
set pathtoexe=%3
set pathtoicon=""
if %pathtoicon%=="" set pathtoicon=%pathtoexe%,0
REG ADD HKEY_CLASSES_ROOT\%extension%\ /t REG_SZ /d %ftypename% /f
REG ADD HKLM\SOFTWARE\Classes\%ftypename%\DefaultIcon\ /t REG_SZ /d %pathtoicon% /f
ftype %ftypename%=%pathtoexe% "%%1" %%*
assoc %extension%=%ftypename%
goto end

:usage
echo.
echo USAGE: %0 [FTYPE_NAME] [.EXT] [EXE_PATH]
echo.
goto end

:end