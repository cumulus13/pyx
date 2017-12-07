@echo off
set back=%PATH%
set PATH=c:\mingw32\5.2.0\posix\dwarf;c:\mingw32\5.2.0\posix\dwarf\bin;c:\GTK;c:\GTK\bin;c:\GTK\lib;c:\GTk\include;%PATH%
gcc -mms-bitfields -Ic:/GTK/include/gtk-3.0 -Ic:/GTK/include/cairo -Ic:/GTK/include/pango-1.0 -Ic:/GTK/include/atk-1.0 -Ic:/GTK/include/cairo -Ic:/GTK/include/pixman-1 -Ic:/GTK/include -Ic:/GTK/include/freetype2 -Ic:/GTK/include -Ic:/GTK/include/libpng15 -Ic:/GTK/include/gdk-pixbuf-2.0 -Ic:/GTK/include/libpng15 -Ic:/GTK/include/glib-2.0 -Ic:/GTK/lib/glib-2.0/include %*
set PATH=%back%

