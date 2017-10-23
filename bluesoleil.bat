@echo on
if %*==* goto usage
if %1==start goto start
if %1==stop goto stop
if %1==restart goto restart
goto end

:stop
reg import c:\pyx\bluesoleil.reg /reg:32
sc config BsHelpCS start= disabled
sc config BlueSoleilCS start= disabled
sc config cPhoneSDKCS start= disabled
sc stop BsHelpCS
sc stop cPhoneSDKCS
sc stop BlueSoleilCS
px -k bttray.exe
reg import c:\pyx\bluesoleil.reg /reg:32
goto end

:start 
reg import c:\pyx\bluesoleil.reg /reg:32
sc config BsHelpCS start= demand
reg import c:\pyx\bluesoleil.reg /reg:32
sc config BlueSoleilCS start= demand
reg import c:\pyx\bluesoleil.reg /reg:32
sc config cPhoneSDKCS start= demand
reg import c:\pyx\bluesoleil.reg /reg:32
sc start BsHelpCS
reg import c:\pyx\bluesoleil.reg /reg:32
sc start cPhoneSDKCS
reg import c:\pyx\bluesoleil.reg /reg:32
sc start BlueSoleilCS
reg import c:\pyx\bluesoleil.reg /reg:32
set me="%CD%"
rem cd /d "c:\Program Files\IVT Corporation\BlueSoleil"
reg import c:\pyx\bluesoleil.reg /reg:32
rem BtTray.exe
cd /d %me%
reg import c:\pyx\bluesoleil.reg /reg:32
goto end

:restart
net stop BsHelpCS
net stop cPhoneSDKCS
net stop BlueSoleilCS
px -k bttray.exe
goto start

:end
reg import c:\pyx\bluesoleil.reg /reg:32