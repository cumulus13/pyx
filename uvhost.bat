@echo off
title %CD%
updatevhost delete & updatevhost2 delete && updatevhost update & updatevhost2 update
goto end

:end