@echo off
if %1*==-V goto version
if %1*==-v goto version
c:\SDK\Python27\python.exe %*
goto end

:version
c:\SDK\Python27\python.exe -V
goto end

:end
