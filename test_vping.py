import vping
import sys

a = vping.vping('192.168.1.2', 120, 4)
print "A =", a