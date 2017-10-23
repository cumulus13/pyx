import module002a
import os

data = r"c:\Program Files\LogMeIn Hamachi\hamachi-2-ui.exe"
service = "hamachi2svc"
module002a.main2(data,service)
os.system("taskkill /f /im hamachi-2.exe");

