@echo off
set me=%CD%
cd /d c:\TOOLS\PentestBox
SET pentestbox_ROOT=c:\TOOLS\PentestBox
start c:/TOOLS/PentestBox/base/conemu-maximus5/ConEmu.exe /Icon "%pentestbox_ROOT%\pentestbox.ico" /Title "Pentest Box" /LoadCfgFile "%pentestbox_ROOT%\config\ConEmu.xml"
cd /d "%me%"