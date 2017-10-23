#!/usr/bin/python
# -*- encoding: iso-8859-1 -*-

import syslogx
import sys
import os

if len(sys.argv) == 1:
	print "\n"
	print "\t Usage:",os.path.split(__file__)[1],"SeverityNumber FacilityNumber HOST PORT MSG"
else:
	syslogx.syslog(str(sys.argv[5]), int(sys.argv[1]), int(sys.argv[2]), str(sys.argv[3]), int(sys.argv[4]))
