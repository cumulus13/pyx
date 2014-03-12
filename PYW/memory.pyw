import win32api
import os

os.system("cls")
print "\n\n"

def cpuload():
	from win32com.client import GetObject
	wmi=GetObject('winmgmts:')
	cpu=wmi.InstancesOf('Win32_Processor')
	for x in cpu:
		print "\tLoadPercentage       = ", x.Properties_('LoadPercentage').Value , "%\n"


data = win32api.GlobalMemoryStatusEx()
mb = float(1024 * 1024 * 10)
mb2 = float(1024 * 1024)
gb = float(1024 * 1024 * 1024)

#print data , "\n\n"

TotalPageFile = data['TotalPageFile']
AvailVirtual  = data['AvailVirtual'] 
MemoryLoad    = data['MemoryLoad']
MemoryFree    = 100 - MemoryLoad
TotalPhys     = data['TotalPhys']
AvailExtendedVirtual = data['AvailExtendedVirtual']
TotalVirtual  = data['TotalVirtual']
AvailPhys     = data['AvailPhys']
AvailPageFile = data['AvailPageFile']

data_TotalPageFile = "TotalPageFile        = %0.2f0 Mb" %(float(TotalPageFile) / mb)
data_AvailVirtual  = "AvailVirtual         = %0.2f0 Mb" %(float(AvailVirtual) / mb)
data_TotalPhys     = "TotalPhys            = %0.2f0 Gb" %(float(TotalPhys) / gb)
data_TotalVirtual  = "TotalVirtual         = %0.2f0 Mb" %(float(TotalVirtual) / mb)
data_UsedPhys       = "UsedPhys             = %0.2f0 Mb" %((float(TotalPhys) /mb2) - (float(AvailPhys) / mb2))
data_AvailPhys     = "AvailPhys            = %0.2f0 Mb" %(float(AvailPhys) / mb2)
data_AvailPageFile = "AvailPageFile        = %0.2f0 Mb" %(float(AvailPageFile) / mb)

print "\t\t   Status Memory \n"
print "\t----------------------------------- \n"
print "\t" + data_TotalPhys, "\n"
print "\t" + data_AvailPhys, "\n"
print "\t" + data_UsedPhys, "\n"
print "\t" + "Memory Load          = %d" %(MemoryLoad) + " %" + "\n"
print "\t" + "Memory Free          = %d" %(MemoryFree) + " %" + "\n"
print "\t" + data_TotalPageFile, "\n"
print "\t" + data_AvailVirtual, "\n"
print "\t" + data_TotalVirtual, "\n"
print "\t" + data_AvailPageFile, "\n"
print "\t" + "AvailExtendedVirtual = %d Mb" %(AvailExtendedVirtual) + "\n"

cpuload()

