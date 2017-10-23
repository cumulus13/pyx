try:
    import pyttsx
except:
    pass
import os
import sys


engine = pyttsx.init()
rate = engine.getProperty('rate')

def play(svc,status):
    engine.setProperty('rate', rate-60) #95
    engine.say('Information. Service ' + str(svc) + ', is, ' + str(status))
    engine.runAndWait()

def play2(app,status):
    engine.setProperty('rate', rate-60) #95
    engine.say('Information. Program ' + str(app) + ', ' + str(status))
    engine.runAndWait()


if __name__ == '__name__':
    play2("Battery is ", "Low")