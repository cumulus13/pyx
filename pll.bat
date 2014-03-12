@echo off
title %CD%

dir c:\WINDOWS\System32\%1*.pl | more
dir d:\pyx\%1*.pl | more
dir c:\qyx\%1*.pl | more
goto end


:end
