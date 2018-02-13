@echo off
set PATH1=%PATH%
if exist %2 goto two
set PATH=%PATH%;c:\Apps\lighttpd
git instaweb --http=lighttpd
goto end

:two
echo REREr
goto end

:end
set PATH=%PATH1%