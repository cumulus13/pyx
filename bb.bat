@echo off
if %1==clone goto clone
goto end

:clone
hg clone https://licface:blackid-licface2@bitbucket.org/licface/%2
goto end


:end
