@echo off
del "d:\LIST_DIRECTORY\LIST\*.txt
del "d:\LIST_DIRECTORY\TREE\*.txt
title %CD%
if %1*==* goto usage
if %1==generate goto generate
if %1==list goto list
if %2==--with-halt goto halt
if %2==--with-reboot goto reboot
if %2==--with-logoff goto logoff

:list
if %2*==* goto usage

tree /A /F %2:\ > d:\LIST_DIRECTORY\TREE\%2_tree.txt
dir /s %2:\ > d:\LIST_DIRECTORY\LIST\%2_list.txt
rem d:\LIST_DIRECTORY\atur.bat
rem Dialog.py
goto fin


:generate
tree /A /F C:\ > d:\LIST_DIRECTORY\TREE\C_tree.txt
dir /s C:\ > d:\LIST_DIRECTORY\LIST\C_list.txt

tree /A /F D:\ > d:\LIST_DIRECTORY\TREE\D_tree.txt
dir /s D:\ > d:\LIST_DIRECTORY\LIST\D_list.txt

tree /A /F E:\ > d:\LIST_DIRECTORY\TREE\E_tree.txt
dir /s e:\ > d:\LIST_DIRECTORY\LIST\E_list.txt

tree /A /F F:\ > d:\LIST_DIRECTORY\TREE\F_tree.txt
dir /s F:\ > d:\LIST_DIRECTORY\LIST\F_list.txt

tree /A /F G:\ > d:\LIST_DIRECTORY\TREE\G_tree.txt
dir /s G:\ > d:\LIST_DIRECTORY\LIST\G_list.txt

tree /A /F H:\ > d:\LIST_DIRECTORY\TREE\H_tree.txt
dir /s H:\ > d:\LIST_DIRECTORY\LIST\H_list.txt

tree /A /F I:\ > d:\LIST_DIRECTORY\TREE\I_tree.txt
dir /s I:\ > d:\LIST_DIRECTORY\LIST\I_list.txt

tree /A /F J:\ > d:\LIST_DIRECTORY\TREE\J_tree.txt
dir /s J:\ > d:\LIST_DIRECTORY\LIST\J_list.txt

tree /A /F K:\ > d:\LIST_DIRECTORY\TREE\K_tree.txt
dir /s K:\ > d:\LIST_DIRECTORY\LIST\K_list.txt

tree /A /F L:\ > d:\LIST_DIRECTORY\TREE\L_tree.txt
dir /s L:\ > d:\LIST_DIRECTORY\LIST\L_list.txt

tree /A /F M:\ > d:\LIST_DIRECTORY\TREE\M_tree.txt
dir /s M:\ > d:\LIST_DIRECTORY\LIST\M_list.txt

tree /A /F N:\ > d:\LIST_DIRECTORY\TREE\N_tree.txt
dir /s N:\ > d:\LIST_DIRECTORY\LIST\N_list.txt

tree /A /F O:\ > d:\LIST_DIRECTORY\TREE\O_tree.txt
dir /s O:\ > d:\LIST_DIRECTORY\LIST\O_list.txt

rem d:\LIST_DIRECTORY\atur.bat
rem Dialog.py
rem sysloggen -t:192.168.128.1 -p:516 -s:5 -f:0 -m:"Listing General Harddisk File Info is SUCCESSFULL Done !" 
goto fin

:halt
tree /A /F C:\ > d:\LIST_DIRECTORY\TREE\C_tree.txt
dir /s C:\ > d:\LIST_DIRECTORY\LIST\C_list.txt

tree /A /F D:\ > d:\LIST_DIRECTORY\TREE\D_tree.txt
dir /s D:\ > d:\LIST_DIRECTORY\LIST\D_list.txt

tree /A /F E:\ > d:\LIST_DIRECTORY\TREE\E_tree.txt
dir /s e:\ > d:\LIST_DIRECTORY\LIST\E_list.txt

tree /A /F F:\ > d:\LIST_DIRECTORY\TREE\F_tree.txt
dir /s F:\ > d:\LIST_DIRECTORY\LIST\F_list.txt

tree /A /F G:\ > d:\LIST_DIRECTORY\TREE\G_tree.txt
dir /s G:\ > d:\LIST_DIRECTORY\LIST\G_list.txt

tree /A /F H:\ > d:\LIST_DIRECTORY\TREE\H_tree.txt
dir /s H:\ > d:\LIST_DIRECTORY\LIST\H_list.txt

tree /A /F I:\ > d:\LIST_DIRECTORY\TREE\I_tree.txt
dir /s I:\ > d:\LIST_DIRECTORY\LIST\I_list.txt

tree /A /F J:\ > d:\LIST_DIRECTORY\TREE\J_tree.txt
dir /s J:\ > d:\LIST_DIRECTORY\LIST\J_list.txt

tree /A /F K:\> d:\LIST_DIRECTORY\TREE\K_tree.txt
dir /s K:\> d:\LIST_DIRECTORY\LIST\K_list.txt

tree /A /F L:\ > d:\LIST_DIRECTORY\TREE\L_tree.txt
dir /s L:\ > d:\LIST_DIRECTORY\LIST\L_list.txt

tree /A /F M:\ > d:\LIST_DIRECTORY\TREE\M_tree.txt
dir /s M:\ > d:\LIST_DIRECTORY\LIST\M_list.txt

tree /A /F N:\ > d:\LIST_DIRECTORY\TREE\N_tree.txt
dir /s N:\ > d:\LIST_DIRECTORY\LIST\N_list.txt

tree /A /F O:\ > d:\LIST_DIRECTORY\TREE\O_tree.txt
dir /s O:\ > d:\LIST_DIRECTORY\LIST\O_list.txt

rem d:\LIST_DIRECTORY\atur.bat
rem Dialog.py
rem sysloggen -t:192.168.128.1 -p:516 -s:5 -f:0 -m:"Listing General Harddisk File Info is SUCCESSFULL Done !" 
goto halt2

:reboot
tree /A /F C:\ > d:\LIST_DIRECTORY\TREE\C_tree.txt
dir /s C:\ > d:\LIST_DIRECTORY\LIST\C_list.txt

tree /A /F D:\ > d:\LIST_DIRECTORY\TREE\D_tree.txt
dir /s D:\ > d:\LIST_DIRECTORY\LIST\D_list.txt

tree /A /F E:\ > d:\LIST_DIRECTORY\TREE\E_tree.txt
dir /s e:\ > d:\LIST_DIRECTORY\LIST\E_list.txt

tree /A /F F:\ > d:\LIST_DIRECTORY\TREE\F_tree.txt
dir /s F:\ > d:\LIST_DIRECTORY\LIST\F_list.txt

tree /A /F G:\ > d:\LIST_DIRECTORY\TREE\G_tree.txt
dir /s G:\ > d:\LIST_DIRECTORY\LIST\G_list.txt

tree /A /F H:\ > d:\LIST_DIRECTORY\TREE\H_tree.txt
dir /s H:\ > d:\LIST_DIRECTORY\LIST\H_list.txt

tree /A /F I:\ > d:\LIST_DIRECTORY\TREE\I_tree.txt
dir /s I:\ > d:\LIST_DIRECTORY\LIST\I_list.txt

tree /A /F J:\ > d:\LIST_DIRECTORY\TREE\J_tree.txt
dir /s J:\ > d:\LIST_DIRECTORY\LIST\J_list.txt

tree /A /F K:\> d:\LIST_DIRECTORY\TREE\K_tree.txt
dir /s K:\> d:\LIST_DIRECTORY\LIST\K_list.txt

tree /A /F L:\ > d:\LIST_DIRECTORY\TREE\L_tree.txt
dir /s L:\ > d:\LIST_DIRECTORY\LIST\L_list.txt

tree /A /F M:\ > d:\LIST_DIRECTORY\TREE\M_tree.txt
dir /s M:\ > d:\LIST_DIRECTORY\LIST\M_list.txt

tree /A /F N:\ > d:\LIST_DIRECTORY\TREE\N_tree.txt
dir /s N:\ > d:\LIST_DIRECTORY\LIST\N_list.txt

tree /A /F O:\ > d:\LIST_DIRECTORY\TREE\O_tree.txt
dir /s O:\ > d:\LIST_DIRECTORY\LIST\O_list.txt

rem d:\LIST_DIRECTORY\atur.bat
rem Dialog.py
rem sysloggen -t:192.168.128.1 -p:516 -s:5 -f:0 -m:"Listing General Harddisk File Info is SUCCESSFULL Done !" 
goto reboot2

:logoff
tree /A /F C:\ > d:\LIST_DIRECTORY\TREE\C_tree.txt
dir /s C:\ > d:\LIST_DIRECTORY\LIST\C_list.txt

tree /A /F D:\ > d:\LIST_DIRECTORY\TREE\D_tree.txt
dir /s D:\ > d:\LIST_DIRECTORY\LIST\D_list.txt

tree /A /F E:\ > d:\LIST_DIRECTORY\TREE\E_tree.txt
dir /s e:\ > d:\LIST_DIRECTORY\LIST\E_list.txt

tree /A /F F:\ > d:\LIST_DIRECTORY\TREE\F_tree.txt
dir /s F:\ > d:\LIST_DIRECTORY\LIST\F_list.txt

tree /A /F G:\ > d:\LIST_DIRECTORY\TREE\G_tree.txt
dir /s G:\ > d:\LIST_DIRECTORY\LIST\G_list.txt

tree /A /F H:\ > d:\LIST_DIRECTORY\TREE\H_tree.txt
dir /s H:\ > d:\LIST_DIRECTORY\LIST\H_list.txt

tree /A /F I:\ > d:\LIST_DIRECTORY\TREE\I_tree.txt
dir /s I:\ > d:\LIST_DIRECTORY\LIST\I_list.txt

tree /A /F J:\ > d:\LIST_DIRECTORY\TREE\J_tree.txt
dir /s J:\ > d:\LIST_DIRECTORY\LIST\J_list.txt

tree /A /F K:\> d:\LIST_DIRECTORY\TREE\K_tree.txt
dir /s K:\> d:\LIST_DIRECTORY\LIST\K_list.txt

tree /A /F L:\ > d:\LIST_DIRECTORY\TREE\L_tree.txt
dir /s L:\ > d:\LIST_DIRECTORY\LIST\L_list.txt

tree /A /F M:\ > d:\LIST_DIRECTORY\TREE\M_tree.txt
dir /s M:\ > d:\LIST_DIRECTORY\LIST\M_list.txt

tree /A /F N:\ > d:\LIST_DIRECTORY\TREE\N_tree.txt
dir /s N:\ > d:\LIST_DIRECTORY\LIST\N_list.txt

tree /A /F O:\ > d:\LIST_DIRECTORY\TREE\O_tree.txt
dir /s O:\ > d:\LIST_DIRECTORY\LIST\O_list.txt

rem d:\LIST_DIRECTORY\atur.bat
rem Dialog.py
rem sysloggen -t:192.168.128.1 -p:516 -s:5 -f:0 -m:"Listing General Harddisk File Info is SUCCESSFULL Done !" 
goto logoff2

:error
echo.
echo.
echo          dRIVE IS nOT aVAILABLE !!!!!
echo.
echo
goto end

:usage
echo.
echo.
echo        Usage : %0 list [Directory] [example %0 list e]
echo		       %0 Generate      [Generate List and Tree all of Directory]
echo                %0 list
echo                %0 --with-halt   [Generate All and Shutdown computer]
echo                %0 --with-reboot [Generate All and Reboot computer]
echo                %0 --with-logoff [Generate All and Logoff computer]
echo.
echo.
goto nofin



:end
rem Dialog.py
goto fin

:halt2

shutdown -s -t 10 -f -c "komputer akan di matikan dalam 10 detik"
rem Dialog.py
rem sysloggen -t:192.168.128.1 -p:516 -s:5 -f:0 -m:"Listing General Harddisk File Info is SUCCESSFULL Done !" 
goto fin

:reboot2

shutdown -r -t 10 -f -c "komputer akan di restart dalam 10 detik"
rem Dialog.py
rem sysloggen -t:192.168.128.1 -p:516 -s:5 -f:0 -m:"Listing General Harddisk File Info is SUCCESSFULL Done !" 
goto fin

:logoff2

shutdown -l -t 10 -f -c "komputer akan di logoff dalam 10 detik"
rem Dialog.py
rem sysloggen -t:192.168.128.1 -p:516 -s:5 -f:0 -m:"Listing General Harddisk File Info is SUCCESSFULL Done !" 
goto fin


:fin
rem Dialog.py
rem "c:\Python25\python.exe" "d:\pyx\listhdd_sound.py"

:nofin
