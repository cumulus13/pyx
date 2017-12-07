@echo off
set back=%PATH%
set PATH=c:\mingw32\5.2.0\posix\dwarf\include;c:\mingw32\5.2.0\posix\dwarf\lib;c:\mingw32\5.2.0\posix\dwarf;c:\mingw32\5.2.0\posix\dwarf\bin;c:\GTK;c:\GTK\bin;c:\GTK\lib;c:\GTk\include;%PATH%
gcc -mms-bitfields -Wall -g -Ic:/GTK/include/gtk-3.0 -Ic:/GTK/include/cairo -Ic:/GTK/include/pango-1.0 -Ic:/GTK/include/atk-1.0 -Ic:/GTK/include/cairo -Ic:/GTK/include/pixman-1 -Ic:/GTK/include -Ic:/GTK/include/freetype2 -Ic:/GTK/include -Ic:/GTK/include/libpng15 -Ic:/GTK/include/gdk-pixbuf-2.0 -Ic:/GTK/include/libpng15 -Ic:/GTK/include/glib-2.0 -Ic:/GTK/lib/glib-2.0/include -c %1 -o %2
g++.exe -LC:\GTK\lib -o %3 %2 -lgtk-3 -lgdk-3 -lgdi32 -limm32 -lshell32 -lole32 -Wl,-luuid -lwinmm -lpangocairo-1.0 -lpangowin32-1.0 -lgdi32 -lpango-1.0 -lm -latk-1.0 -lcairo-gobject -lcairo -lgdk_pixbuf-2.0 -lgio-2.0 -lgobject-2.0 -lglib-2.0 -lintl  C:\GTK\lib\gtk-win32-3.0.lib
del %2
%3
set PATH=%back%

rem gcc -mms-bitfields -Wall -g -IC:\GTK-2.24\include -IC:\GTK-2.24\include\gtk-2.0 -IC:\GTK-2.24\include\cairo -IC:\GTK-2.24\include\gdk -IC:\GTK-2.24\include\glib-2.0 -IC:\GTK-2.24\lib\glib-2.0\include -IC:\GTK-2.24\include\pango-1.0 -IC:\GTK-2.24\lib\gtk-2.0\include -IC:\GTK-2.24\include\atk-1.0 -IC:\GTK-2.24\include\gdk-pixbuf-2.0 -Ic:\mingw32\5.2.0\posix\dwarf\bin -IC:\GTK-2.24\bin %*
rem -c e:\BUILD\test\gtk01\main.c -o obj\Debug\main.o
rem [100.0%] g++.exe -LC:\GTK-2.24\lib -LC:\GTK\lib -o bin\Debug\gtk01.exe obj\Debug\main.o   -lgtk-win32-2.0 -lgobject-2.0 -lglib-2.0 C:\GTK\lib\gtk-win32-3.0.lib
rem Output file is bin\Debug\gtk01.exe with size 62.64 KB