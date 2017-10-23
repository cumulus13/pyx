@echo off
if %1*==* goto usage
if %1==config goto config
goto end

:config
start notepad2 "e:\wampserver\www3\viewgit\inc\localconfig.php"
goto end

:usage
echo.
echo.      use : %0 config
echo.
goto end

:end