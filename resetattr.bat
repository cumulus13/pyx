@echo off
title %CD%

for /r d:\music %%X in (*.jpg) do (attrib -r -a -s -h %%X)
goto end

:end