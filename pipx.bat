@echo off
if %1==-i goto install
if %1==--install goto install
rem c:\SDK\Anaconda2\Scripts\pip.exe install -d F:\PYTHON_MODULES --no-use-wheel %*
rem c:\SDK\Anaconda2\Scripts\pip.exe install -d F:\PYTHON_MODULES --use-wheel %*
c:\SDK\Anaconda2\Scripts\pip.exe download -d F:\PYTHON_MODULES --no-binary all %*
c:\SDK\Anaconda2\Scripts\pip.exe download -d F:\PYTHON_MODULES --only-binary all %*
c:\SDK\Anaconda2\Scripts\pip.exe download -d F:\PYTHON_MODULES %*
c:\SDK\Anaconda2\Scripts\pip.exe install -d F:\PYTHON_MODULES --use-wheel %*
goto end

:install
c:\SDK\Anaconda2\Scripts\pip.exe download -d F:\PYTHON_MODULES --no-binary all  %2
c:\SDK\Anaconda2\Scripts\pip.exe download -d F:\PYTHON_MODULES --only-binary all  %2
c:\SDK\Anaconda2\Scripts\pip.exe download -d F:\PYTHON_MODULES  %2
c:\SDK\Anaconda2\Scripts\pip.exe install -d F:\PYTHON_MODULES --use-wheel %2
c:\SDK\Anaconda2\Scripts\pip.exe install %2
goto end


:end