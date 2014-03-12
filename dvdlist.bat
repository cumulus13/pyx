@echo off
title %CD%
if %1*==* goto usage
if %1==--norem eject goto start2
if %1==-norem eject goto start2
if %1==norem eject goto start2
rem if %3== norem eject goto norem eject
if %2*==* goto start

dir /s G:\ > "H:\cd_dvdlist\%1_list(%2).txt"
tree /A /F G:\ > "H:\cd_dvdlist\%1_tree(%2).txt"
rem eject dvd
goto end

:start
dir /s G:\ > "H:\cd_dvdlist\%1_list.txt"
tree /A /F G:\ > "H:\cd_dvdlist\%1_tree.txt"
rem eject dvd
goto end

:start2
dir /s G:\ > "H:\cd_dvdlist\%1_list.txt"
tree /A /F G:\ > "H:\cd_dvdlist\%1_tree.txt"
goto end

:norem eject
if %2*==* goto start2
dir /s G:\ > "H:\cd_dvdlist\%1_list(%2).txt"
tree /A /F G:\ > "H:\cd_dvdlist\%1_tree(%2).txt"
goto end

:usage
echo.
echo.
echo			use %0 [file_name not use ".txt"]
echo.
echo
goto end


:end
