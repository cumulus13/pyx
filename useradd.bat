@echo off

if %1*==* goto usage
net user %1 %2 /add
net localgroup %3 %1 /add
wmic USERACCOUNT WHERE "Name='%1'" set PasswordExpires=FALSE

goto end


:usage
echo.
echo usage: %0 [username] [password] [group]
echo. 
goto end

:end