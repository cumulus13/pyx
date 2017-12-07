
import ctypes
from ctypes import wintypes
import sys
import winsound
import traceback
import time

class SYSTEM_POWER_STATUS(ctypes.Structure):
    _fields_ = [
        ('ACLineStatus', wintypes.BYTE),
        ('BatteryFlag', wintypes.BYTE),
        ('BatteryLifePercent', wintypes.BYTE),
        ('Reserved1', wintypes.BYTE),
        ('BatteryLifeTime', wintypes.DWORD),
        ('BatteryFullLifeTime', wintypes.DWORD),
    ]

def convertTime(sec):pass

def check():
    SYSTEM_POWER_STATUS_P = ctypes.POINTER(SYSTEM_POWER_STATUS)

    GetSystemPowerStatus = ctypes.windll.kernel32.GetSystemPowerStatus
    GetSystemPowerStatus.argtypes = [SYSTEM_POWER_STATUS_P]
    GetSystemPowerStatus.restype = wintypes.BOOL

    status = SYSTEM_POWER_STATUS()
    if not GetSystemPowerStatus(ctypes.pointer(status)):
        raise ctypes.WinError()

    print 'ACLineStatus         =', status.ACLineStatus
    print 'BatteryFlag          =', status.BatteryFlag
    print 'BatteryLifePercent   =', status.BatteryLifePercent,"%"
    print 'BatteryLifeTime      =', status.BatteryLifeTime
    print 'BatteryFullLifeTime  =', status.BatteryFullLifeTime

    return status.ACLineStatus

while True:
    try:
        onLine = check()
        if onLine == 0:
            print "AAA"
            print 'ACLineStatus         =', onLine
            winsound.PlaySound(r'f:\SOUNDS\WAV\06. Alarm 6.wav', winsound.SND_FILENAME)
        # elif status.ACLineStatus == "0":
        #     print "BBB"
        #     winsound.PlaySound(r'f:\SOUNDS\WAV\06. Alarm 6.wav', winsound.SND_FILENAME)
        else:
            onLine = check()
            print 'ACLineStatus         =', onLine
            time.sleep(1)
    except KeyboardInterrupt:
        sys.exit(0)
    except:
        print traceback.format_ext()
        time.sleep(1)
# print 'ACLineStatus         =', status.ACLineStatus
# print 'BatteryFlag          =', status.BatteryFlag
# print 'BatteryLifePercent   =', status.BatteryLifePercent,"%"
# print 'BatteryLifeTime      =', status.BatteryLifeTime
# print 'BatteryFullLifeTime  =', status.BatteryFullLifeTime
