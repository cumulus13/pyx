
@rem ----- ExeScript Options Begin -----
@rem ScriptType: console,silent,invoker
@rem DestDirectory: temp
@rem Icon: default
@rem OutputFile: d:\pyx\u.exe
@rem TimeOut: 2
@rem ----- ExeScript Options End -----
@echo off
title %CD%

%SystemRoot%\system32\control.exe %SystemRoot%\system32\%1.cpl,,%2
goto end



:end