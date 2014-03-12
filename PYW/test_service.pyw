import Cservice
import os
import sys

cek_status = Cservice.WService("apache2.2")
print cek_status.status()