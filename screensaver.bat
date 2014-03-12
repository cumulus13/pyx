
@rem ----- ExeScript Options Begin -----
@rem ScriptType: console,silent,invoker
@rem DestDirectory: temp
@rem Icon: default
@rem OutputFile: D:\pyx\screensaver.exe
@rem TimeOut: 2
@rem ----- ExeScript Options End -----
@echo off
title %CD%

%SystemRoot%\system32\control.exe %SystemRoot%\system32\desk.cpl,,1
goto end


:end