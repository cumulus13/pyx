@echo off
cd /d "c:\Apps\hgweb"
"c:\Program Files\Mercurial\hg.exe" serve --web-conf=c:\Apps\hgweb\webconf.conf
goto end


:end
rem cd /d %back%
rem exit /b

