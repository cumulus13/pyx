@echo off
rem if defined %1 goto one
if %1*==* goto one
if %1==-a goto archive
if %1==-d goto directory
goto end

:one
dir /o:-d %* | more
goto end

:archive
if %2*==* goto archive2
dir /a:a /o:-d %2 | more
goto end

:archive2
dir /a:a /o:-d %CD% | more
goto end

:directory
if %2*==* goto directory2
dir /a:d /o:-d %2 | more
goto end

:directory2
dir /a:d /o:-d %CD% | more
goto end

:end
