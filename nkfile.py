#this script only create a blank file on Windows encode system support
#not tested on linux
#licface (licface@yahoo.com)

import sys
import os
import clipboard

__version__ = "1.0"
__filename__ = os.path.basename(sys.argv[0])
__usage__ = "\t use : " + __filename__ + " [name of file to create \n\n\t Example : " + __filename__ + " filetxt.py"

if len(sys.argv) > 1:
    f = open(sys.argv[1],"w")
    f.close()
    clipboard.copy(os.path.abspath(sys.argv[1]))
else:
    print "\n"
    print __usage__
