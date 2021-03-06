@echo off
title %CD%
REM  QBFC Project Options Begin
REM  HasVersionInfo: Yes
REM  Companyname: licface
REM  Productname: Config Center
REM  Filedescription: Configuration Common Setting On Windows System
REM  Copyrights: 2010
REM  Trademarks: licface
REM  Originalname: config
REM  Comments: This For Use Windows Only
REM  Productversion: 01.00.00.01
REM  Fileversion: 01.00.00.10
REM  Internalname: Config Center
REM  Appicon: D:\ICONS\Best Icon Collection\Popo Emotions\hell_boy.ico
REM  QBFC Project Options End
if %1*==* goto help
if %1==help goto help
if %1==-? goto help
if %1==-h goto help
if %1==--help goto help

if %1==internet goto internet
if %1==desktop goto desktop
if %1==mouse goto mouse
if %1==application goto app
if %1==bluetooth goto bluetooth
if %1==firewall goto firewall
if %1==hardware goto hardware
if %1==regional goto regional
if %1==game goto game
if %1==java goto java
if %1==sound goto sound
if %1==network goto net
if %1==net goto net
if %1==netsetup goto netsetup
if %1==user goto user
if %1==power goto power
if %1==modem goto modem
if %1==security goto security
if %1==xampp goto xampp
if %1==wamp goto wamp
if %1==wampp goto wamp

goto end




:internet
start control "c:\WINDOWS\System32\inetcpl.cpl"
goto end

:desktop
start control "c:\WINDOWS\System32\desk.cpl"
goto end

:mouse
start control "c:\WINDOWS\System32\main.cpl"
goto end

:app
start control "c:\WINDOWS\System32\appwiz.cpl"
goto end

:bluetooth
start control "c:\WINDOWS\System32\desk.cpl"
goto end

:firewall
start control "c:\WINDOWS\System32\firewall.cpl"
goto end

:hardware
start control "c:\WINDOWS\System32\hdwwiz.cpl"
goto end

:regional
start control "c:\WINDOWS\System32\intl.cpl"
goto end

:game
start control "c:\WINDOWS\System32\joy.cpl"
goto end

:java
start control "c:\WINDOWS\System32\javacpl.cpl"
goto end

:sound
start control "c:\WINDOWS\System32\mmsys.cpl"
goto end

:netsetup
start control "c:\WINDOWS\System32\netsetup.cpl"
goto end

:net
start control "c:\WINDOWS\System32\ncpa.cpl"
goto end

:user
start control "c:\WINDOWS\System32\nusrmgr.cpl"
goto end

:power
start control "c:\WINDOWS\System32\powercfg.cpl"
goto end

:modem
start control "c:\WINDOWS\System32\telephon.cpl"
goto end

:security
start control "c:\WINDOWS\System32\wscui.cpl"
goto end

:xampp
echo.
echo.
notepad2 d:\pyx\xampp.py
copy /Y d:\pyx\xampp.py "g:\PROGRAMMING\Python\XAMPP_start control"
set bme = %CD%
cd /d "g:\PROGRAMMING\Python\XAMPP_start control"
thg commit
goto preend

:wamp
echo.
notepad2 d:\pyx\wamp.py
copy /Y d:\pyx\wamp.py" g:\PROGRAMMING\Python\WAMP_start control"
set bme = %CD%
cd /d "g:\PROGRAMMING\Python\WAMP_start control"
thg commit
goto preend

:help
cls
echo.
echo.
echo   use : %0 [internet / desktop / mouse / application / bluetooth 
echo.
echo                firewall / hardware/ regional / game / java / sound 
echo.
echo                network / net / netsetup / user / power / modem / security ]
echo.
echo.
echo                     #------------- Script By licface --------------#
echo.
goto end

:preend
cd /d %bme%
goto end

:end

