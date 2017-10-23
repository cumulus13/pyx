@echo off
title %CD%
attrib -h -r -a -s /s /d %*
goto end

:end
