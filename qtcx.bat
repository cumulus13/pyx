@echo on
set BACK=%PATH%
set QTDIR=C:\Qt\4.8.6
set PATH=C:\Qt\4.8.6\bin
set PATH=%PATH%;c:\mingw32\4.9.2\bin
set PATH=%PATH%;%SystemRoot%\System32
set QMAKESPEC=win32-g++-4.6

qmake -project
qmake
call c:\Qt\4.8.6\bin\make.bat
set PATH=%BACK%