@echo off
rem if %*==& goto usage
if %1==open goto open
if %1==close goto close
goto end

:open
safe -entry Safe.ToggleDrive.mbu Safe.Pass.Bl4ck1d-L1cf4ce2 
goto end

:close
safe -entry Safe.ToggleDrive.mbu Safe.Pass.Close
goto end

:usage
echo.
echo usage%) [open/close]
echo.
goto end

:end
