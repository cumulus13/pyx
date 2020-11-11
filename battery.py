#!/usr/bin/env python
#coding:utf-8
"""
  Author:  LICFACE --<licface@yahoo.com>
  Purpose: Show Battery Capatsities
  Created: 7/16/2018
"""


import ctypes                                                                                                                        
from ctypes import wintypes                                                                                                          

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

SYSTEM_POWER_STATUS_P = ctypes.POINTER(SYSTEM_POWER_STATUS)                                                                          

GetSystemPowerStatus = ctypes.windll.kernel32.GetSystemPowerStatus                                                                   
GetSystemPowerStatus.argtypes = [SYSTEM_POWER_STATUS_P]                                                                              
GetSystemPowerStatus.restype = wintypes.BOOL                                                                                         

status = SYSTEM_POWER_STATUS()                                                                                                       
if not GetSystemPowerStatus(ctypes.pointer(status)):                                                                                 
    raise ctypes.WinError()

try:
    from make_colors import make_colors
    print make_colors('ACLineStatus', 'red', attrs= ['bold']) + '         =', make_colors(str(status.ACLineStatus), 'white', 'red', attrs= ['bold'])
    print make_colors('BatteryFlag', 'blue', attrs= ['bold']) + '          =', make_colors(str(status.BatteryFlag), 'white', 'blue', attrs= ['bold'])
    print make_colors('BatteryLifePercent', 'cyan', attrs= ['bold']) + '   =', make_colors(str(status.BatteryLifePercent) + " %", 'white', 'cyan', attrs= ['bold'])                                                       
    print make_colors('BatteryLifeTime', 'yellow', attrs= ['bold']) + '      =', make_colors(str(status.BatteryLifeTime), 'white', 'yellow', attrs= ['bold'])                                                             
    print make_colors('BatteryFullLifeTime', 'magenta') + '  =', make_colors(status.BatteryFullLifeTime, 'white', 'magenta', attrs= ['bold'])
except:
    print 'ACLineStatus         =', status.ACLineStatus                                                                   
    print 'BatteryFlag          =', status.BatteryFlag
    print 'BatteryLifePercent   =', status.BatteryLifePercent,"%"                                                       
    print 'BatteryLifeTime      =', status.BatteryLifeTime                                                             
    print 'BatteryFullLifeTime  =', status.BatteryFullLifeTime    