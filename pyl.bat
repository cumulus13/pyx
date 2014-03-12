@echo off
title %CD%

dir c:\WINDOWS\System32\%1*.py | more
dir d:\pyx\%1*.py | more
dir d:\pyx\%1*.pyw | more
dir c:\TOOLS\qyx\%1*.py | more
goto end


:end
