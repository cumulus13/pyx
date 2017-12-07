import module002a
# import os
# import sys
# args = []
# if os.path.isfile(sys.argv[1]):
#     file_argv = sys.argv[1]
#     print "file_argv =", file_argv
#     godir = os.path.dirname(file_argv)
#     if godir == "":
#         godir = os.getcwd()
#     os.chdir(godir)
#     del(sys.argv[1])
#     sys.argv.insert(1, os.path.basename(file_argv))
# else:
#     os.chdir("c:\\DOWNLOAD")
# print "sys.argv =", sys.argv
# print "cwd      =", os.getcwd()
# import subprocess
import os
os.environ.update({'HOME':'c:\DOWNLOAD'})
data = [r"c:\Apps\elinks-0.11.6\elinks.exe"]
# print data
# subprocess.Popen(data)
# data = [r"c:\Apps\elinks-0.11.6\elinks.exe"]
module002a.main(data)
