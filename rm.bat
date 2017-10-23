@echo off
title %CD%
if %1==-rf goto eraser
if %1==* goto all

del %1 
goto end


:eraser
rmdir /s /q %2 %3 %4 %5 %6 %7 %8 %9
goto end

:all
rmdir /s /q for %%2 in dir /a:D
goto end

:end


