@echo off
rem c:\Anaconda2\Scripts\pip.exe install -d F:\PYTHON_MODULES --no-use-wheel %*
rem c:\Anaconda2\Scripts\pip.exe install -d F:\PYTHON_MODULES --use-wheel %*
c:\Anaconda2\Scripts\pip.exe download -d F:\PYTHON_MODULES --no-binary all %*
c:\Anaconda2\Scripts\pip.exe download -d F:\PYTHON_MODULES --only-binary all %*
c:\Anaconda2\Scripts\pip.exe download -d F:\PYTHON_MODULES %*
c:\Anaconda2\Scripts\pip.exe install -d F:\PYTHON_MODULES --use-wheel %*