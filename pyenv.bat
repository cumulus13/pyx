@echo off
if [%1]==[] goto usage
if [%1]==[ls] goto ls
if [%1]==[make] goto make

SET LOCAL
SET ROOT_PYENV=c:\PYENV
set ME=%CD%
call %ROOT_PYENV%\%1\Scripts\activate.bat
rem activate.bat
CD /d %ME%
goto end

:ls
echo.
CD /d %ROOT_PYENV%
DIR /w
echo.
goto end

:make
CD /d %ROOT_PYENV%
if not [%2]==[] (
	if [%3]==[3] (
		virtualenv3 %2
		CD /d %ROOT_PYENV%\%2\Scripts
		activate.bat
	) else (
		virtualenv %2
		CD /d %ROOT_PYENV%\%2\Scripts
		activate.bat
	)
) else (
	goto usage1
)
goto end

:make1
virtualenv 
goto end

:usage
echo.
CD /d %ROOT_PYENV%
DIR /w
echo.
echo.
echo USAGE: %0 NAME_VIRTUALENV
echo        %0 make NEW_VIRTUALENV 
echo        %0 make NEW_VIRTUALENV 3  (3 = for python version 3)
echo.
:goto end

:usage1
echo.
echo.
echo USAGE: %0 NAME_VIRTUALENV
echo        %0 make NEW_VIRTUALENV 
echo        %0 make NEW_VIRTUALENV 3  (3 = for python version 3)
echo.
:goto end

:end
CD /d %ME%
