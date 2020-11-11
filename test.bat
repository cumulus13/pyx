@echo off
echo    %%~1 = %~1            expands %I removing any surrounding quotes (")
echo    % %~f1 = %~f1            expands %I to a fully qualified path name
echo    %%~d1 = %~d1                                       expands %I to a drive letter only
echo    %%~p1 = %~p1                      expands %I to a path only
echo    %%~n1 = %~n1                                    expands %I to a file name only
echo    %%~x1 = %~x1                                     expands %I to a file extension only
echo    %%~s1 = %~s1             expanded path contains short names only
echo    %%~a1 = %~a1                              expands %I to file attributes of file
echo    %%~t1 = %~t1                         expands %I to date/time of file
echo    %%~z1 = %~z1                                  expands %I to size of file
echo    %%~$PATH:1 = %~$PATH:1      searches the directories listed in the PATH
echo                                                    environment variable and expands %I to the
echo                                                    fully qualified name of the first one found.
echo                                                    If the environment variable name is not
echo                                                    defined or the file is not found by the
echo                                                    search, then this modifier expands to the
echo                                                    empty string
echo                                                    The modifiers can be combined to get compound results:

echo    %%~dp1 = %~dp1                   expands %I to a drive letter and path only
echo    %%~nx1 = %~nx1                               expands %I to a file name and extension only
echo    %%~fs1 = %~fs1            expands %I to a full path name with short names only
echo    %%~dp$PATH:1 = %~dp$PATH:1             searches the directories listed in the PATH
echo                                                    environment variable for %I and expands to the
echo                                                    drive letter and path of the first one found.
echo    %%~ftza1 = %~ftza1        expands %I to a DIR like output line

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
REM  echo off
REM  if %1==test (
	REM  goto test
REM  ) else if %1==test2 (
	REM  echo test x
REM  ) else (
	REM  goto test1
REM  )
REM  goto end

REM  :test
REM  echo.
REM  echo TEST
REM  echo.
REM  goto end

REM  :test1
REM  echo.
REM  echo TEST 1
REM  echo.
REM  goto end

REM  :end

echo off