@echo off

set PATH=%PATH_BCK%

if %1*==* goto one

"c:\Program Files\SapphireSteel Software\Ruby In Steel\v1.0\IronRuby\rbx.exe" %1
goto end

:one
path="c:\Program Files\SapphireSteel Software\Ruby In Steel\v1.0\IronRuby";%PATH%
rbx -V
goto end


:end