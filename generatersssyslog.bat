REM  QBFC Project Options Begin
REM  HasVersionInfo: Yes
REM  Companyname: licface
REM  Productname: RSSPHP Generate
REM  Filedescription: For MyScript PHP Generater
REM  Copyrights: 2010
REM  Trademarks: licface
REM  Originalname: generatersssyslog.bat
REM  Comments: For Scripting Only
REM  Productversion: 01.00.10.01
REM  Fileversion: 01.00.10.10
REM  Internalname: Generatersssyslog
REM  Appicon: D:\ICONS\Best Icon Collection\Aqua Neue\Burn.ico
REM  QBFC Project Options End

d:\pyx\generatersssyslog.batd:\pyx\generatersssyslog.bat
@rem ----- ExeScript Options Begin -----
@rem ScriptType: console,silent,invoker
@rem DestDirectory: temp
@rem Icon: default
@rem OutputFile: d:\pyx\generatersssyslog.exe
@rem CompanyName: licface
@rem FileDescription: Generate RSS For Script PHP
@rem FileVersion: 1.0.0.1
@rem LegalCopyright: licface
@rem ProductName: RSSPHP_Generate
@rem ProductVersion: 1.0.0.1
@rem TimeOut: 10
@rem ----- ExeScript Options End -----
@echo off
title %CD%
cd /d "e:\wampserver\www3\kiwisyslog\theme\theme2"

"d:\xampp\php\php.exe" writerss3.php
"d:\xampp\php\php.exe" writerss2.php
"d:\xampp\php\php.exe" writerss.php
goto end


:end
