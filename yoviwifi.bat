@echo off
netsh interface ip set address wi-fi2 static 192.168.0.10 255.255.255.0 192.168.0.254
netsh interface ip set dnsservers wi-fi2 static 192.168.0.10
netsh interface ip add dnsservers wi-fi2 192.168.0.254 index=2
netsh interface ip add dnsservers wi-fi2 8.8.8.8 index=3
netsh wlan connect TP-LINK_POCKET_3020_B8042B TP-LINK_POCKET_3020_B8042B
netsh interface ip show config wi-fi2
c:\SDK\Anaconda2\python.exe c:\pyx\addhostx.py update -U 192.168.0.10
goto end


:end