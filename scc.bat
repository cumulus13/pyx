@echo off
if %1*==* goto usage
if %2*==* goto usage
if %1==sd goto stopdemand
if %1==sb goto stopdisabled
if %1==sa goto stopauto
if %1==td goto startdemand
if %1==tb goto startdisabled
if %1==ta goto startauto
goto end

:stopdemand
sc config %2 start= demand
sc stop %2
goto end

:stopdisabled
sc config %2 start= disabled
sc stop %2
goto end

:stopauto
sc config %2 start= auto
sc stop %2
goto end

:startdemand
sc config %2 start= demand
sc start %2
goto end

:startdisabled
sc config %2 start= disabled
sc start %2
goto end

:startauto
sc config %2 start= auto
sc start %2
goto end

:usage
echo.
echo usage: %0  sd SERVICE           Stop service and set manual start
echo		    sb SERVICE           Stop service and set disable start
echo		    sa SERVICE           Stop service and set auto start
echo		    td SERVICE           Start service and set manual start
echo		    tb SERVICE           Start service and set disable start
echo		    ta SERVICE           Start service and set auto start
goto end

:end