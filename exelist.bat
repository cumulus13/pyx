@echo off
title %CD%

dir %1*.exe | more
goto end


:end
