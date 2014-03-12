@echo off
title %CD%
title %cd%
cls
echo.
echo.
rem C:\cygwin\bin\ls -X -p %1 

if %1*==* goto one
if %1==-d goto directory
if %1==-f goto file
if %1==-t goto timed
if %1==-h goto hide
if %1==-r goto reado
if %1==-n goto byname
if %1==-e goto byext
if %1==-s goto bysize
if %1==-help goto help
if %1==rar goto byrar
if %1==jar goto byjar
if %1==zip goto byzip
if %1==7z  goto by7zip
if %1==tar goto bytar
if %1==tgz goto bytgz
if %1==gz  goto bygz
if %1==rpm goto byrpm
if %1==bz2 goto bybz2
if %1==bzip2 goto bybzip2
if %1==arj goto byarj
if %1==cab goto bycab
if %1==cpio goto bycpio
if %1==deb goto bydeb
if %1==gzip goto bygzip
if %1==hfs goto byhfs
if %1==iso goto byiso
if %1==lha goto bylha
if %1==lzh goto bylzh
if %1==lzma goto bylzma
if %1==split goto bysplit
if %1==swm goto byswm
if %1==taz goto bytaz
if %1==tbz goto bytbz
if %1==tbz2 goto bytbz2
if %1==tpz goto bytpz
if %1==wim goto bywim
if %1==xar goto byxar
if %1==zar goto byzar
if %1==dmg goto bydmg
if %1==py goto bypy
if %1==pl goto bypl
if %1==rb goto byrb
if %1==bat goto bybat
if %1==exe goto byexe

:one
dir %1 %2 | more
goto end

:byexe
dir *.exe | more
goto end

:bypy
dir *.py | more
goto end

:bypl
dir *.pl | more
goto more

:byrb
dir *.rb | more
goto end

:bybat
dir *.bat | more
goto end

:directory
dir /a:D | more
goto end

:file
dir /a:A | more
goto end

:timed
dir /o:d | more
goto end

:hide
dir /a:h | more
goto end

:reado
dir /a:r | more
goto end

:byname
dir /q:n | more
goto end

:byext
dir /o:e | more
goto end

:bysize
dir /o:s | more
goto end

:byrar
dir *.rar | more
goto end

:byzip
dir *.zip | more
goto end

:by7zip
dir *.7z | more
goto end

:bytar
dir *.tar | more
goto end

:bytaz
dir *.taz | more
goto end

:bytgz
dir *.tgz | more
goto end

:bygz
dir *.gz | more
goto end

:bybz2
dir *.bz2 | more
goto end

:bybzip2
dir *.bzip2 | more
goto end

:byrpm
dir *.rpm | more
goto end

:byarj
dir *.arj | more
goto end

:bycpio
dir *.cpio | more
goto end

:bydeb
dir *.deb | more
goto end

:byhfs
dir *.hfs | more
goto end

:byiso
dir *.iso | more
goto end

:bylha
dir *.lha | more
goto end

:bylzh
dir *.lzh | more
goto end

:bylzma
dir *.lzma | more
goto end

:bysplit
dir *.split | more
goto end

:byswm
dir *.swm | more
goto end

:bytbz
dir *.tbz | more
goto end

:bytbz2
dir *.tbz2 | more
goto end

:bytpz
dir *.tpz | more
goto end

:bywim
dir *.wim | more
goto end

:byxar
dir *.xar | more
goto end

:byzar
dir *.z | more
goto end

:bydmg
dir *.dmg | more
goto end

:byjar
dir *.jar | more
goto end

:help
echo.
echo.
echo			use %0 -d	= list by Directory
echo			       -f	= list by File
echo			       -t	= list by Time Modified {Ascending}
echo			       -n	= list by Name Of File
echo			       -e	= list by Extentsion Of File
echo			       -s	= list by Size Of File
echo			       -h	= show File Hidden Attribute
echo			       -r	= show file Read Only Attribute
echo			       -help	= This Option Help Of this file
echo.

:end
echo.
echo							"%cd%"
echo.
echo				For Help use option "-help"
echo.
