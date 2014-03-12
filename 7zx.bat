@echo off
title %CD%
7z -tzip a %1.zip %1 -pblackid
goto end

:end
