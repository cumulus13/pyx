@echo off
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout d:\WWW\SSLCertificateKeyFile\%1.key -out d:\WWW\SSLCertificateKeyFile\%1.crt