@echo off
netsh wlan show interface | grep -iE "state|name|ssid"