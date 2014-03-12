@echo off
title %CD%
if %1*==* goto usage
if %2*==* goto start
if %3==noeject goto noeject

dir /s K:\ > "e:\CD_DVD_LIST\%1_list(%2).txt"
tree /A /F K:\ > "e:\CD_DVD_LIST\%1_tree(%2).txt"
eject cd
goto end

:start
dir /s K:\ > "e:\CD_DVD_LIST\%1_list.txt"
tree /A /F K:\ > "e:\CD_DVD_LIST\%1_tree.txt"
eject cd
goto end

:start2
dir /s K:\ > "e:\CD_DVD_LIST\%1_list.txt"
tree /A /F K:\ > "e:\CD_DVD_LIST\%1_tree.txt"
goto end

:noeject
if %2*==* goto start2
dir /s K:\ > "e:\CD_DVD_LIST\%1_list(%2).txt"
tree /A /F K:\ > "e:\CD_DVD_LIST\%1_tree(%2).txt"
goto end

:usage
echo.
echo.
echo			use %0 [file_name not use ".txt"]
echo.
echo
goto end


:end