echo off
rem set PATH=%PATH:c:\SDK\Anaconda2=c:\Anaconda2%
REM SET "PATH=!PATH:c:\SDK\Anaconda2=%VIRTUAL_ENV%!"
echo ALL_ARGV=%*
set ARGV1=%1
echo ARGV1 = %ARGV1%
set ARGV=%*
set "ARGV=!ARGV:%ARGV1%=!"
REM  set "ARGV=!ARGV:%ARGV1%=!"
echo ARGV = %ARGV%
REM  if %1*==* goto usage
REM  echo %* f:\PROJECTS\REPOSITORY
REM  :usage
REM  git 
REM  goto end

REM  :end
