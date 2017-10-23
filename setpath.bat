
@rem ----- ExeScript Options Begin -----
@rem ScriptType: console,silent,invoker
@rem DestDirectory: temp
@rem Icon: default
@rem OutputFile: d:\pyx\setpath.exe
@rem TimeOut: 10
@rem ----- ExeScript Options End -----
@echo off
title %CD%

start %SystemRoot%\system32\control.exe %SystemRoot%\system32\sysdm.cpl,,3
goto end


:end
