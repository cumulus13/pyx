
@rem ----- ExeScript Options Begin -----
@rem ScriptType: console,silent,invoker
@rem DestDirectory: temp
@rem Icon: default
@rem OutputFile: D:\pyx\screensaver.exe
@rem TimeOut: 2
@rem ----- ExeScript Options End -----
@echo off
title %CD%

rem %SystemRoot%\system32\control.exe %SystemRoot%\system32\desk.cpl,,1
goto end
"C:\WINDOWS\system32\rundll32.exe" shell32.dll,Control_RunDLL desk.cpl,screensaver,@screensaver


:end