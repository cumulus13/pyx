@echo off
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout %1.key -out %1.crt