@echo off
title %CD%
if %1==-rf goto eraser
if %1==* goto all

del %1 
goto end


:eraser
rmdir /s /q %2
goto end

:all
rmdir /s /q for %%2 in dir /a:D
goto end

:end


