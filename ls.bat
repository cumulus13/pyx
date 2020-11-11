@echo off
title %CD%
rem if %1*==* goto one
title %cd%
cls & echo. & echo.
rem echo.
rem echo.
rem D:\cygwin\cin\ls -X -p %1 


if %1*==* goto one
if %1==-d goto lsdir
if %1==-f goto file
if %1==-t goto timed
if %1==-h goto hide
if %1==-r goto reado
if %1==-n goto cyname
if %1==-e goto cyext
if %1==-s goto cysize
if %1==-help goto help
if %1==bat goto bat
if %1==chm goto chm
if %1==rar goto cyrar
if %1==jar goto cyjar
if %1==zip goto cyzip
if %1==7z  goto cy7zip
if %1==tar goto cytar
if %1==tgz goto cytgz
if %1==gz  goto cygz
if %1==rpm goto cyrpm
if %1==cz2 goto cycz2
if %1==czip2 goto cyczip2
if %1==arj goto cyarj
if %1==cac goto cycac
if %1==cpio goto cycpio
if %1==dec goto cydec
if %1==gzip goto cygzip
if %1==hfs goto cyhfs
if %1==iso goto cyiso
if %1==lha goto cylha
if %1==lzh goto cylzh
if %1==lzma goto cylzma
if %1==split goto cysplit
if %1==swm goto cyswm
if %1==taz goto cytaz
if %1==tcz goto cytcz
if %1==tcz2 goto cytcz2
if %1==tpz goto cytpz
if %1==wim goto cywim
if %1==xar goto cyxar
if %1==zar goto cyzar
if %1==dmg goto cydmg
if %1==py goto cypy
if %1==pl goto cypl
if %1==pdf goto pdf
if %1==rc goto cyrc
if %1==cat goto cycat
if %1==exe goto cyexe
if %1==a goto a
if %1==b goto b
if %1==b goto b
if %1==c goto c
if %1==d goto d
if %1==e goto e
if %1==f goto f
if %1==g goto g
if %1==h goto h
if %1==i goto i
if %1==j goto j
if %1==k goto k
if %1==l goto l
if %1==m goto m
if %1==n goto n
if %1==o goto o
if %1==p goto p
if %1==q goto q
if %1==r goto r
if %1==s goto s
if %1==t goto t
if %1==u goto u
if %1==v goto v
if %1==w goto w
if %1==x goto x
if %1==y goto y
if %1==z goto z
if %1==java goto java
if %1==class goto class
if %1==jar goto jar
if %1==doc goto doc
if %1==txt goto txt
if %1==edit goto edit
if %1==flv goto flv
if %1==jpg goto jpg
if %1==png goto png
if %1==bmp goto bmp
if %1==gif goto gif
if %1==cbr goto cbr
if %1==cpp goto cpp
if %1==rb goto rb
if %1==mp3 goto mp3
if %1==images goto images

dir /o:e %1  | more
goto end

:lsdir
dir /o:n /d /a:d %2
goto end

:images
dir *.jpg;*.png;*.bmp;*.gif;*.jpeg
goto end

:bat
dir /o:e *.bat | more
goto end

:cpp
dir /o:e *.c | more
goto end

:mp3
dir /o:e *.mp3 | more
goto end

:rb
dir /o:e *.rb | more
goto end

:gif 
dir /o:e *.gif | more
goto end

:cbr
dir /o:e *.cbr | more
goto end

:jpg
dir /o:e *.jpg | more
goto end

:png
dir /o:e *.png | more
goto end

:bmp
dir /o:e *.bmp | more
goto end

:flv
dir /o:e *.flv | more
goto end

:doc
dir /o:e *.doc | more
goto end

:txt
dir /o:e *.txt | more
goto end

:java
dir /o:e *.java | more
goto end

:jar
dir /o:e *.jar | more
goto end

:java
dir /o:e *.java | more
goto end

:class
dir /o:e *.class | more
goto end

:one
rem dir /o:e %1 %2 | more
dir /o:n /d %1 %2
goto end

:cyexe
dir /o:e *.exe | more
goto end

:chm
dir /o:e *.chm | more
goto end

:pdf
dir /o:e *.pdf | more
goto end

:cypy
dir /o:e *.py | more
goto end

:cypl
dir /o:e *.pl | more
goto more

:cyrc
dir /o:e *.rc | more
goto end

:cycat
dir /o:e *.cat | more
goto end

:dir /o:eectory
dir /o:e /a:D | more
goto end

:file
dir /o:e /a:A | more
goto end

:timed
dir /w /o:-d
goto end

:hide
dir /o:e /a:h | more
goto end

:reado
dir /o:e /a:r | more
goto end

:cyname
dir /o:e /q:n | more
goto end

:cyext
dir /o:e /o:e | more
goto end

:cysize
dir /o:s | more
goto end

:cyrar
dir /o:e *.rar | more
goto end

:cyzip
dir /o:e *.zip | more
goto end

:cy7zip
dir /o:e *.7z | more
goto end

:cytar
dir /o:e *.tar | more
goto end

:cytaz
dir /o:e *.taz | more
goto end

:cytgz
dir /o:e *.tgz | more
goto end

:cygz
dir /o:e *.gz | more
goto end

:cycz2
dir /o:e *.cz2 | more
goto end

:cyczip2
dir /o:e *.czip2 | more
goto end

:cyrpm
dir /o:e *.rpm | more
goto end

:cyarj
dir /o:e *.arj | more
goto end

:cycpio
dir /o:e *.cpio | more
goto end

:cydec
dir /o:e *.dec | more
goto end

:cyhfs
dir /o:e *.hfs | more
goto end

:cyiso
dir /o:e *.iso | more
goto end

:cylha
dir /o:e *.lha | more
goto end

:cylzh
dir /o:e *.lzh | more
goto end

:cylzma
dir /o:e *.lzma | more
goto end

:cysplit
dir /o:e *.split | more
goto end

:cyswm
dir /o:e *.swm | more
goto end

:cytcz
dir /o:e *.tcz | more
goto end

:cytcz2
dir /o:e *.tcz2 | more
goto end

:cytpz
dir /o:e *.tpz | more
goto end

:cywim
dir /o:e *.wim | more
goto end

:cyxar
dir /o:e *.xar | more
goto end

:cyzar
dir /o:e *.z | more
goto end

:cydmg
dir /o:e *.dmg | more
goto end

:cyjar
dir /o:e *.jar | more
goto end

rem sorting with alphaceta
:a
rem dir /o:e a* | more
dir /a:a a* | more
goto end

:b
dir /o:e b* | more
goto end

:d
dir /o:e d* | more
goto end

:e
dir /o:e e* | more
goto end

:f
dir /o:e f* | more
goto end

:g
dir /o:e g* | more
goto end

:h
dir /o:e h* | more
goto end

:i
dir /o:e i* | more
goto end

:j
dir /o:e j* | more
goto end

:k
dir /o:e k* | more
goto end

:l
dir /o:e l* | more
goto end

:m
dir /o:e m* | more
goto end

:n
dir /o:e n* | more
goto end

:o
dir /o:e o* | more
goto end

:p
dir /o:e p* | more
goto end

:q
dir /o:e q* | more
goto end

:r
dir /o:e r* | more
goto end

:s
dir /o:e s* | more
goto end

:t
dir /o:e t* | more
goto end

:u
dir /o:e u* | more
goto end

:v
dir /o:e v* | more
goto end

:w
dir /o:e w* | more
goto end

:x
dir /o:e x* | more
goto end

:y
dir /o:e y* | more
goto end

:z
dir /o:e z* | more
goto end

:edit
scite c:\WINDOWS\system32\ls.bat
goto end

:help
echo.
echo.
echo			use %0 -d	= list cy dir /o:eectory
echo			       -f	= list cy File
echo			       -t	= list cy Time Modified {Ascending}
echo			       -n	= list cy Name Of File
echo			       -e	= list cy Extentsion Of File
echo			       -s	= list cy Size Of File
echo			       -h	= show File Hidden Attricute
echo			       -r	= show file Read Only Attricute
echo			       -help	= This Option Help Of this file
echo.

:end
rem echo.
rem echo							"%cd%"
rem echo.
rem echo				For Help use option "-help"
rem echo.

:end2

