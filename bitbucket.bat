@echo off
set one=%CD%
c:\Apps\curl-7.46.0-win32-mingw\bin\curl.exe --user licface@yahoo.com:blackid-licface2 https://api.bitbucket.org/1.0/repositories/ --data name=%1
cd "%1"
git push https://licface:blackid-licface2@bitbucket.org/licface/%1 master
git push https://licface:blackid-licface2@bitbucket.org/licface/%1 --tag
cd /d %one%