@echo off
set PWD=%CD%
PUSHD c:\msys2
start c:\msys2\msys2_shell.bat
cd /d %PWD%

