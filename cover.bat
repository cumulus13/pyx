@echo off

if %1*==* goto usage
if %1==/? goto usage
if %1==help goto usage
if %1==-help goto usage
if %1==--help goto usage
if %1==-h goto usage
if %1==--h goto usage

if %1==all goto all
if %1==!front goto notfront
if %1==!folder goto notfolder
if %1==!folder1 goto notfolder1
if %1==!cover goto notcover

goto end

:all
copy /-Y %2 Folder.jpg
copy /-Y %2 Folder1.jpg
copy /-Y %2 Cover.jpg
copy /-Y %2 Front.jpg
goto end

:notfront
copy /-Y %2 Folder.jpg
copy /-Y %2 Folder1.jpg
copy /-Y %2 Cover.jpg
goto end

:notfolder
copy /-Y %2 Folder1.jpg
copy /-Y %2 Cover.jpg
copy /-Y %2 Front.jpg
goto end

:notfolder1
copy /-Y %2 Folder.jpg
copy /-Y %2 Cover.jpg
copy /-Y %2 Front.jpg
goto end

:notcover
copy /-Y %2 Folder.jpg
copy /-Y %2 Folder1.jpg
copy /-Y %2 Front.jpg
goto end

:usage
echo.
echo        use : %0 [all/!folder/!folder1/!cover/!front]
echo.
goto end

:end