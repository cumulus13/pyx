@echo off
hg update --repository "%1" --verbose --config ui.merge=internal:fail --rev "%2" --clean
goto end


:end
