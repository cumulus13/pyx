import module002a,os
import os

data = os.getenv("ProgramFiles") +"\\"  + r"LogMeIn Hamachi\hamachi-2-ui.exe"
service = "hamachi2svc"
module002a.main2(data,service)
os.system("taskkill /f /im hamachi-2.exe");

