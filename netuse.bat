@echo off
REM  if DEFINED %3 goto one
rem NET USE %1: %2 
REM  goto end

REM  :one
REM  if DEFINED %4 goto two
REM  NET USE %1=%2 %3 /user:root
REM  goto end

REM  :two
REM  NET USE %1=%2 %3 /user:%4 
REM  goto end

REM  :end
net use X: /delete /y > NUL
net use D: /delete /y > NUL
net use E: /delete /y > NUL
net use F: /delete /y > NUL
net use G: /delete /y > NUL
net use H: /delete /y > NUL
net use J: /delete /y > NUL
net use V: /delete /y > NUL
net use N: /delete /y > NUL
net use M: /delete /y > NUL

net use X: \\192.168.10.1\C Bl4ck1d /user:root
net use D: \\192.168.10.1\D
net use E: \\192.168.10.1\E
net use F: \\192.168.10.1\F
net use G: \\192.168.10.1\G
net use H: \\192.168.10.1\H
net use J: \\192.168.10.1\J
net use V: \\192.168.10.4\var xxxnuxer13 /user:licface
rem net use M: \\192.168.100.4\etc xxxnuxer13 /user:licface
rem net use N: \\192.168.100.4\var xxxnuxer13 /user:licface