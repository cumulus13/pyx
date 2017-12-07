@echo off
set PATH1=%PATH%
if %1*==* goto usage
if %1==-r goto remove
if %1==--remove goto remove
set path=%1;%PATH%
echo PATH 0 = %PATH%
goto end

:remove
set INPUT=
set INPUT=%2
set CLR=""
echo INPUT = %INPUT%
rem SET "PATH=!PATH:c:\SDK\Anaconda2=%VIRTUAL_ENV%!"
echo PATH 1 = %PATH%
goto end1

:usage
echo.
echo USAGE: %~n0 [dir path to add]
echo              -r, --remove [dir path to remove]
echo.
goto end

:end1
set PATH=%PATH1%

:end
