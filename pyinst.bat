@echo off

rem setup build -c mingw32 
setup.py install 
setup.py bdist_wininst --skip-build --target-version 2.7
setup.py bdist_wininst --skip-build

goto end


:end
rm -rf build