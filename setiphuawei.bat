@echo off
netsh interface ip set address "TSEL-TIMEBASED" static %1 255.255.255.255 %1