@echo off
title %CD%

copy "I:\FROM C\dir2html\"*.gif
copy "I:\FROM C\dir2html\"*.ion
"I:\FROM C\dir2html\dir2html-win32.exe" 
"I:\FROM C\dir2html\describe-win32.exe" -get *.*

goto end


:end