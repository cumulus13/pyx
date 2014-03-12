@echo off
title %CD%

"C:\Program Files\NetBeans 6.8\ruby2\jruby-1.4.0\bin\jruby.exe" "C:\Program Files\NetBeans 6.8\ruby2\jruby-1.4.0\bin\jgem" %1 %2
goto end


:end