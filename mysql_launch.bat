@echo off
SET PATH=%PATH:c:\SDK\Anaconda2=%
SET PATH=%PATH:c:\Anaconda2=%
SET PATH=%PATH:c:\SDK\Python27=%
SET PATH=%PATH:c:\SDK\Python352=%
SET PATH=c:\TOOLS\mysql-shell-1.0.10-windows-x86-64bit\bin;%PATH%
mysql -uroot -h192.168.1.2 -p