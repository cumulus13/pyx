@echo off
if %1==-i goto install
if %1==--install goto install
if %1==install goto install
if %1==justinstall goto justinstall
echo process download ...
rem c:\SDK\Anaconda2\Scripts\pip.exe install -d D:\PYTHON_MODULES --no-use-wheel %*
rem c:\SDK\Anaconda2\Scripts\pip.exe install -d D:\PYTHON_MODULES --use-wheel %*
c:\SDK\Anaconda2\Scripts\pip.exe download -i https://pypi.python.org/simple -d D:\PYTHON_MODULES --no-binary=:all:  %*
c:\SDK\Anaconda2\Scripts\pip.exe download -i https://pypi.python.org/simple -d D:\PYTHON_MODULES --only-binary=:all:  %*
c:\SDK\Anaconda2\Scripts\pip.exe download -i https://pypi.python.org/simple -d D:\PYTHON_MODULES --only-binary=:all: --no-binary=:none:  %*
rem c:\SDK\Anaconda2\Scripts\pip.exe download -d D:\PYTHON_MODULES %*
rem c:\SDK\Anaconda2\Scripts\pip.exe install -d D:\PYTHON_MODULES --use-wheel %*

goto end

:install
rem mkdir D:\PYTHON_MODULES\%2
echo python2 install process ...
echo download no-binary
c:\SDK\Anaconda2\Scripts\pip.exe install -i https://pypi.python.org/simple -d D:\PYTHON_MODULES --no-binary=:all:  %2
echo download only-binary
c:\SDK\Anaconda2\Scripts\pip.exe install -i https://pypi.python.org/simple -d D:\PYTHON_MODULES --only-binary=:all:  %2
echo download only-binary and no-binary
rem c:\SDK\Anaconda2\Scripts\pip.exe download -d D:\PYTHON_MODULES  %2
c:\SDK\Anaconda2\Scripts\pip.exe install -i https://pypi.python.org/simple -d D:\PYTHON_MODULES --only-binary=:all: --no-binary=:none:  %2
c:\SDK\Anaconda2\Scripts\pip.exe install %2 -i http://127.0.0.1:7777/simple
c:\SDK\Anaconda2\Scripts\pip.exe install %2 -i http://127.0.0.1:7777/simple
goto end

:justinstall
c:\SDK\Anaconda2\Scripts\pip.exe install %2 -i http://127.0.0.1:7777/simple
c:\SDK\Anaconda2\Scripts\pip.exe install %2 -i http://127.0.0.1:7777/simple
goto end


:end
sendgrowl.py -t PIPd -a PIP -m "pipd download successfull" -T 10 -e "pip download" -i "D:\DOWNLOADS\python-logo.jpg"