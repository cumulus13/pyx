import module002a,os

data = ["cFosSpeeds"]
data2 = [os.getenv("ProgramFiles") +"\\"  + r"Topos\cFosSpeed\cfosspeed.exe"]

module002a.services2(data2, data)
