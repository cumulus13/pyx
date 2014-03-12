@echo off

@echo off
title %CD%
rem notepad c:\license2.txt | "c:\Program Files\Scintilla Text Editor\SciTE.exe" d:\pyx\burn.txt | "c:\Program Files\TagScanner\Tagscan.exe" | "c:\Program Files\MAF-Soft\MP3Test\MP3Test.exe"
start /I call notepad c:\license2.txt 
start /I call "c:\Program Files\TagScanner\Tagscan.exe" 
start /I call "c:\Program Files\MAF-Soft\MP3Test\MP3Test.exe"
goto end

:end
cls
echo.
echo		Edit MP3 tag and scanner ..............
