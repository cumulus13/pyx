@echo off
title %CD%
cls
echo.
echo.
echo		####################################################
echo		#              Bitnami Trac Server Stack           #
echo		#                                                  #
echo		#                    Programmer by                 #
echo		#                 Laode Hadi Cahyadi               #
echo		#                                                  #
echo         ####################################################
echo.
echo.

if %1*==* goto usage
if %1==start goto start
if %1==stop goto stop
if %1==restart goto restart
if %1==status goto status

:start
sc config tracApache start= demand
sc config tracSubversion start= demand
sc start tracSubversion
sc start tracApache
echo.
echo.
rem pause > nul
goto end

:stop
sc stop tracSubversion
sc stop tracApache
sc config tracApache start= demand
sc config tracSubversion start= demand
echo.
echo.
rem pause > nul
goto end

:restart
net stop tracSubversion
net stop tracApache
sc start tracSubversion
sc start tracApache
goto end


:status
sc query tracSubversion
sc query tracApache
echo.
echo.
rem pause > nul
goto end

:usage
echo.
echo.
echo		use : %0 start / stop / restart / status
echo.
echo.
goto end

:end
