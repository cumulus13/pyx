@echo off

set PATH=%PATH_BCK%

if %1*==* goto one

"c:\Redmine\ruby\bin\ruby.exe" %1
goto end

:one
path="c:\Redmine\ruby\bin";%PATH%
ruby --version
goto end


:end