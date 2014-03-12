import module002
import module003
import module004
import sys
import os

report = "ipMonitorRpt"
service = "ipMonitorSrv"
datagui = os.getenv("ProgramFiles") +"\\"  + r"SolarWinds\ipMonitor\ipm9config.exe"

try:
	if (sys.argv[1] == "start"):
		module003.start(service)
		module003.start(report)
	elif (sys.argv[1] == "stop"):
		module003.stop(service)
		module003.stop(report)
	elif (sys.argv[1] == "restart"):
		module003.restart(service)
		module003.restart(report)
	elif (sys.argv[1] == "status"):
		module004.status(service)
		module004.status(report)
	elif (sys.argv[1] == "help"):
		os.system("cls")
		module003.guide()
	elif (sys.argv[1] == "gui"):
		module002.main(datagui)
	elif (sys.argv[1] == "config"):
		module002.main(datagui)
	else:
		os.system("cls")
		module003.usage()
except IndexError, e:
	os.system("cls")
	module003.guide()