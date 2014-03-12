@echo off
title %CD%
title %cd%
cls
echo.
echo.
rem C:\cygwin\cin\ls -X -p %1 

if %1*==* goto one
if %1==-d goto directory
if %1==-f goto file
if %1==-t goto timed
if %1==-h goto hide
if %1==-r goto reado
if %1==-n goto cyname
if %1==-e goto cyext
if %1==-s goto cysize
if %1==-help goto help
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
if %1== doc goto doc
if %1==txt goto txt
if %1==edit goto edit
if %1==flv goto flv
if %1==jpg goto jpg
if %1==png goto png
if %1==bmp goto bmp
if %1==gif goto gif
if %1==cbr goto cbr

dir %1
goto end

:gif
dir *.gif
goto end

:cbr
dir *.cbr
goto end


:jpg
dir *.jpg 
goto end

:png
dir *.png 
goto end

:bmp
dir *.bmp 
goto end

:flv
dir *.flv 
goto end

:doc
dir *.doc 
goto end

:txt
dir *.txt 
goto end

:java
dir *.java 
goto end

:jar
dir *.jar 
goto end

:java
dir *.java 
goto end

:class
dir *.class 
goto end

:one
dir %1 %2 
goto end

:cyexe
dir *.exe 
goto end

:pdf
dir *.pdf 
goto end

:cypy
dir *.py 
goto end

:cypl
dir *.pl 
goto more

:cyrc
dir *.rc 
goto end

:cycat
dir *.cat 
goto end

:directory
dir /a:D 
goto end

:file
dir /a:A 
goto end

:timed
dir /o:d 
goto end

:hide
dir /a:h 
goto end

:reado
dir /a:r 
goto end

:cyname
dir /q:n 
goto end

:cyext
dir /o:e 
goto end

:cysize
dir /o:s 
goto end

:cyrar
dir *.rar 
goto end

:cyzip
dir *.zip 
goto end

:cy7zip
dir *.7z 
goto end

:cytar
dir *.tar 
goto end

:cytaz
dir *.taz 
goto end

:cytgz
dir *.tgz 
goto end

:cygz
dir *.gz 
goto end

:cycz2
dir *.cz2 
goto end

:cyczip2
dir *.czip2 
goto end

:cyrpm
dir *.rpm 
goto end

:cyarj
dir *.arj 
goto end

:cycpio
dir *.cpio 
goto end

:cydec
dir *.dec 
goto end

:cyhfs
dir *.hfs 
goto end

:cyiso
dir *.iso 
goto end

:cylha
dir *.lha 
goto end

:cylzh
dir *.lzh 
goto end

:cylzma
dir *.lzma 
goto end

:cysplit
dir *.split 
goto end

:cyswm
dir *.swm 
goto end

:cytcz
dir *.tcz 
goto end

:cytcz2
dir *.tcz2 
goto end

:cytpz
dir *.tpz 
goto end

:cywim
dir *.wim 
goto end

:cyxar
dir *.xar 
goto end

:cyzar
dir *.z 
goto end

:cydmg
dir *.dmg 
goto end

:cyjar
dir *.jar 
goto end

rem sorting with alphaceta
:a
dir a* 
goto end

:b
dir b* 
goto end

:d
dir d* 
goto end

:e
dir e* 
goto end

:f
dir f* 
goto end

:g
dir g* 
goto end

:h
dir h* 
goto end

:i
dir i* 
goto end

:j
dir j* 
goto end

:k
dir k* 
goto end

:l
dir l* 
goto end

:m
dir m* 
goto end

:n
dir n* 
goto end

:o
dir o* 
goto end

:p
dir p* 
goto end

:q
dir q* 
goto end

:r
dir r* 
goto end

:s
dir s* 
goto end

:t
dir t* 
goto end

:u
dir u* 
goto end

:v
dir v* 
goto end

:w
dir w* 
goto end

:x
dir x* 
goto end

:y
dir y* 
goto end

:z
dir z* 
goto end

:edit
scite c:\WINDOWS\system32\lsl.bat
goto end

:help
echo.
echo.
echo			use %0 -d	= list cy Directory
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
echo.
echo							"%cd%"
echo.
echo				For Help use option "-help"
echo.
