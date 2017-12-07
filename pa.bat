@echo off
if %1*==* goto usage
if %1==-r (
	goto remove
) else if %1==--remove (
	goto remove
) else (
	goto add
)
goto end

:remove
SET VER_USER=
SET VER_SYSTEM=
SET VER_ACTION_USER=
SET VER_ACTION_SYSTEM=
set USER_PATH=
set SYSTEM_PATH=
set INPUT_USER=
set INPUT_SYSTEM=

FOR /F "tokens=* USEBACKQ" %%F IN (`reg query "HKCU\Environment" /v Path`) DO (
	SET USER_PATH=%%F
)

FOR /F "tokens=* USEBACKQ" %%F IN (`reg query "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v Path`) DO (
	SET SYSTEM_PATH=%%F
)

rem ECHO USER_PATH 0=%USER_PATH%
SET USER_PATH=%USER_PATH:REG_SZ    =%
SET USER_PATH=%USER_PATH:Path    =%
REM ECHO USER_PATH=%USER_PATH%

SET SYSTEM_PATH=%SYSTEM_PATH:REG_EXPAND_SZ    =%
SET SYSTEM_PATH=%SYSTEM_PATH:Path    =%
REM ~ ECHO SYSTEM_PATH=%SYSTEM_PATH%

if %2*==* goto usage
rem echo args 1=%1
set INPUT_USER=%2
set INPUT_SYSTEM=%2
set INPUT_USER=%INPUT_USER:"=%
set INPUT_SYSTEM=%INPUT_SYSTEM:"=%
REM ~ echo INPUT_USER=%INPUT_USER%
REM ~ echo INPUT_SYSTEM=%INPUT_SYSTEM%

echo %USER_PATH% | findstr /i /c:"%INPUT_USER%" >nul && SET VER_USER=1 || SET VER_USER=0
rem echo VER 1=%VER%
if %VER_USER%==1 (
	rem echo "ADA"
	goto useractionremove
) else (
	echo.
	echo "NOT FOUND ON USER PATH !"
)

echo %SYSTEM_PATH% | findstr /i /c:"%INPUT_SYSTEM%" >nul && SET VER_SYSTEM=1 || SET VER_SYSTEM=0
rem echo VER 1=%VER%
if %VER_SYSTEM%==1 (
	rem echo "ADA"
	goto systemactionremove
) else (
	echo.
	echo "NOT FOUND ON SYSTEM PATH !"
)
goto end1

:add
SET VER_USER=
SET VER_SYSTEM=
SET VER_ACTION_USER=
SET VER_ACTION_SYSTEM=
set USER_PATH=
set SYSTEM_PATH=
set INPUT_USER=
set INPUT_SYSTEM=

FOR /F "tokens=* USEBACKQ" %%F IN (`reg query "HKCU\Environment" /v Path`) DO (
	SET USER_PATH=%%F
)

FOR /F "tokens=* USEBACKQ" %%F IN (`reg query "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v Path`) DO (
	SET SYSTEM_PATH=%%F
)

rem ECHO USER_PATH 0=%USER_PATH%
SET USER_PATH=%USER_PATH:REG_SZ    =%
SET USER_PATH=%USER_PATH:Path    =%
REM ECHO USER_PATH=%USER_PATH%

SET SYSTEM_PATH=%SYSTEM_PATH:REG_EXPAND_SZ    =%
SET SYSTEM_PATH=%SYSTEM_PATH:Path    =%
REM ~ ECHO SYSTEM_PATH=%SYSTEM_PATH%

if %1*==* goto usage
rem echo args 1=%1
set INPUT_USER=%1
set INPUT_SYSTEM=%1
set INPUT_USER=%INPUT_USER:"=%
set INPUT_SYSTEM=%INPUT_SYSTEM:"=%
REM ~ echo INPUT_USER=%INPUT_USER%
REM ~ echo INPUT_SYSTEM=%INPUT_SYSTEM%

echo %USER_PATH% | findstr /i /c:"%INPUT_USER%" >nul && SET VER_USER=1 || SET VER_USER=0
rem echo VER 1=%VER%
if %VER_USER%==1 (
	rem echo "ADA"
	echo.
	echo "USER PATH HAS BEEN ADDED !"
) else (
	goto useraction
)

echo %SYSTEM_PATH% | findstr /i /c:"%INPUT_SYSTEM%" >nul && SET VER_SYSTEM=1 || SET VER_SYSTEM=0
rem echo VER 1=%VER%
if %VER_SYSTEM%==1 (
	rem echo "ADA"
	echo.
	echo "SYSTEM PATH HAS BEEN ADDED !"
) else (
	goto systemaction
)
REM ~ SET /P VER_ACTION=Do you want to add ? [y[es],1 n[o],0]:
REM ~ echo VER_ACTION=%VER_ACTION%
REM ~ if %VER_ACTION%==1 (
	REM ~ goto action
REM ~ ) else if %VER_ACTION%==y (
	REM ~ goto action
REM ~ ) else if %VER_ACTION%==yes (
	REM ~ goto action
REM ~ ) else (
	REM ~ goto end
REM ~ )
goto end

:useraction
set ARGV_USER="%INPUT_USER%;%USER_PATH%"
rem echo ARGV=%ARGV%
reg add "HKCU\Environment" /v "Path" /t REG_SZ /d %ARGV_USER% /f

set USER_PATH=
FOR /F "tokens=* USEBACKQ" %%F IN (`reg query "HKCU\Environment" /v Path`) DO (
	SET USER_PATH=%%F
)
rem ECHO USER_PATH 0=%USER_PATH%
SET USER_PATH=%USER_PATH:REG_SZ    =%
SET USER_PATH=%USER_PATH:Path    =%
ECHO USER_PATH=%USER_PATH%

echo %SYSTEM_PATH% | findstr /i /c:"%INPUT_SYSTEM%" >nul && SET VER_SYSTEM=1 || SET VER_SYSTEM=0
rem echo VER 1=%VER%
if %VER_SYSTEM%==1 (
	rem echo "ADA"
	echo.
	echo "SYSTEM PATH HAS BEEN ADDED !"
) else (
	goto systemaction
)

goto end

:systemaction
set ARGV_SYSTEM="%INPUT_SYSTEM%;%SYSTEM_PATH%"
rem echo ARGV=%ARGV%
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v "Path" /t REG_EXPAND_SZ /d %ARGV_SYSTEM% /f

set SYSTEM_PATH=
FOR /F "tokens=* USEBACKQ" %%F IN (`reg query "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v Path`) DO (
	SET SYSTEM_PATH=%%F
)
rem ECHO USER_PATH 0=%USER_PATH%
SET SYSTEM_PATH=%SYSTEM_PATH:REG_EXPAND_SZ    =%
SET SYSTEM_PATH=%SYSTEM_PATH:Path    =%
ECHO SYSTEM_PATH=%SYSTEM_PATH%
goto end

:useractionremove
REM  set ARGV_USER="%INPUT_USER%;%USER_PATH%"
REM  echo USER_PATH 0 = %USER_PATH%
call set USER_PATH=%%USER_PATH:%INPUT_USER%;=%%
REM  call set USER_PATH=%%USER_PATH:%2;=%%
REM  echo USER_PATH 1 = %USER_PATH%

rem echo ARGV=%ARGV%
reg add "HKCU\Environment" /v "Path" /t REG_SZ /d "%USER_PATH%" /f

set USER_PATH=
FOR /F "tokens=* USEBACKQ" %%F IN (`reg query "HKCU\Environment" /v Path`) DO (
	SET USER_PATH=%%F
)
rem ECHO USER_PATH 0=%USER_PATH%
SET USER_PATH=%USER_PATH:REG_SZ    =%
SET USER_PATH=%USER_PATH:Path    =%
ECHO USER_PATH=%USER_PATH%

echo %SYSTEM_PATH% | findstr /i /c:"%INPUT_SYSTEM%" >nul && SET VER_SYSTEM=1 || SET VER_SYSTEM=0
rem echo VER 1=%VER%
if %VER_SYSTEM%==1 (
	rem echo "ADA"
	goto systemactionremove
) else (
	echo.
	echo "SYSTEM PATH HAS BEEN REMOVED !"
)

goto end1

:systemactionremove
REM  echo SYSTEM_PATH 0 = %SYSTEM_PATH%
call set SYSTEM_PATH=%%SYSTEM_PATH:%INPUT_SYSTEM%;=%%
REM  echo SYSTEM_PATH 1 = %SYSTEM_PATH%

reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v "Path" /t REG_EXPAND_SZ /d "%SYSTEM_PATH%" /f

set SYSTEM_PATH=
FOR /F "tokens=* USEBACKQ" %%F IN (`reg query "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v Path`) DO (
	SET SYSTEM_PATH=%%F
)
rem ECHO USER_PATH 0=%USER_PATH%
SET SYSTEM_PATH=%SYSTEM_PATH:REG_EXPAND_SZ    =%
SET SYSTEM_PATH=%SYSTEM_PATH:Path    =%
ECHO SYSTEM_PATH=%SYSTEM_PATH%
goto end1

:usage
SET USER_PATH=
set SYSTEM_PATH=
FOR /F "tokens=* USEBACKQ" %%F IN (`reg query "HKCU\Environment" /v Path`) DO (
	SET USER_PATH=%%F
)
SET USER_PATH=%USER_PATH:REG_SZ    =%
SET USER_PATH=%USER_PATH:Path    =%

FOR /F "tokens=* USEBACKQ" %%F IN (`reg query "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v Path`) DO (
	SET SYSTEM_PATH=%%F
)
SET SYSTEM_PATH=%SYSTEM_PATH:REG_EXPAND_SZ    =%
SET SYSTEM_PATH=%SYSTEM_PATH:Path    =%
echo USER_PATH   = %USER_PATH%
echo.
echo SYSTEM_PATH = %SYSTEM_PATH%
echo.
echo USAGE: %~n0 [Path to add]
echo           -r, --remove [Path to remove]
echo.
goto end

:end
SET PATH=%INPUT_USER%;%PATH%
SET VER_USER=
SET VER_SYSTEM=
SET VER_ACTION_USER=
SET VER_ACTION_SYSTEM=
set USER_PATH=
set SYSTEM_PATH=
set INPUT_USER=
set INPUT_SYSTEM=
goto fin

:end1
SET VER_USER=
SET VER_SYSTEM=
SET VER_ACTION_USER=
SET VER_ACTION_SYSTEM=
set USER_PATH=
set SYSTEM_PATH=
set INPUT_USER=
set INPUT_SYSTEM=
goto fin

:fin