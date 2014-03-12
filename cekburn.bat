@echo off
title %CD%
cls
echo.
echo.
if %1*==* goto me
if %1==--list goto me
if %1==--size goto size
if %1==-s goto size
if %1==-l goto list
if %1==--music goto music
if %1==--film goto film

:me
r2 d:\burn
r2 e:\burn
r2 f:\burn
r2 g:\burn
r2 h:\burn
r2 i:\burn
r2 m:\burn
r2 k:\burn
r2 n:\burn
r2 o:\burn
r2 p:\burn
goto end

:size
c:\cygwin\bin\du -s -h d:\burn
c:\cygwin\bin\du -s -h e:\burn
c:\cygwin\bin\du -s -h f:\burn
c:\cygwin\bin\du -s -h g:\burn
c:\cygwin\bin\du -s -h h:\burn
c:\cygwin\bin\du -s -h i:\burn
c:\cygwin\bin\du -s -h m:\burn
c:\cygwin\bin\du -s -h k:\burn
c:\cygwin\bin\du -s -h n:\burn
c:\cygwin\bin\du -s -h o:\burn
c:\cygwin\bin\du -s -h p:\burn
goto end

:film
if %2*==* goto flist
if %2==--list goto flist
if $2==--size goto fsize
goto end

:flist
r2 D:\FILM
r2 E:\FILM
r2 F:\FILM
r2 G:\FILM
r2 H:\FILM
r2 I:\FILM
r2 M:\FILM
r2 K:\FILM
r2 N:\FILM
r2 O:\FILM
r2 P:\FILM

c:\cygwin\bin\du -s -h D:\FILM
c:\cygwin\bin\du -s -h E:\FILM
c:\cygwin\bin\du -s -h F:\FILM
c:\cygwin\bin\du -s -h G:\FILM
c:\cygwin\bin\du -s -h H:\FILM
c:\cygwin\bin\du -s -h I:\FILM
c:\cygwin\bin\du -s -h M:\FILM
c:\cygwin\bin\du -s -h K:\FILM
c:\cygwin\bin\du -s -h N:\FILM
c:\cygwin\bin\du -s -h O:\FILM
c:\cygwin\bin\du -s -h P:\FILM

goto end

:fsize
c:\cygwin\bin\du -s -h D:\FILM
c:\cygwin\bin\du -s -h E:\FILM
c:\cygwin\bin\du -s -h F:\FILM
c:\cygwin\bin\du -s -h G:\FILM
c:\cygwin\bin\du -s -h H:\FILM
c:\cygwin\bin\du -s -h I:\FILM
c:\cygwin\bin\du -s -h M:\FILM
c:\cygwin\bin\du -s -h K:\FILM
c:\cygwin\bin\du -s -h N:\FILM
c:\cygwin\bin\du -s -h O:\FILM
c:\cygwin\bin\du -s -h P:\FILM
goto end

:music
if %2*==* goto mlist
if %2==--list goto mlist
if $2==--size goto msize
if %2==--prepare goto prepare
goto end

:mlist
r2 "F:\MUSIC\0.WEST\LAGU\BURN"
c:\cygwin\bin\du -s -h "F:\MUSIC\0.WEST\LAGU\BURN"
goto end

:msize
c:\cygwin\bin\du -s -h "F:\MUSIC\0.WEST\LAGU\BURN"
goto end

:prepare
r2 "F:\MUSIC\0.WEST\LAGU\YANG UDAH"
echo.
c:\cygwin\bin\du -s -h "F:\MUSIC\0.WEST\LAGU\YANG UDAH"
goto end


:end