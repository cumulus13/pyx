@echo off
title %CD%
if %1==-1 goto one
if %1==-2 goto two
if %1==-3 goto two

dir c:\WINDOWS\System32\%1*.exe | more
dir c:\EXE\%1*.exe | more
rem dir c:\TOOLS\qyx\%1*.exe | more
goto end

:one
dir c:\EXE\%2*.exe | more
goto end

:two
rem dir c:\qyx\TOOLS\%2*.exe | more
goto end

:three
dir c:\WINDOWS\System32\%2*.exe | more
goto end

:end
