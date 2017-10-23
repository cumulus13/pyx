@echo off
title %CD%
cls
echo.
echo.
if %1*==* goto usage
if %1==xampp goto xampp
if %1==far goto far
if %1==ssh goto ssh
type c:\pyx\%1.help
rem PAUSE > NUL
goto end

:xampp
type D:\xampp\readme_en.txt;xampp-changes.txt;passwords.txt;readme-addon-tomcat.txt | more
goto end

:far
type "C:\Program Files\Far2\Documentation\eng\"TechInfo.txt;Plugins.Install.txt;Plugins.Review.txt;Arc.Support.txt;Far.FAQ.txt;Bug.Report.txt;"C:\Program Files\Far2\"changelog | more
goto end

:ssh
type "c:\Program Files\OpenSSH\docs\readme.txt" | more
goto end

:usage
cls
echo.
echo.
echo            use : %0 [topic]
echo.
goto end

:end
rem cls
echo.
echo.
