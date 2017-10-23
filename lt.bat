@echo off
rem if defined %2 goto two
if %1*==* goto one
if %1==-a goto archive
if %1==-d goto directory
if %1==-s goto size
if %1==-n goto three
dir /o:d %* | c:\DevKit\bin\tail.exe -n 47
goto end

:one
if defined %2 goto two
dir /o:d %* | c:\DevKit\bin\tail.exe -n 47
goto end

:two
dir /o:d | c:\DevKit\bin\tail.exe -n %2
goto end

:three
if %1==-n goto two
dir /o:d %* | c:\DevKit\bin\tail.exe -n %2
goto end

:size
dir /a:a /o:s | c:\DevKit\bin\tail.exe -n 47
goto end

:archive
if %2*==* goto archive2
if %2==-n goto archive3
dir /a:a /o:d %2 | c:\DevKit\bin\tail.exe -n 47
goto end

:archive3
dir /a:a /o:d %* | c:\DevKit\bin\tail.exe -n %3 
goto end

:archive2
dir /a:a /o:d %CD% | c:\DevKit\bin\tail.exe -n 47
goto end

:directory
if %2*==* goto directory2
dir /a:d /o:d %2 | c:\DevKit\bin\tail.exe -n 47
goto end

:directory2
dir /a:d /o:d %CD% | c:\DevKit\bin\tail.exe -n 47
goto end

:end
