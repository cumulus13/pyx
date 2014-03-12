@echo off
title %CD%
mysql -uroot -pblackid -D %1 -e %2
goto end

:end
