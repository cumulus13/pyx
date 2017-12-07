import PySnarl


replyWnd = 'TEST01'
appName = 'TEST1'
replyMsg = 1
icon = r'f:\ICONS\topi4.png'
#b = PySnarl.snRegisterConfig2(replyWnd, appName, replyMsg, icon)
#PySnarl.snRegisterAlert(appName, 'test001')
#PySnarl.snShowMessageEx('TEST01', 'JUST TEST', 'JUST TEST', 3, icon, soundFile= r'f:\sounds\ALARM\Beep.wav')
PySnarl.snShowMessage("RERER", "ETSESET", timeout= 10, iconPath= icon)
#m = PySnarl.SnarlMessage()
#m.setIcon(icon)
#m.setText("BLABLALBLABLLA")
#m.setText('JUST TITLE')
#m.setID(001)
#m.setHwnd(replyWnd)
#m.setClass('TESTX')
#m.show(10, 'TEST 002', 'HELLO', icon, soundPath= r'f:\sounds\ALARM\Beep.wav')
#m.send()
print PySnarl.s


