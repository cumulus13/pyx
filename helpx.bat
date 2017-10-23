@echo off
rem if NOT EXISTS %1 goto bbb
type %1.help | more
goto end

:bbb

:end
