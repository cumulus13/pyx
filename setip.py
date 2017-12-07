import os
import sys
import argparse

class setip(object):
	def __init__(self):
		super(setip, self)

	def setip(self, ip=None, netmask=None, gateway=None, device=None, dhcp=None, verbosity=None):
		if verbosity:
			print "IP      =", ip
			print "NETMASK =", netmask
			print "GATEWAY =", gateway
			print "DEVICE  =", device
		if ip:
			os.system('netsh interface ip set address %s static %s %s %s' %(device, str(ip), str(netmask), str(gateway)))
		elif dhcp:
			os.system('netsh interface ip set address %s DHCP')
		else:
			WindowsError('Please Definition your ip !')

	def usage(self):
		parser = argparse.ArgumentParser()
		parser.add_argument('IP', help='Ip address', action='store', type=str)				
		parser.add_argument('NETMASK', help='Netmask Address', action='store', type=str)
		parser.add_argument('GATEWAY', help='Gateway Ip', action='store', type=str)
		parser.add_argument('DEVICE', help='Device name', action='store', type=str)
		parser.add_argument('-d','--dhcp', help='Set Ip as Dhcp', action='store_true' )
		parser.add_argument('-v', '--verbosity', help='verbosity', action='count')
		if len(sys.argv) > 1:
			args = parser.parse_args()
			if args.IP:
				if args.dhcp:
					self.setip(dhcp=True)
				elif args.NETMASK:
					if args.GATEWAY:
						self.setip(args.IP, args.NETMASK, args.GATEWAY, args.DEVICE, args.verbosity)
		else:
			parser.print_help()

if __name__ == '__main__':
	c = setip()
	c.usage()
