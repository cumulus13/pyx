@echo off
set me=%CD%
cd /D "c:\Ruby244\msys64\usr\bin"
bash.exe -l
rem set MSYSTEM=MINGW32

rem set MSYSCON=sh.exe

rem start %COMSPEC% /C sh.exe --login -i
cd /D %me%
