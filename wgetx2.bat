@echo off
if %2*==* goto one
wget -c -t 0 %1  --no-check-certificate -O D:\DOWNLOADS\%2
goto end

:one
wget -c -t 0 %1  --no-check-certificate 
goto end

:end