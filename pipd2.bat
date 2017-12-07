@echo off
rem c:\SDK\Anaconda2\Scripts\pip.exe install -d F:\PYTHON_MODULES --no-use-wheel %*
rem c:\SDK\Anaconda2\Scripts\pip.exe install -d F:\PYTHON_MODULES --use-wheel %*
c:\SDK\Anaconda2\Scripts\pip.exe download -d F:\PYTHON_MODULES --no-binary all %*
c:\SDK\Anaconda2\Scripts\pip.exe download -d F:\PYTHON_MODULES --only-binary all %*
c:\SDK\Anaconda2\Scripts\pip.exe download -d F:\PYTHON_MODULES %*
c:\SDK\Anaconda2\Scripts\pip.exe install -d F:\PYTHON_MODULES --use-wheel %*