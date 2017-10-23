@echo off

set PATH=%PATH_BCK%

if %1*==* goto one

"c:\Ruby192\bin\ruby.exe" %1
goto end

:one
path="c:\Ruby192\bin";%PATH%
ruby --version
goto end


:end