@echo off
set BACK=%PATH%
set PATH=c:\dm;c:\dm\bin;c:\dm\lib;c:\dm\include;c:\dm\stlport;
dmc %1 -Ic:\dm\stlport\stlport
set PATH=%BACK%