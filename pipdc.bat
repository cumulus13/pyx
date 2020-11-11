@echo off
if %1==-i goto install
if %1==--install goto install
if %1==install goto install
if %1==justinstall goto justinstall
echo process download ...
rem c:\SDK\Anaconda3\Scripts\pip.exe install -d Y:\PYTHON_MODULES --no-use-wheel %*
rem c:\SDK\Anaconda3\Scripts\pip.exe install -d Y:\PYTHON_MODULES --use-wheel %*
echo download for python3 ...
c:\SDK\Anaconda3\Scripts\pip.exe download -i https://pypi.python.org/simple -d Y:\PYTHON_MODULES --no-binary=:all:  %*
c:\SDK\Anaconda3\Scripts\pip.exe download -i https://pypi.python.org/simple -d Y:\PYTHON_MODULES --only-binary=:all:  %*
c:\SDK\Anaconda3\Scripts\pip.exe download -i https://pypi.python.org/simple -d Y:\PYTHON_MODULES --only-binary=:all: --no-binary=:none:  %*
rem c:\SDK\Anaconda3\Scripts\pip.exe download -d Y:\PYTHON_MODULES %*
rem c:\SDK\Anaconda3\Scripts\pip.exe install -d Y:\PYTHON_MODULES --use-wheel %*
echo download for python2 ...
c:\SDK\Anaconda2\Scripts\pip.exe download -i https://pypi.python.org/simple -d Y:\PYTHON_MODULES --no-binary=:all:  %*
c:\SDK\Anaconda2\Scripts\pip.exe download -i https://pypi.python.org/simple -d Y:\PYTHON_MODULES --only-binary=:all:  %*
c:\SDK\Anaconda2\Scripts\pip.exe download -i https://pypi.python.org/simple -d Y:\PYTHON_MODULES --only-binary=:all: --no-binary=:none:  %*

goto end

:install
rem mkdir Y:\PYTHON_MODULES\%2
echo python3 install process ...
echo download no-binary
c:\SDK\Anaconda3\Scripts\pip.exe install -i https://pypi.python.org/simple -d Y:\PYTHON_MODULES --no-binary=:all:  %2
echo download only-binary
c:\SDK\Anaconda3\Scripts\pip.exe install -i https://pypi.python.org/simple -d Y:\PYTHON_MODULES --only-binary=:all:  %2
echo download only-binary and no-binary
rem c:\SDK\Anaconda3\Scripts\pip.exe download -d Y:\PYTHON_MODULES  %2
c:\SDK\Anaconda3\Scripts\pip.exe install -i https://pypi.python.org/simple -d Y:\PYTHON_MODULES --only-binary=:all: --no-binary=:none:  %2
c:\SDK\Anaconda3\Scripts\pip.exe install %2 -i http://127.0.0.1:7777/simple
c:\SDK\Anaconda3\Scripts\pip.exe install %2 -i http://127.0.0.1:7777/simple
echo python2 install process ...
echo download no-binary
c:\SDK\Anaconda2\Scripts\pip.exe install -i https://pypi.python.org/simple -d Y:\PYTHON_MODULES --no-binary=:all:  %2
echo download only-binary
c:\SDK\Anaconda2\Scripts\pip.exe install -i https://pypi.python.org/simple -d Y:\PYTHON_MODULES --only-binary=:all:  %2
echo download only-binary and no-binary
rem c:\SDK\Anaconda2\Scripts\pip.exe download -d Y:\PYTHON_MODULES  %2
c:\SDK\Anaconda2\Scripts\pip.exe install -i https://pypi.python.org/simple -d Y:\PYTHON_MODULES --only-binary=:all: --no-binary=:none:  %2
c:\SDK\Anaconda2\Scripts\pip.exe install %2 -i http://127.0.0.1:7777/simple
c:\SDK\Anaconda2\Scripts\pip.exe install %2 -i http://127.0.0.1:7777/simple
goto end

:justinstall
echo python3 just install process ...
c:\SDK\Anaconda3\Scripts\pip.exe install %2 -i http://127.0.0.1:7777/simple
c:\SDK\Anaconda3\Scripts\pip.exe install %2 -i http://127.0.0.1:7777/simple
echo python2 just install process ...
c:\SDK\Anaconda2\Scripts\pip.exe install %2 -i http://127.0.0.1:7777/simple
c:\SDK\Anaconda2\Scripts\pip.exe install %2 -i http://127.0.0.1:7777/simple
goto end


:end
sendgrowl PIP "pip download" PIPd "pipd download successfull" -t 10 -i "D:\DOWNLOADS\python-logo.jpg"