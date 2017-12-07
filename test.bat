@echo off
REM  set x='exit' 
REM  rem echo %x%
REM  echo exit ? 
REM  set x=
REM  PAUSE
REM  echo x=%x%
rem if %x%=='exit' echo exit

REM  set word=table
REM  echo word=%word%
REM  set str="jump over the chair"
REM  echo str 0 = %str%
REM  call set str=%%str:chair=%word%%%
REM  echo str 1 = %str%

REM  setlocal enabledelayedexpansion
REM  set data=HELLO ROOT
REM  echo data 0 = %data%
REM  set search=ROOT
REM  echo search=%search%
REM  set replace=BLACKID
REM  echo replace=%replace%
REM  set "data=!data:%search%=%replace%!"
REM  echo data 1 = %data%
REM  Use %data% here before calling endlocal.
REM  endlocal
REM  echo on
REM  if exist %2 goto error1
REM  if exist %3 goto error2
REM  goto end

REM  :error1
REM  echo ERROR 1
REM  goto end

REM  :error2
REM  echo ERROR 2
REM  goto end

REM  :end
echo off
if %1==test (
	goto test
) else if %1==test2 (
	echo test x
) else (
	goto test1
)
goto end

:test
echo.
echo TEST
echo.
goto end

:test1
echo.
echo TEST 1
echo.
goto end

:end