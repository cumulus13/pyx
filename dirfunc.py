import os
import sys

print "os.path.abspath                   = ", os.path.abspath(sys.argv[1])
print "os.path.basename                  = ", os.path.basename(sys.argv[1])
print "os.path.commonprefix              = ", os.path.commonprefix(sys.argv[1])
print "os.path.curdir                    = ", os.path.curdir
print "os.path.altsep                    = ", os.path.altsep
print "os.path.defpath                   = ", os.path.defpath
print "os.path.devnull                   = ", os.path.devnull
print "os.path.dirname                   = ", os.path.dirname(sys.argv[1])
print "os.path.expandvars                = ", os.path.expandvars(sys.argv[1])
#print "os.path.genericpath               = ", os.path.genericpath(sys.argv[1])
print "os.path.extsep                    = ", os.path.extsep
print "os.path.normcase                  = ", os.path.normcase(sys.argv[1])
print "os.path.normpath                  = ", os.path.normpath(sys.argv[1])
print "os.path.realpath                  = ", os.path.realpath(sys.argv[1])
print "os.path.relpath                   = ", os.path.relpath(sys.argv[1])
print "os.path.pardir                    = ", os.path.pardir
print "os.path.pathsep                   = ", os.path.pathsep
print "os.path.getsize(sys.argv[1])      = ", os.path.getsize(sys.argv[1])
print "os.path.normcase(sys.argv[1])     = ", os.path.normcase(sys.argv[1])
print "os.path.isabs(sys.argv[1])        = ", os.path.isabs(sys.argv[1])
print "os.path.splitdrive(sys.argv[1])   = ", os.path.splitdrive(sys.argv[1])
print "os.path.splitunc(sys.argv[1])     = ", os.path.splitunc(sys.argv[1])
#print "os.path.stat()                    = ", os.path.stat(sys.argv[1])
print "os.path.__all__                   = ", os.path.__all__