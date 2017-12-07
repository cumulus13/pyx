@echo off
setup.py build -c mingw32 & setup.py bdist_wininst --skip-build & setup.py bdist_wininst --skip-build --target-version 2.7 & setup.py sdist register -r djangopypi upload -r djangopypi & setup.py sdist register -r chishop upload -r chishop

