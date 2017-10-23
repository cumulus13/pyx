import module002a,os,sys,subprocess
if sys.argv[1] == "stop":
	subprocess.Popen(["c:\Windows\System32\sc.exe", "CONFIG","BstHdUpdaterSvc", "start=", "demand"])
	subprocess.Popen(["c:\Windows\System32\sc.exe", "STOP","BstHdUpdaterSvc"])
	subprocess.Popen(["c:\Windows\System32\sc.exe", "CONFIG","BstHdLogRotatorSvc", "start=", "demand"])
	subprocess.Popen(["c:\Windows\System32\sc.exe", "STOP","BstHdLogRotatorSvc"])
	subprocess.Popen(["c:\Windows\System32\sc.exe", "CONFIG","BstHdAndroidSvc", "start=", "demand"])
	subprocess.Popen(["c:\Windows\System32\sc.exe", "STOP","BstHdAndroidSvc"])
	subprocess.Popen(["c:\exe\px.exe", "-k", "HD-Agent.exe"])
else:
	data = ['C:\\Program Files\\BlueStacks\\HD-StartLauncher.exe']
	module002a.main(data)