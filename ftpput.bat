@echo off 
if %2*==* goto one
ncftpput -u root -p xxxnuxer13 -P 2323 192.168.10.4 %1 %2

:one
ncftpput -u root -p xxxnuxer13 -P 2323 192.168.10.4 /sdcard/blackmart/downloads %1 
goto end 
:end 
