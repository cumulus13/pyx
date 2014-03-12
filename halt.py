import pyttsx
import os
import sys

dtime = sys.argv[1]
engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.say('Attention !.Computer will be shutdown in ' + str(dtime) + " seconds")
engine.runAndWait()
os.system("shutdown -s -t " + str(dtime) + " -f")

