@echo off
if %1*==* goto usage
if %1==1 goto one
if %1==2 goto two
if %1==3 goto three
goto end

:one
powercfg /x monitor-timeout-ac 60
powercfg /x monitor-timeout-dc 60
powercfg /x disk-timeout-ac 55
powercfg /x disk-timeout-dc 55
powercfg /x standby-timeout-ac 57
powercfg /x standby-timeout-dc 57
powercfg /x hibernate-timeout-ac 60
powercfg /x hibernate-timeout-dc 60
goto end

:two
powercfg /x monitor-timeout-ac 180
powercfg /x monitor-timeout-dc 180
powercfg /x disk-timeout-ac 175
powercfg /x disk-timeout-dc 175
powercfg /x standby-timeout-ac 177
powercfg /x standby-timeout-dc 177
powercfg /x hibernate-timeout-ac 180
powercfg /x hibernate-timeout-dc 180
goto end

:three
powercfg /s 381b4222-f694-41f0-9685-ff5bb260df2e
goto end

:usage
echo USAGE: %0 1 / 2
echo        1 = MAX
echo        2 = Balance
echo.
goto end

:end
