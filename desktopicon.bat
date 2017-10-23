@echo off
if %1*==* goto usage
if %1==hide goto hide
if %1==show goto show
goto end

:hide
move /Y "C:\Documents and Settings\root\Desktop"\*.lnk "d:\Link\Adm" > c:\temp\null
move /Y "C:\Documents and Settings\All Users\Desktop"\*.lnk "d:\Link\Als" > c:\temp\null
goto end

:show
move /Y "d:\Link\Adm"\*.lnk "C:\Documents and Settings\root\Desktop" > c:\temp\null
move /Y "d:\Link\Als"\*.lnk "C:\Documents and Settings\All Users\Desktop" > c:\temp\null
goto end

:usage
echo.
echo        use : %0 [hide/show]
echo.
goto end

:end

