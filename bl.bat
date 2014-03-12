@echo off
title %CD%

dir c:\WINDOWS\System32\%1*.bat | more
dir d:\pyx\%1*.bat | more
goto end


:end
