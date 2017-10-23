@echo off
if NOT EXIST "C:\Temp\Me" goto one
cd /d "C:\Temp\Me"

:one
mkdir "C:\Temp\Me"
cd /d "C:\Temp\Me"