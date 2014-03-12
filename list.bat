@echo off
title %CD%
if %1*==* goto usage
if %1==-F goto F

tree /A /F %1 > c:\LIST_DIRECTORY\%2
goto end


:F
tree /A /F %1 > c:\LIST_DIRECTORY\D.txt
tree /A /F %1 > c:\LIST_DIRECTORY\E.txt
tree /A /F %1 > c:\LIST_DIRECTORY\I.txt
tree /A /F %1 > c:\LIST_DIRECTORY\J.txt
tree /A /F %1 > c:\LIST_DIRECTORY\K.txt
tree /A /F %1 > c:\LIST_DIRECTORY\L.txt
tree /A /F %1 > c:\LIST_DIRECTORY\N.txt
tree /A /F %1 > c:\LIST_DIRECTORY\O.txt
tree /A /F %1 > c:\LIST_DIRECTORY\P.txt

goto end


:usage
echo.
echo.
echo        Usage : %0 [Directory] [report_file]
echo		       %0 -F For Make All List Directory
echo.
echo.
goto end

:end
