#!/use/bin/python

import os
import sys
# from _winreg import *
# import win32con
# import win32com.client
import termcolor
import random

data_random = ['red', 'yellow', 'green', 'blue', 'cyan', 'magenta', 'grey']


def writereg(name, parent, keyval, reg_type, value):
    import _winreg
    # keyval = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
    if not os.path.exists(keyval):
        keyval = _winreg.CreateKey(_winreg.HKEY_LOCAL_MACHINE, keyval)
    # RegKey = OpenKey(HKEY_LOCAL_MACHINE, keyval, 0, KEY_WRITE)
    RegKey = _winreg.OpenKey(parent, keyval, 0, _winreg.KEY_WRITE)
    # SetValueEx(RegKey, name, 0, REG_SZ, path)
    _winreg.SetValueEx(RegKey, name, 0, reg_type, value)
    _winreg.CloseKey(RegKey)
    print termcolor.colored("Add {0}: {1}".format(name, value), random.choice(data_random))


def setParameter(data):
    import _winreg
    data_key = {
        1: {
            'name': 'IPAddress',
            'value': data,
            'path': 'SYSTEM\ControlSet001\Services\{76AC6BB9-4C7D-4EEE-A241-F483F94672B3}\Parameters\Tcpip',
            'type': _winreg.REG_MULTI_SZ,
            'parent': 'HKEY_LOCAL_MACHINE'
            },
        2: {
            'name': 'IPAddress',
            'value': data,
            'path': 'SYSTEM\CurrentControlSet\Services\{76AC6BB9-4C7D-4EEE-A241-F483F94672B3}\Parameters\Tcpip',
            'type': _winreg.REG_MULTI_SZ,
            'parent': 'HKEY_LOCAL_MACHINE'
            },
        3: {
            'name': 'NameServer',
            'value': data,
            'path': 'SYSTEM\ControlSet001\Services\Tcpip\Parameters\Interfaces\{4fa65d49-0b51-4503-9248-53cec562af54}\25F4554554250223',
            'type': _winreg.REG_SZ,
            'parent': 'HKEY_LOCAL_MACHINE'
            },
        4: {
            'name': 'NameServer',
            'value': data,
            'path': 'SYSTEM\ControlSet001\Services\Tcpip\Parameters\Interfaces\{4fa65d49-0b51-4503-9248-53cec562af54}\4445D21303030205C65737F5637373',
            'type': _winreg.REG_SZ,
            'parent': 'HKEY_LOCAL_MACHINE'
            },
        5: {
            'name': 'NameServer',
            'value': data,
            'path': 'SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces\{4fa65d49-0b51-4503-9248-53cec562af54}\25F4554554250223',
            'type': _winreg.REG_SZ,
            'parent': 'HKEY_LOCAL_MACHINE'
            },
        6: {
            'name': 'NameServer',
            'value': data,
            'path': 'SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces\{4fa65d49-0b51-4503-9248-53cec562af54}\4445D21303030205C65737F5637373',
            'type': _winreg.REG_SZ,
            'parent': 'HKEY_LOCAL_MACHINE'
            },
        7: {
            'name': 'ScopeAddress',
            'value': data,
            'path': 'SYSTEM\ControlSet001\Services\SharedAccess\Parameters',
            'type': _winreg.REG_SZ,
            'parent': 'HKEY_LOCAL_MACHINE'
            },
        8: {
            'name': 'ScopeAddressBackup',
            'value': data,
            'path': 'SYSTEM\ControlSet001\Services\SharedAccess\Parameters',
            'type': _winreg.REG_SZ,
            'parent': 'HKEY_LOCAL_MACHINE'
            },
        9: {
            'name': 'StandaloneDhcpAddress',
            'value': data,
            'path': 'SYSTEM\ControlSet001\Services\SharedAccess\Parameters',
            'type': _winreg.REG_SZ,
            'parent': 'HKEY_LOCAL_MACHINE'
            },
        10: {
            'name': 'ScopeAddress',
            'value': data,
            'path': 'SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters',
            'type': _winreg.REG_SZ,
            'parent': 'HKEY_LOCAL_MACHINE'
            },
        11: {
            'name': 'ScopeAddressBackup',
            'value': data,
            'path': 'SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters',
            'type': _winreg.REG_SZ,
            'parent': 'HKEY_LOCAL_MACHINE'
            },
        12: {
            'name': 'StandaloneDhcpAddress',
            'value': data,
            'path': 'SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters',
            'type': _winreg.REG_SZ,
            'parent': 'HKEY_LOCAL_MACHINE'
            },
        13: {
            'name': 'DhcpNameServer',
            'value': data,
            'path': 'SYSTEM\ControlSet001\Services\Tcpip\Parameters\Interfaces\{4fa65d49-0b51-4503-9248-53cec562af54}\25F455455425',
            'type': _winreg.REG_SZ,
            'parent': 'HKEY_LOCAL_MACHINE'
            },
        14: {
            'name': 'DhcpNameServer',
            'value': data,
            'path': 'SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces\{4fa65d49-0b51-4503-9248-53cec562af54}\25F455455425',
            'type': _winreg.REG_SZ,
            'parent': 'HKEY_LOCAL_MACHINE'
            },
    }

    return data_key

def setParameter1(data):
    data_key = {
        1: {
            'name': 'IPAddress',
            'value': data,
            'path': 'HKLM\SYSTEM\ControlSet001\Services\{76AC6BB9-4C7D-4EEE-A241-F483F94672B3}\Parameters\Tcpip',
            'parent': 'HKEY_LOCAL_MACHINE', 
            'type': 'REG_MULTI_SZ',
            },
        2: {
            'name': 'IPAddress',
            'value': data,
            'path': 'HKLM\SYSTEM\CurrentControlSet\Services\{76AC6BB9-4C7D-4EEE-A241-F483F94672B3}\Parameters\Tcpip',
            'parent': 'HKEY_LOCAL_MACHINE',
            'type': 'REG_MULTI_SZ',
            },
        3: {
            'name': 'NameServer',
            'value': data,
            'path': 'HKLM\SYSTEM\ControlSet001\Services\Tcpip\Parameters\Interfaces\{4fa65d49-0b51-4503-9248-53cec562af54}\25F4554554250223',
            'parent': 'HKEY_LOCAL_MACHINE',
            'type': 'REG_SZ',
            },
        4: {
            'name': 'NameServer',
            'value': data,
            'path': 'HKLM\SYSTEM\ControlSet001\Services\Tcpip\Parameters\Interfaces\{4fa65d49-0b51-4503-9248-53cec562af54}\4445D21303030205C65737F5637373',
            'parent': 'HKEY_LOCAL_MACHINE',
            'type': 'REG_SZ',
            },
        5: {
            'name': 'NameServer',
            'value': data,
            'path': 'HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces\{4fa65d49-0b51-4503-9248-53cec562af54}\25F4554554250223',
            'parent': 'HKEY_LOCAL_MACHINE',
            'type': 'REG_SZ',
            },
        6: {
            'name': 'NameServer',
            'value': data,
            'path': 'HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces\{4fa65d49-0b51-4503-9248-53cec562af54}\4445D21303030205C65737F5637373',
            'parent': 'HKEY_LOCAL_MACHINE',
            'type': 'REG_SZ',
            },
        7: {
            'name': 'ScopeAddress',
            'value': data,
            'path': 'HKLM\SYSTEM\ControlSet001\Services\SharedAccess\Parameters',
            'parent': 'HKEY_LOCAL_MACHINE',
            'type': 'REG_SZ',
            },
        8: {
            'name': 'ScopeAddressBackup',
            'value': data,
            'path': 'HKLM\SYSTEM\ControlSet001\Services\SharedAccess\Parameters',
            'parent': 'HKEY_LOCAL_MACHINE',
            'type': 'REG_SZ',
            },
        9: {
            'name': 'StandaloneDhcpAddress',
            'value': data,
            'path': 'HKLM\SYSTEM\ControlSet001\Services\SharedAccess\Parameters',
            'parent': 'HKEY_LOCAL_MACHINE',
            'type': 'REG_SZ',
            },
        10: {
            'name': 'ScopeAddress',
            'value': data,
            'path': 'HKLM\SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters',
            'parent': 'HKEY_LOCAL_MACHINE',
            'type': 'REG_SZ',
            },
        11: {
            'name': 'ScopeAddressBackup',
            'value': data,
            'path': 'HKLM\SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters',
            'parent': 'HKEY_LOCAL_MACHINE',
            'type': 'REG_SZ',
            },
        12: {
            'name': 'StandaloneDhcpAddress',
            'value': data,
            'path': 'HKLM\SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters',
            'parent': 'HKEY_LOCAL_MACHINE',
            'type': 'REG_SZ',
            },
        13: {
            'name': 'DhcpNameServer',
            'value': data,
            'path': 'HKLM\SYSTEM\ControlSet001\Services\Tcpip\Parameters\Interfaces\{4fa65d49-0b51-4503-9248-53cec562af54}\25F455455425',
            'parent': 'HKEY_LOCAL_MACHINE',
            'type': 'REG_SZ',
            },
        14: {
            'name': 'DhcpNameServer',
            'value': data,
            'path': 'HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces\{4fa65d49-0b51-4503-9248-53cec562af54}\25F455455425',
            'parent': 'HKEY_LOCAL_MACHINE',
            'type': 'REG_SZ',
            },
        15: {
            'name': 'DhcpNameServer',
            'value': data,
            'path': 'HKLM\SYSTEM\ControlSet001\Services\Tcpip\Parameters\Interfaces\{4fa65d49-0b51-4503-9248-53cec562af54}\4445D21303030205C65737F5637373',
            'parent': 'HKEY_LOCAL_MACHINE',
            'type': 'REG_SZ',
            },
        16: {
            'name': 'NameServer',
            'value': data,
            'path': 'HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces\{4fa65d49-0b51-4503-9248-53cec562af54}\25F455455425',
            'parent': 'HKEY_LOCAL_MACHINE',
            'type': 'REG_SZ',
            },
        17: {
            'name': 'NameServer',
            'value': data,
            'path': 'HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces\{4fa65d49-0b51-4503-9248-53cec562af54}\4445D21303030205C65737F5637373',
            'parent': 'HKEY_LOCAL_MACHINE',
            'type': 'REG_SZ',
            },
        18: {
            'name': 'ScopeAddress',
            'value': data,
            'path': 'HKLM\SYSTEM\ControlSet001\Services\SharedAccess\Parameters',
            'parent': 'HKEY_LOCAL_MACHINE',
            'type': 'REG_SZ',
            },
        19: {
            'name': 'ScopeAddressBackup',
            'value': data,
            'path': 'HKLM\SYSTEM\ControlSet001\Services\SharedAccess\Parameters',
            'parent': 'HKEY_LOCAL_MACHINE',
            'type': 'REG_SZ',
            },
        20: {
            'name': 'StandaloneDhcpAddress',
            'value': data,
            'path': 'HKLM\SYSTEM\ControlSet001\Services\SharedAccess\Parameters',
            'parent': 'HKEY_LOCAL_MACHINE',
            'type': 'REG_SZ',
            },
        21: {
            'name': 'ScopeAddress',
            'value': data,
            'path': 'HKLM\SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters',
            'parent': 'HKEY_LOCAL_MACHINE',
            'type': 'REG_SZ',
            },
        22: {
            'name': 'ScopeAddressBackup',
            'value': data,
            'path': 'HKLM\SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters',
            'parent': 'HKEY_LOCAL_MACHINE',
            'type': 'REG_SZ',
            },
        23: {
            'name': 'StandaloneDhcpAddress',
            'value': data,
            'path': 'HKLM\SYSTEM\CurrentControlSet\Services\SharedAccess\Parameters',
            'parent': 'HKEY_LOCAL_MACHINE',
            'type': 'REG_SZ',
            },
        24: {
            'name': 'DhcpNameServer',
            'value': data,
            'path': 'HKLM\SYSTEM\ControlSet001\Services\Tcpip\Parameters\Interfaces\{4fa65d49-0b51-4503-9248-53cec562af54}\25F455455425',
            'parent': 'HKEY_LOCAL_MACHINE',
            'type': 'REG_SZ',
            },
        25: {
            'name': 'IPAddress',
            'value': data,
            'path': 'HKLM\SYSTEM\ControlSet001\Services\{76AC6BB9-4C7D-4EEE-A241-F483F94672B3}\Parameters\Tcpip',
            'parent': 'HKEY_LOCAL_MACHINE',
            'type': 'REG_MULTI_SZ',
            },
        26: {
            'name': 'IPAddress',
            'value': data,
            'path': 'HKLM\SYSTEM\CurrentControlSet\Services\{76AC6BB9-4C7D-4EEE-A241-F483F94672B3}\Parameters\Tcpip',
            'parent': 'HKEY_LOCAL_MACHINE',
            'type': 'REG_MULTI_SZ',
            },
    }

    return data_key

if __name__ == '__main__':
    if len(sys.argv) == 3:
        parameter = setParameter1(sys.argv[1])
        if sys.argv[2] == 'fast':
            for i in parameter:
                name = parameter.get(i).get('name')
                keyval = parameter.get(i).get('path')
                reg_type = parameter.get(i).get('type')
                value = parameter.get(i).get('value')
                #if parent == 'HKEY_LOCAL_MACHINE':
                        #parent = 'HKLM'
                #elif parent == 'HKEY_CURRENT_USER':
                        #parent = 'HKCU'
                #elif parent == 'HKEY_CLASSES_ROOT':
                        #parent = 'HKCR'
                #elif parent == 'HKEY_CURRENT_CONFIG':
                        #parent = 'HKCC'
                #elif parent == 'HKEY_USERS':
                        #parent = 'HKU'
                #print "keyval =", keyval
                #print "name =", name
                #print "reg_type =", reg_type
                #print "value =", value
                os.system('REG ADD {0} /v {1} /t {2} /d {3} /f'.format(keyval, name, reg_type, value))
            sys.exit(0)
        elif len(sys.argv) == 2:
            parameter = setParameter(sys.argv[1])
            for i in parameter:
                name = parameter.get(i).get('name')
                parent = parameter.get(i).get('parent')
                keyval = parameter.get(i).get('path')
                reg_type = parameter.get(i).get('type')
                value = parameter.get(i).get('value')
                writereg(name, parent, keyval, reg_type, value)
    sys.exit(0)
