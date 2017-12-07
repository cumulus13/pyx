@echo off
if %1==sur goto suryadi
if %1==dav goto david
if %1==dav2 goto david2
if %1==pre goto pre
if %1==pre2 goto pre2
if %1==q goto q
if %1==q2 goto q2
echo "MAIN"
c:\Python352\python.exe "f:\PROJECTS\REPOSITORY\utorrentctl\utorrentctl.py" %*
goto end

:q
echo "Q"
c:\Python352\python.exe "f:\PROJECTS\REPOSITORY\utorrentctl\utorrentctl.py" -H 25.72.21.236:9898 -U root -P blackid --api=linux %2 %3 %4 %5 %6 %7 %8 %9 %10 %11 %12 %13 %14 %15
goto end

:q2
echo "Q 2"
c:\Python352\python.exe "f:\PROJECTS\REPOSITORY\utorrentctl\utorrentctl.py" -H 192.168.100.20:9898 -U root -P blackid --api=linux %2 %3 %4 %5 %6 %7 %8 %9 %11 %12 %13 %14 %15
goto end

:suryadi
echo "SUR"
c:\Python352\python.exe "f:\PROJECTS\REPOSITORY\utorrentctl\utorrentctl.py" -H 25.51.125.206:9898 -U root -P blackid --api=linux %2 %3 %4 %5 %6 %7 %8 %9 %11 %12 %13 %14 %15
goto end

:david
echo "DAV"
c:\Python352\python.exe "f:\PROJECTS\REPOSITORY\utorrentctl\utorrentctl.py" -H 25.49.177.92:9898 -U root -P blackid --api=linux %2 %3 %4 %5 %6 %7 %8 %9 %11 %12 %13 %14 %15
goto end

:david2
echo "DAV 2"
c:\Python352\python.exe "f:\PROJECTS\REPOSITORY\utorrentctl\utorrentctl.py" -H 192.168.100.38:9898 -U root -P blackid --api=linux %2 %3 %4 %5 %6
goto end

:pre
echo "PRE"
c:\Python352\python.exe "f:\PROJECTS\REPOSITORY\utorrentctl\utorrentctl.py" -H 25.22.225.8:9898 -U root -P blackid --api=linux %2 %3 %4 %5 %6
goto end

:pre2
echo "PRE 2"
c:\Python352\python.exe "f:\PROJECTS\REPOSITORY\utorrentctl\utorrentctl.py" -H 192.168.100.5:9898 -U root -P blackid --api=linux %2 %3 %4 %5 %6
goto end

:end