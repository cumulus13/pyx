@echo off
if %1==-i goto install
if %1==--install goto install
if %1==install goto install
if %1==justinstall goto justinstall
echo process download ...
rem c:\SDK\Anaconda2\Scripts\pip.exe install -d F:\PYTHON_MODULES --no-use-wheel %*
rem c:\SDK\Anaconda2\Scripts\pip.exe install -d F:\PYTHON_MODULES --use-wheel %*
c:\SDK\Anaconda2\Scripts\pip.exe download -d F:\PYTHON_MODULES --no-binary :all: %*
c:\SDK\Anaconda2\Scripts\pip.exe download -d F:\PYTHON_MODULES --only-binary :all: %*
c:\SDK\Anaconda2\Scripts\pip.exe download -d F:\PYTHON_MODULES --only-binary :all:   --no-binary :none: --implementation py %*
rem c:\SDK\Anaconda2\Scripts\pip.exe download -d F:\PYTHON_MODULES %*
rem c:\SDK\Anaconda2\Scripts\pip.exe install -d F:\PYTHON_MODULES --use-wheel %*
 
goto end

:install
rem mkdir F:\PYTHON_MODULES\%2
echo install process ...
c:\SDK\Anaconda2\Scripts\pip.exe download -d F:\PYTHON_MODULES --no-binary :all:  %2
c:\SDK\Anaconda2\Scripts\pip.exe download -d F:\PYTHON_MODULES --only-binary :all: %2
rem c:\SDK\Anaconda2\Scripts\pip.exe download -d F:\PYTHON_MODULES  %2
c:\SDK\Anaconda2\Scripts\pip.exe download -d F:\PYTHON_MODULES --only-binary :all:   --no-binary :none: --implementation py %2
c:\SDK\Anaconda2\Scripts\pip.exe install %2 -i http://127.0.0.1:7777/simple
c:\Anaconda2\Scripts\pip.exe install %2 -i http://127.0.0.1:7777/simple
goto end

:justinstall
c:\SDK\Anaconda2\Scripts\pip.exe install %2 -i http://127.0.0.1:7777/simple
c:\Anaconda2\Scripts\pip.exe install %2 -i http://127.0.0.1:7777/simple
goto end


:end