@@echo off
if %1*==* goto usage
if %1==access goto access
if %1==close goto close
goto end

:access
@echo on
attrib -R -A -S -H -I -X /S /D c:\DOWNLOAD\MBX
@echo off
goto end

:close
@echo on
attrib +R +A +S +H +I +X /S /D c:\DOWNLOAD\MBX
@echo off
goto end

:usage
echo.
echo USAGE: %0 access/close
echo.
goto end

:end

