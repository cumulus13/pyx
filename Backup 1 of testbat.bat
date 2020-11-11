@@echo off

rem SET PATH_%~n0 = %PATH%
rem goto end

echo %%~1 : %~1
echo FULL PATH                      (%%~f) : %~f1
echo DIRECTORY                      (%%~d) : %~d1
echo PATH                           (%%~p) : %~p1
echo FILE NAME ONLY                 (%%~n) : %~n1
echo EXTENSION ONLY:                (%%~x) : %~x1
echo EXPANDED PATH WITH SHORT NAMES (%%~s) : %~s1
echo ATTRIBUTES                     (%%~a) : %~a1
echo DATE AND TIME                  (%%~t) : %~t1
echo SIZE                           (%%~z) : %~z1
echo DRIVE + PATH                   (%%~dp): %~dp1
echo NAME.EXT                       (%%~nx): %~nx1
echo FULL PATH + SHORT NAME         (%%~fs): [37m[46m%~fs1[0m[0m
ECHO.
ECHO. 
ECHO. 
goto end

:TEST001
rem SETLOCAL ENABLEEXTENSIONS
SET PATH1=%PATH%
ECHO PATH0=[93m%PATH%[0m
SET BEFORE=%~1
SET AFTER=%~2
ECHO [104m BEFORE= %BEFORE% [0m
ECHO [104m AFTER=%AFTER% [0m
rem SET PATH="%PATH:!BEFORE!=!AFTER!%"
CALL SET PATH=%%PATH:%BEFORE%=%AFTER%%%
ECHO [101;97mPATH1=%PATH%[0m
goto end

:BLINK_COLOR_DISPLAY
set NUM=0 1 2 3 4 5 6 7 8 9 A B C D E F
for %%x in (%NUM%) do (
    for %%y in (%NUM%) do (
        color %%x%%y
        timeout 1 >nul
    )
)
goto end

:end
rem SET PATH=%PATH1%
rem ECHO PATH=%PATH%
rem ECHO [101;93m  PATH_%~n0=%PATH_^%~n0%  [0m
rem SET count=1
rem FOR /F %%A in ('dir /b') DO (
rem 	ECHO %count%:%%A
rem 	SET /a count+=1
rem )
SET REPLACEMENT_01=c:\ProgramData\Anaconda2
SET REPLACEMENT_02=c:\ProgramData\Python37
SET REPLACEMENT_03=c:\Python37
SET REPLACEMENT_04=c:\Python27
SET REPLACEMENT_05=c:\Python26
SET REPLACEMENT_06=c:\Anaconda2
SET REPLACEMENT_07=c:\Anaconda3

SET REPLACEMENT=c:\ProgramData\Anaconda2;c:\ProgramData\Python37;c:\Python37;c:\Python27;c:\Python26;c:\Anaconda2;c:\Anaconda3
SET DEST_REPLACEMENT=c:\AnacondaXXX

FOR %%i in (
	%REPLACEMENT_01%
	%REPLACEMENT_02%
	%REPLACEMENT_03%
	%REPLACEMENT_04%
	%REPLACEMENT_05%
	%REPLACEMENT_06%
	%REPLACEMENT_07%
) DO (
	echo %%i
	CALL SET REPLACEMENT=%%REPLACEMENT:%%i=%DEST_REPLACEMENT%%%
)


PROMPT [101;93m $P$G [0m
PROMPT $P$G