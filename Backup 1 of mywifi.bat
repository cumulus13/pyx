@echo off
netsh interface ip set address wi-fi2 static 192.168.10.2 255.255.255.0 192.168.10.254
netsh interface ip set dnsservers wi-fi2 static 192.168.10.2
netsh interface ip add dnsservers wi-fi2 192.168.10.254 index=2
netsh interface ip add dnsservers wi-fi2 8.8.8.8 index=3
netsh wlan connect OXIMA OXIMA
c:\Python27\python.exe c:\pyx\addhostx.py update -U 192.168.10.2
netsh interface ip show config wi-fi2
goto end


:end