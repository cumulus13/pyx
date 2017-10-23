import module002a,os
data = os.getenv("ProgramFiles") +"\\"  + r"BWMeter\BWMeter.exe"
service = "BWMeterConSvc"
module002a.main2(data,service)