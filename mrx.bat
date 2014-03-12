@echo off
if %1*==* goto help

mkdir %2\%1
c:\exe\mirror.exe %1 %2\%1

:help
echo.
echo  Usage: %0 [source] [destination]
echo.


