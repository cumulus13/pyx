@echo off
SET PYTHONSTARTUP=d:\TOOLS\pyx\PYTHONSTARTUP.py
if %1*==* goto one
if %~x1==.py (
	c:\SDK\Anaconda2\python.exe %*
) else (
	c:\SDK\Anaconda2\pythonw.exe %*
)
goto end

:one
c:\SDK\Anaconda2\python.exe
goto end

:end
SET PYTHONSTARTUP=