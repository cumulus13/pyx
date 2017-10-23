@echo off
c:\Apps\mysql\mysql-5.6.20\bin\mysql.exe  -u root -e "insert into snarelog.logs(`tag`,`msg`) values %1,%2"