@echo off
ipconfig /flushdns
net stop dnscache
ipconfig /flushdns
net start dnscache
ipconfig /flushdns