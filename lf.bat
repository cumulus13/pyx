@echo off
cls
echo.
if %1*==* goto help
if %1==-t goto time
if %1==-a goto arcv
if %1==-d goto directory
if %1==-s goto size
if %1==-h goto hidden
if %1==-n goto name
if %1==-e goto ext
if %1==-g goto group
goto end

:arcv
dir /a:a /o:D %2
goto end

:time
dir /o:D %2
goto end

:directory
dir /a:d /o:D %2
goto end

:size
dir /o:S /o:s %2
goto end

:hidden
dir /a:h /o:D %2
goto end

:name
dir /o:n %2
goto end

:ext
dir /o:e /o:n %2
goto end

:group
dir /o:g %2
goto end

:help
echo.
echo.
echo         use : %0 -t (by time)
echo                  -a (by Archieve)
echo                  -d (by directory)
echo                  -s (by size)
echo                  -h (by hidden file)
echo                  -n (by name)
echo                  -e (by extension)
echo                  -g (by group)
echo.
goto end

:end