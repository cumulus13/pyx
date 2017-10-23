@echo off
set me=%CD%
cd /D "C:\msys\1.0\bin"

set MSYSTEM=MINGW32

set MSYSCON=sh.exe

start %COMSPEC% /C sh.exe --login -i
cd /D %me%