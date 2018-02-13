@echo off
if %1*==* goto usage
if %1==open goto open
if %1==close goto close
goto end

:open
"c:\Program Files (x86)\Steganos Safe 18\Safe.exe" -entry Safe.ToggleDrive.mbu Safe.Pass.Bl4ck1d-L1cf4ce2
"c:\Program Files (x86)\Steganos Safe 18\Safe.exe" -entry Safe.ToggleDrive.safe001 Safe.Pass.Bl4ck1d-L1cf4ce2
goto end

:close
"c:\Program Files (x86)\Steganos Safe 18\Safe.exe" -entry Safe.ToggleDrive.mbu Safe.Pass.Close
"c:\Program Files (x86)\Steganos Safe 18\Safe.exe" -entry Safe.ToggleDrive.safe001 Safe.Pass.Close
goto end

:usage
echo.
echo usage%) [open/close]
echo.
goto end

:end
