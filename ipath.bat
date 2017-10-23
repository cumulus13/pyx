@echo off

if %1*==* goto one
if %1==+ goto addme

"h:\EXE\ipathx.exe" %1

if %2*==* goto end
if %2==+ goto add

goto end

:one
"h:\EXE\ipathx.exe" %CD%
goto end

:addme
"h:\EXE\ipathx.exe" %CD%\%2
rem "h:\EXE\ipathx.exe" "%CD%\%2"
goto end

:add
"h:\EXE\ipathx.exe" %1\%3
goto end

:end