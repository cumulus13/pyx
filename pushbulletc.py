#!c:/SDK/Anaconda2/python.exe

from __future__ import print_function
import sys, os
import argparse
import win32gui
import win32con
from configset import configset
import re
from make_colors import make_colors
import time

config = configset(os.path.join(os.path.dirname(__file__), 'pushbulletc.ini'))
api = "o.HbAh6uKbn8iBfQXbbJ4ZWauOlHhRuDNf"
note = ""
title = ""

PROJECT_PATH = r"D:\PROJECTS2"
sys.path.insert(0, PROJECT_PATH)
from dcmd import dcmd
cmd = dcmd.dcmd()

def send(title, note):
	from pushbullet import Pushbullet
	pb = Pushbullet(api)
	if isinstance(note, list):
		note = " ".join(note)
	return pb.push_note(title, note)

def search(close_all=False, verbosity = False, FOUNDS = [], q = None, delay = None):
	excp = config.read_config('excp', 'handles')
	if excp:
		excp = re.split(",| |\n", excp)
		excp = filter(None, excp)
	# print("excp =", excp)
	
	all_filter, all_list_hide, all_list_hide_filter, all_pids = cmd.getListWindows(filter = ['pushbullet_client'], print_list = False)
	if not FOUNDS:
		if all_filter:
			for i in all_filter:
				if ".exe" in i[0].lower():
					if str(i[-1]) not  in excp:
						FOUNDS.append(i)
		else:
			print(make_colors("No pushbullet_client FOUND !", 'lw', 'lr', ['blink']))
			sys.exit()
	if FOUNDS:
		n = 1
		for i in FOUNDS:
			number = str(n)
			if len(number) == 1:
				number = "0" + str(n)
			if not close_all:
				print(make_colors(number, 'lc') + ". " + make_colors(i[0], 'lr', 'lw') + " " + make_colors("PID:", 'lw', 'bl') + " " + make_colors(str(i[2]), 'b', 'ly') + " " + make_colors("HANDLE:", 'lw', 'bl') + " " + make_colors(str(i[-1]), 'lr', 'lw') + " " + make_colors("PARENT:", 'lw', 'bl') + " " + make_colors(str(win32gui.GetParent(i[-1])), 'b', 'lg'))
				n += 1
			else:
				if delay and str(delay).isdigit():
					time.sleep(int(delay))
				win32gui.PostMessage(i[-1], win32con.WM_CLOSE, 0, 0)
				
		if not close_all:
			q = raw_input(make_colors("Select number to close [n | n1-nx | n1,n2,nx | n1 n2 nx]", 'b', 'lg') + make_colors("[a = close all", 'b', 'ly') + ", " + make_colors("[q]uit | e[x]it = exit", 'lw', 'lr') + " : ")
				
			if q:
				q = str(q).strip()
				
				if q == 'x' or q == 'q' or q == 'exit' or q == 'quit':
					sys.exit()
				if str(q).isdigit() and int(q) <= len(FOUNDS):
					if verbosity:
						print(make_colors("CLOSE", 'lw', 'lr') + ": " + make_colors(FOUNDS[int(q) - 1][-1], 'lr', 'lw') + " " + make_colors("PID:", 'lw', 'bl') + " " + make_colors(str(FOUNDS[int(q) - 1][2]), 'b', 'ly') + " " + make_colors("PARENT:", 'lw', 'bl') + " " + make_colors(str(win32gui.GetParent(FOUNDS[int(q) - 1][-1])), 'b', 'lg'))
					if delay and str(delay).isdigit():
						time.sleep(int(delay))					
					win32gui.PostMessage(FOUNDS[int(q) - 1][-1], win32con.WM_CLOSE, 0, 0)
				elif "," in q or " " in q:
					q = re.split(",| ", q)
					q = filter(None, q)
					for x in q:
						if "-" in x:
							search(close_all, verbosity, FOUNDS, x)
						else:
							if x <= len(FOUNDS):
								if verbosity:
									print(make_colors("CLOSE", 'lw', 'lr') + ": " + make_colors(FOUNDS[int(x) - 1][-1], 'lr', 'lw') + " " + make_colors("PID:", 'lw', 'bl') + " " + make_colors(str(FOUNDS[int(x) - 1][2]), 'b', 'ly') + " " + make_colors("PARENT:", 'lw', 'bl') + " " + make_colors(str(win32gui.GetParent(FOUNDS[int(x) - 1][-1])), 'b', 'lg'))
								if delay and str(delay).isdigit():
									time.sleep(int(delay))								
								win32gui.PostMessage(FOUNDS[int(x) - 1][-1], win32con.WM_CLOSE, 0, 0)							
							
				elif "-" in q:
					fr, to = filter(None, re.split("-", q))
					x = range(int(fr), int(to) + 1)
					for i in x:
						if i <= len(FOUNDS):
							if verbosity:
								print(make_colors("CLOSE", 'lw', 'lr') + ": " + make_colors(FOUNDS[int(i) - 1][-1], 'lr', 'lw') + " " + make_colors("PID:", 'lw', 'bl') + " " + make_colors(str(FOUNDS[int(i) - 1][2]), 'b', 'ly') + " " + make_colors("PARENT:", 'lw', 'bl') + " " + make_colors(str(win32gui.GetParent(FOUNDS[int(i) - 1][-1])), 'b', 'lg'))
							if delay and str(delay).isdigit():
								time.sleep(int(delay))							
							win32gui.PostMessage(FOUNDS[int(i) - 1][-1], win32con.WM_CLOSE, 0, 0)
				elif q == 'a':
					for i in FOUNDS:
						if verbosity:
							print(make_colors("CLOSE", 'lw', 'lr') + ": " + make_colors(i[-1], 'lr', 'lw') + " " + make_colors("PID:", 'lw', 'bl') + " " + make_colors(str(i[2]), 'b', 'ly') + " " + make_colors("PARENT:", 'lw', 'bl') + " " + make_colors(str(win32gui.GetParent(i[-1])), 'b', 'lg'))
						if delay and str(delay).isdigit():
							time.sleep(int(delay))						
						win32gui.PostMessage(i[-1], win32con.WM_CLOSE, 0, 0)					
				else:
					print(make_colors("Invalid Input number !", 'lw', 'lr', ['blink']))
		else:
			for i in FOUNDS:
				if verbosity:
					print(make_colors("CLOSE", 'lw', 'lr') + ": " + make_colors(i[-1], 'lr', 'lw') + " " + make_colors("PID:", 'lw', 'bl') + " " + make_colors(str(i[2]), 'b', 'ly') + " " + make_colors("PARENT:", 'lw', 'bl') + " " + make_colors(str(win32gui.GetParent(i[-1])), 'b', 'lg'))
				if delay and str(delay).isdigit():
					time.sleep(int(delay))				
				win32gui.PostMessage(i[-1], win32con.WM_CLOSE, 0, 0)
					
	else:
		print(make_colors('No "pushbullet_client" FOUND !', 'lw', 'lr', ['blink']))
		sys.exit()
		
def add_excpt(excp = []):
	if excp:
		excp = ",".join(excp)
		print(make_colors("Add", 'lw', 'lr') + " " + make_colors(excp, 'lw', 'bl'))
		config.write_config('excp', 'handles', excp)
		
def add_excpt_this():
	all_filter, all_list_hide, all_list_hide_filter, all_pids = cmd.getListWindows(filter = ['pushbullet_client'], print_list = False)
	all_handle = []
	if all_filter:
		for i in all_filter:
			all_handle.append(i[-1])
	if all_handle:
		print(make_colors("Add", 'lw', 'lr') + " " + make_colors(",".join(all_handle), 'lw', 'bl'))
		config.write("excp", "handles", ",".join(all_handle))
	
		
def usage():
	import argparse
	parser = argparse.ArgumentParser(formatter_class = argparse.RawTextHelpFormatter)
	parser.add_argument('-a', '--add-excp', help = 'Add Exception', action = 'store', nargs = '*')
	parser.add_argument('-an', '--add-excp-now', help = 'Add Exception for this process exit only', action = 'store_true')
	parser.add_argument('-c', '--close-all', help = 'Close all', action = 'store_true')
	parser.add_argument('-v', '--verbosity', help = 'Show print list', action = 'store_true')
	parser.add_argument('-w', '--wait', help = 'Wait/delay before close', action = 'store', type = int)
	
	if len(sys.argv) == 1:
		print(make_colors('use "-h" for Command HELP', 'lr', 'lw'))
		search()
	elif len(sys.argv) == 2 and sys.argv[1] == 'c':
		search(True)
	else:
		args = parser.parse_args()
		if args.add_excp:
			add_excpt(args.add_excp)
		elif args.add_excp_now:
			add_excpt_this()
		search(args.close_all, args.verbosity, delay = args.wait)
		
if __name__ == '__main__':
	usage()
