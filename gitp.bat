@echo off
git add -A
git commit -a -m "version: %1"
git push ssh://root@192.168.123.2:2222/%2.git master