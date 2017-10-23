@echo off
set me0=%CD%
cd /d "f:\CD_DVD_LIST2"
dir /s W: > %1_list.txt
tree /A /F W: > %1_tree.txt
cd /d %me0%
eject cd