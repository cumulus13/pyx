@echo off
title %CD%

title DjangoDemo - Server
cls
echo.
echo.

python E:\wampserver\www3\django_project\cms\manage.py runserver 0.0.0.0:9000

goto end

:end