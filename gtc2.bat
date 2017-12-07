@echo off
set back=%PATH%
set PATH=c:\mingw32\5.2.0\posix\dwarf;c:\mingw32\5.2.0\posix\dwarf\lib;c:\mingw32\5.2.0\posix\dwarf\include;c:\mingw32\5.2.0\posix\dwarf\bin;c:\GTK-2.24;c:\GTK-2.24\bin;c:\GTK-2.24\lib;c:\GTK-2.24\include;%PATH%
gcc -mms-bitfields -Ic:/GTK-2.24/include/gtk-2.0 -Ic:/GTK-2.24/lib/gtk-2.0/include -Ic:/GTK-2.24/include/atk-1.0 -Ic:/GTK-2.24/include/cairo -Ic:/GTK-2.24/include/gdk-pixbuf-2.0 -Ic:/GTK-2.24/include/pango-1.0 -Ic:/GTK-2.24/include/glib-2.0 -Ic:/GTK-2.24/lib/glib-2.0/include -Ic:/GTK-2.24/include -Ic:/GTK-2.24/include/freetype2 -Ic:/GTK-2.24/include/libpng14 -IC:\GTK-2.24\include -IC:\GTK-2.24\include\gtk-2.0 -IC:\GTK-2.24\include\cairo -IC:\GTK-2.24\include\gdk -IC:\GTK-2.24\include\glib-2.0 -IC:\GTK-2.24\lib\glib-2.0\include -IC:\GTK-2.24\include\pango-1.0 -IC:\GTK-2.24\lib\gtk-2.0\include -IC:\GTK-2.24\include\atk-1.0 -IC:\GTK-2.24\include\gdk-pixbuf-2.0 -Ic:\mingw32\5.2.0\posix\dwarf\bin -IC:\GTK-2.24\bin  -c %1 -o %2

rem gcc -mms-bitfields -Wall -g -IC:\GTK-2.24\include -IC:\GTK-2.24\include\gtk-2.0 -IC:\GTK-2.24\include\cairo -IC:\GTK-2.24\include\gdk -IC:\GTK-2.24\include\glib-2.0 -IC:\GTK-2.24\lib\glib-2.0\include -IC:\GTK-2.24\include\pango-1.0 -IC:\GTK-2.24\lib\gtk-2.0\include -IC:\GTK-2.24\include\atk-1.0 -IC:\GTK-2.24\include\gdk-pixbuf-2.0 -Ic:\mingw32\5.2.0\posix\dwarf\bin -IC:\GTK-2.24\bin %*
rem -c e:\BUILD\test\gtk01\main.c -o obj\Debug\main.o
rem [100.0%] g++.exe -LC:\GTK-2.24\lib -LC:\GTK\lib -o bin\Debug\gtk01.exe obj\Debug\main.o   -lgtk-win32-2.0 -lgobject-2.0 -lglib-2.0 C:\GTK\lib\gtk-win32-3.0.lib
rem Output file is bin\Debug\gtk01.exe with size 62.64 KB

g++.exe -LC:\GTK-2.24\lib -o %3 %2 -lgtk-3 -lgdk-3 -limm32 -lshell32 -lole32 -Wl,-luuid -lwinmm -lm -latk-1.0 -lcairo-gobject -lgtk-win32-2.0 -lgdk-win32-2.0 -latk-1.0 -lgio-2.0 -lpangowin32-1.0 -lgdi32 -lpangocairo-1.0 -lgdk_pixbuf-2.0 -lpango-1.0 -lcairo -lgobject-2.0 -lgmodule-2.0 -lgthread-2.0 -lglib-2.0 -lintl C:\GTK-2.24\lib\gtk-win32-2.0.lib
del %2
%3
set PATH=%back%
