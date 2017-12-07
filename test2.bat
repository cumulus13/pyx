@echo off
SET VER01=
echo VER 0=%VER%
rem echo %path% | findstr /i /c:"%1" >nul && echo Variable contains the string "%1" || echo Variable does not have the string "%1"
echo %path% | findstr /i /c:"%1" >nul && SET VER=1 || SET VER=0
echo VER 1=%VER%

if %VER%==1 (
	echo "ADA"
) else (
	echo "TIDAK ADA"
)

SET /P TEST=Do you want to add ?:
echo TEST=%TEST%