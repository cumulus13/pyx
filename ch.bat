@echo off
title %CD%
c:\cygwin\bin\chown.exe -R -v -c Administrator %1
c:\cygwin\bin\chgrp.exe -c -R -v None %1
c:\cygwin\bin\chmod.exe -c -R -v 777 %1
goto end


:end