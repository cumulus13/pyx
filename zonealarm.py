import module002a,os

#app1 = os.getenv("ProgramFiles") +"\\"  + r'zone labs\zonealarm\zlclient.exe'
data_app = [os.getenv("ProgramFiles") +"\\"  + r'zone labs\zonealarm\zlclient.exe']
svc_app = ['IswSvc','vsmon']
module002a.services2(data_app, svc_app)