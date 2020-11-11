import os
import sys
from make_colors import make_colors
os.system("cls")
print("\n")

def cpuload():
	from win32com.client import GetObject
	wmi=GetObject('winmgmts:')
	cpu=wmi.InstancesOf('Win32_Processor')
	for x in cpu:
		print("\tLoadPercentage       = ", x.Properties_('LoadPercentage').Value , "%\n")

def meminfo(verbosity=None):
	import win32api
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

	data_TotalPageFile = make_colors("TotalPageFile        = %0.2f0 Mb" %(float(TotalPageFile) / mb), 'blue', 'yellow')
	data_AvailVirtual  = make_colors("AvailVirtual         = %0.2f0 Mb" %(float(AvailVirtual) / mb), 'white', 'cyan')
	data_TotalPhys     = make_colors("TotalPhys            = %0.2f0 Gb" %(float(TotalPhys) / gb), 'white', 'green')
	data_TotalVirtual  = make_colors("TotalVirtual         = %0.2f0 Mb" %(float(TotalVirtual) / mb), 'white', 'blue')
	data_UsedPhys       = make_colors("UsedPhys             = %0.2f0 Mb" %((float(TotalPhys) /mb2) - (float(AvailPhys) / mb2)), 'white', 'magenta')
	data_AvailPhys     = make_colors("AvailPhys            = %0.2f0 Mb" %(float(AvailPhys) / mb2), 'white', 'red')
	data_AvailPageFile = make_colors("AvailPageFile        = %0.2f0 Mb" %(float(AvailPageFile) / mb), 'blue', 'white', ['bold'])

	print("\t\t   Status Memory ")
	print("\t==================================== \n")
	print("\t" + data_TotalPhys, "\n")
	print("\t" + data_AvailPhys, "\n")
	print("\t" + data_UsedPhys, "\n")
	print("\t" + make_colors("Memory Load          = %d" %(MemoryLoad) + " %", 'red', 'yellow', ['bold']) + "\n")
	if MemoryFree < 10:
		print("\t" + make_colors("Memory Free          = %d" %(MemoryFree) + " %", 'white', 'red', ['bold', 'blink']) + "\n")
	else:
		print("\t" + make_colors("Memory Free          = %d" %(MemoryFree) + " %", 'white', 'red', ['bold']) + "\n")
	print("\t" + data_TotalPageFile, "\n")
	print("\t" + data_AvailVirtual, "\n")
	print("\t" + data_TotalVirtual, "\n")
	print("\t" + data_AvailPageFile, "\n")
	print("\t" + make_colors("AvailExtendedVirtual = %d Mb" %(AvailExtendedVirtual), 'white', 'magenta', ['bold']) + "\n")
	if verbosity:
		cpuload()

def usage():
	import argparse
	parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
	parser.add_argument('-v', '--verbosity', help='Show CPU load too', action='store_true')
	if len(sys.argv) == 1:
		meminfo()
	else:
		args = parser.parse_args()
		if sys.platform == 'win32':
			meminfo(args.verbosity)
		else:
			print("This support Windows Only")

usage()