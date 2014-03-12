@echo off
title %CD%

c:\cygwin\bin\chgrp.exe -c -R -v None %1

goto end


:end