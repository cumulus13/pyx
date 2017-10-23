@echo off
netstat -anob | grep -i %1 -A 5 -B 5