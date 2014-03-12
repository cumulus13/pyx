@echo off
title %CD%
echo.
echo                ###############################################################
echo                #                Zope Server Service Control                  #
echo                #                         Scr1pt by                           #
echo                #                          BL4CK1D                            #
echo                #                                                             #
echo                ###############################################################
echo.


if %1*==* goto usage
if %1==start goto start
if %1==stop goto stop
if %1==restart goto restart
if %1==control goto control
if %1==help goto usage
if %1==h goto usage
if %1==-h goto usage
if %1==-help goto usage
if %1==--h goto usage
if %1==--help goto usage

:start
start J:\Zope\Instance\2.11.4\bin\runzope.bat
goto end

:control
opera "http://www.zope.net:8080"
goto end

:usage
echo.
echo.
echo            use %0 start    [start Zope Server]
echo.                  control  [start Zope manager]
echo.
echo.
goto end


:end