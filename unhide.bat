@echo off
title %CD%
attrib -h -r -a -s /s /d %1
goto end

:end
