import module002a,os

data = os.getenv("ProgramFiles") +"\\"  + r"DU Meter\DUMeter.exe"
service = "DUMeterSvc"

module002a.main2(data,service)