
@echo off
title %CD%

set iam = %cd%
c:
cd "C:\Program Files\NetSarang\Xmanager Enterprise 3"

Xshell.exe

goto end

:end
cd /d %iam%