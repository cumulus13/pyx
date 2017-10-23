@echo off

set PATH=%PATH_BCK%

if %1*==* goto one

"c:\Ruby186\bin\ruby.exe" %1
goto end

:one
path="c:\Ruby186\bin";%PATH%
ruby --version
goto end


:end