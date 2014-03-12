
@rem ----- ExeScript Options Begin -----
@rem ScriptType: console,silent,invoker
@rem DestDirectory: temp
@rem Icon: default
@rem OutputFile: d:\pyx\scitex.exe
@rem TimeOut: 1
@rem ----- ExeScript Options End -----
@echo off
title %CD%

"c:\Program Files\Scintilla Text Editor\SciTE.exe" %1

goto end


:end
exit