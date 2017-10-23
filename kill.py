import os
import sys
import argparse
import platform

if platform.uname()[0] == 'Linux':
	APP_KILL = 'killall -9'
	APP_KILL2 = 'killall -9'
elif platform.uname()[0] == 'Windows':
	APP_KILL = 'taskkill /f /im'
	APP_KILL2 = 'px -k '

class kill(object):
	def __init__(self):
		super(kill, self)

	def kill(self, process):
		os.popen(APP_KILL + ' %s' %(process))

	def multikill(self, process):
		if isinstance(process, list):
			for i in process:
				self.kill(self.windowsprocesscheck(i))

	def killbypid(self, pid):
		try:
			os.kill(pid, pid)
			os.popen(APP_KILL2 + ' %s' %(pid))
		except:
			pass

	def multikillbypid(self, pid):
		if isinstance(pid, list):
			for i in pid:
				self.killbypid(i)		

	def windowsprocesscheck(self, process):
		p = os.path.splitext(process)
		if p[1] == '':
			return process + ".exe"
		return process

	def usage(self):
		parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
		parser.add_argument('-p', '--pid', help='Kill By PID', nargs='*', action='store')
		parser.add_argument('PROCESS', help='Process to Kill', nargs='*', action='store')
		if len(sys.argv) == 1:
			parser.print_help()
		else:
			args = parser.parse_args()
			if args.pid:
				self.multikillbypid(args.pid)
			else:
				self.multikill(args.PROCESS)

if __name__ == '__main__':
	c = kill()
	c.usage()
