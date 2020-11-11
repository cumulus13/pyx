#!c:/SDK/Anaconda2/python.exe
import os
import sys
from debug import debug
import re
import argparse
from make_colors import make_colors
COUNT_ON_START = False
COUNT_ON_END = False

class bulkrename(object):
	def __init__(self):
		super(bulkrename, self)

	def check_extentions(self, data_list, extentions, path):
		list_dirs = []
		for i in data_list:
			for e in extentions:
				if i.split('\n')[0].endswith(e):
					# list_dirs.append(os.path.join(os.path.abspath(path), i.split('\n')[0]))
					list_dirs.append(i.split('\n')[0])
		return list_dirs

	def check_start_with(self, data_list, start_with, path):
		debug(start_with=start_with)
		list_dirs = []
		for i in data_list:
			for e in start_with:
				if i.split('\n')[0].startswith(e):
					# list_dirs.append(os.path.join(os.path.abspath(path), i.split('\n')[0]))
					list_dirs.append(i.split('\n')[0])
		return list_dirs

	def make_list(self, path, pattern, newname='', len_count_number_string=2, sort_by='time', overwrite=False, extentions=None, start_with=None, test=False, exceptions=[]):
		'''Make list based on pattern
		
	Arguments:
		path {list} -- Full path directory contain file to renaming
		pattern {list} -- list code
		newname {string} -- new name replacement based on pattern
		                    example: "[N] [S] [C].mkv" this can be "NewName 01.mkv"
		sort_by {string} -- time|name
	
	pattern:
		N[n] = Name or Name with n new name
		C[N][n][s|e] = Number or Count with N start then raise up with n step constant 
		               and s = start position or e = end position of name of file
		E[n] = [New] Extention with n Extention
		S[n] = Seprator with n
		A[n] = Additional String with n
	
	count:
		C[n] = C with step n contant
		example:
			1[1] = C then raise up with 1 step = 2
			1[2] = C then raise up with 2 step = 3

	example running:

	>> ls
	Prison Break - Season 1 Episode 001 - Pilot.mkv
	Prison Break - Season 1 Episode 001 - Pilot.srt
	Prison Break - Season 1 Episode 002 - Allen.mkv
	Prison Break - Season 1 Episode 002 - Allen.srt
	Prison Break - Season 1 Episode 003 - Cell Test.mkv
	Prison Break - Season 1 Episode 003 - Cell Test.srt
	Prison Break - Season 1 Episode 004 - Cute Poison.mkv
	Prison Break - Season 1 Episode 004 - Cute Poison.srt
	Prison Break - Season 1 Episode 005 - English, Fitz Or Percy.mkv
	Prison Break - Season 1 Episode 005 - English, Fitz Or Percy.srt
	Prison Break - Season 1 Episode 006 - Riots, Drills And The Devil - Part 1.mkv
	Prison Break - Season 1 Episode 006 - Riots, Drills And The Devil - Part 1.srt
	Prison Break - Season 1 Episode 007 - Riots, Drills And The Devil - Part 2.mkv
	Prison Break - Season 1 Episode 007 - Riots, Drills And The Devil - Part 2.srt
	Prison Break - Season 1 Episode 008 - The Old Head.mkv
	Prison Break - Season 1 Episode 008 - The Old Head.srt
	Prison Break - Season 1 Episode 009 - Tweener.mkv

	>> bn -n "Prison Break" -N "[N] S01E[C]" -fe .mkv -x name
	01. Prison Break - Season 1 Episode 001 - Pilot.mkv --> Prison Break S01E01.mkv
	02. Prison Break - Season 1 Episode 002 - Allen.mkv --> Prison Break S01E02.mkv
	03. Prison Break - Season 1 Episode 003 - Cell Test.mkv --> Prison Break S01E03.mkv
	04. Prison Break - Season 1 Episode 004 - Cute Poison.mkv --> Prison Break S01E04.mkv
	05. Prison Break - Season 1 Episode 005 - English, Fitz Or Percy.mkv --> Prison Break S01E05.mkv
	06. Prison Break - Season 1 Episode 006 - Riots, Drills And The Devil - Part 1.mkv --> Prison Break S01E06.mkv
	07. Prison Break - Season 1 Episode 007 - Riots, Drills And The Devil - Part 2.mkv --> Prison Break S01E07.mkv
	08. Prison Break - Season 1 Episode 008 - The Old Head.mkv --> Prison Break S01E08.mkv
	09. Prison Break - Season 1 Episode 009 - Tweener.mkv --> Prison Break S01E09.mkv
	Are you ready to rename [y/n]: y
	RENAME: Prison Break - Season 1 Episode 001 - Pilot.mkv ==> Prison Break S01E01.mkv
	RENAME: Prison Break - Season 1 Episode 002 - Allen.mkv ==> Prison Break S01E02.mkv
	RENAME: Prison Break - Season 1 Episode 003 - Cell Test.mkv ==> Prison Break S01E03.mkv
	RENAME: Prison Break - Season 1 Episode 004 - Cute Poison.mkv ==> Prison Break S01E04.mkv
	RENAME: Prison Break - Season 1 Episode 005 - English, Fitz Or Percy.mkv ==> Prison Break S01E05.mkv
	RENAME: Prison Break - Season 1 Episode 006 - Riots, Drills And The Devil - Part 1.mkv ==> Prison Break S01E06.mkv
	RENAME: Prison Break - Season 1 Episode 007 - Riots, Drills And The Devil - Part 2.mkv ==> Prison Break S01E07.mkv
	RENAME: Prison Break - Season 1 Episode 008 - The Old Head.mkv ==> Prison Break S01E08.mkv
	RENAME: Prison Break - Season 1 Episode 009 - Tweener.mkv ==> Prison Break S01E09.mkv
		'''
		global COUNT_ON_START
		global COUNT_ON_END
		# print "COUNT_ON_START 1 =", COUNT_ON_START
		# print "COUNT_ON_END   1 =", COUNT_ON_END
		debug(path=path)
		debug(pattern=pattern)
		debug(newname=newname)
		new_name = ''
		new_extention = ''
		count = ''
		count_step = ''
		count_on_start = COUNT_ON_START
		count_on_end = COUNT_ON_END
		separator = ''
		additional = ''
		bulk_list = []
		list_dirs = []
		if sort_by == 'time':
			list_dirs_temp = os.popen("dir /od /b \"%s\""%(path)).readlines()
		elif sort_by == 'name':
			list_dirs_temp = os.popen("dir /on /b \"%s\""%(path)).readlines()
		else:
			list_dirs_temp = os.popen("dir /b \"%s\""%(path)).readlines()
		debug(list_dirs_temp=list_dirs_temp)
		debug(os_path_abspath=os.path.abspath(path))
		debug(extentions=extentions)
		if extentions:
			list_dirs_temp = self.check_extentions(list_dirs_temp, extentions, path)
			debug(list_dirs_temp_extentions = list_dirs_temp)
		if start_with:
			list_dirs_temp = self.check_start_with(list_dirs_temp, start_with, path)
			debug(list_dirs_temp_start_with = list_dirs_temp)
		# if not extentions and not start_with:
		if exceptions:
			for i in exceptions:
				for j in list_dirs_temp:
					if i in j:
						list_dirs_temp.remove(list_dirs_temp[list_dirs_temp.index(j)])
		for i in list_dirs_temp:
			# if extentions:
			# 	for e in extentions:
			# 		if i.split('\n')[0].endswith(e):
			# 			list_dirs.append(os.path.join(os.path.abspath(path), i.split('\n')[0]))
			# if start_with:
			# 	for e in start_with:
			# 		if i.split('\n')[0].startswith(e):
			# 			list_dirs.append(os.path.join(os.path.abspath(path), i.split('\n')[0]))
			# else:
			list_dirs.append(os.path.join(os.path.abspath(path), i.split('\n')[0]))
		# else:
		# 	list_dirs = list_dirs_temp
		debug(list_dirs=list_dirs)
		for i in pattern:
			if i[0] == 'N':
				data_name = re.split("\[|\]", i)
				new_name = data_name[1]
				debug(new_name=new_name)
			elif i[0] == 'C':
				data_count = re.split("\[|\]", i)
				count = int(data_count[1])
				count_step = int(data_count[3])
				if len(data_count) > 5:
					if data_count[5] == 's':
						count_on_start = True
						COUNT_ON_START = True
					elif data_count[5] == 'e':
						count_on_end = True
						COUNT_ON_END = True
				debug(count=count)
				debug(count_step=count_step)
			elif i[0] == 'E':
				data_ext = re.split("\[|\]", i)
				new_extention = data_ext[1]
				debug(new_extention=new_extention)
			elif i[0] == 'S':
				data_sep = re.split("\[|\]", i)
				separator = data_sep[1]
				if separator == 'n':
					separator = ' '
				debug(separator=separator)
			elif i[0] == 'A':
				data_add = re.split("\[|\]", i)
				additional = data_add[1]
				if ";" in additional:
					additional = str(additional).strip().split(";")
				debug(additional=additional)
			# print "new_name 0 =", new_name
			# print "new_extention 0 =", new_extention

		if isinstance(additional, list):
			if separator:
				separator.join(additional)
			else:
				" ".join(additional)

		for x in list_dirs:
			if newname:
				newname_split = str(newname).split(' ')
				debug(newname_split=newname_split)
				if len_count_number_string == 2:
					if len(str(count)) == 1:
						count = "0" + str(count)
				for i in newname_split:
					if i == '[N]':
						index_N = newname_split.index(i)
						newname_split.pop(index_N)
						newname_split.insert(index_N, new_name)
					# elif i == 'S':
					# 	index_S = newname_split.index(i)
					# 	newname_split.pop(index_S)
					# 	newname_split.insert(index_S, separator)
					elif '[C]' in i:
						index_C = newname_split.index(i)
						newname_pre = newname_split[index_C]
						newname_split.pop(index_C)
						newname_insert = newname_pre.replace('[C]', str(count))
						newname_split.insert(index_C, newname_insert)
						count = int(count)
					elif i[0] == 'E':
						newname_split = os.path.splitext(newname_split)
						newname_split = newname_split[0] + str(new_extention)
				debug(newname_split=newname_split)
				EXT = os.path.splitext(x)
				if len(EXT) == 2:
					EXT = EXT[1]
				else:
					EXT = ''	
				if separator:
					# print "separator =", [separator]
					newname_format = separator.join(newname_split)
				else:
					newname_format = " ".join(newname_split)
				newname_format += EXT
				bulk_list.append({'old':os.path.basename(x), 'new': newname_format})
			else:
				# print "new_name 1 =", new_name
				# print "new_extention =", new_extention
				# print "x =",x
				if not new_name:
					new_name_format = os.path.splitext(os.path.basename(x))[0]
					# print "new_name_format 1 =", new_name_format
				else:
					new_name_format = new_name
					# print "new_name_format 2 =", new_name_format
				if not new_extention:
					new_extention_format = os.path.splitext(x)[1]
					# print "new_extention_format 1 =", new_extention_format
				else:
					new_extention_format = new_extention
					# print "new_extention_format 2 =", new_extention_format
				# print "count          2 =", count
				# print "count_on_start 2 =", count_on_start
				# print "count_on_end   2 =", count_on_end
				if new_extention:
					if not new_extention[0] == ".":
						new_extention = "." + new_extention
						new_extention_format = new_extention
				if not additional:
					separator1 = ''
				else:
					separator1 = separator
				if count:
					if len_count_number_string == 2:
						if len(str(count)) == 1:
							count = "0" + str(count)
					elif len_count_number_string == 3:
						if len(str(count)) == 1:
							count = "00" + str(count)
						elif len(str(count)) == 2:
							count = "0" + str(count)

				if count and count_on_start:
					newname_format = str(count).strip() + separator + new_name_format + separator1 + str(additional).strip() + str(new_extention_format).strip() 
					count = int(count)
				elif count and count_on_end:
					newname_format =  new_name_format + separator1 + str(additional).strip() + separator + str(count).strip() + str(new_extention_format).strip()
					count = int(count)
				else:
					newname_format = new_name_format + separator1 + str(additional).strip() + str(new_extention_format).strip()
				bulk_list.append({'old':os.path.basename(x), 'new': newname_format}) 
			count = int(count) + count_step

		# print "BULK LIST =", bulk_list
		n = 1
		for i in bulk_list:
			if len_count_number_string == 2:
				if len(str(n)) == 1:
					n = "0" + str(n)
				elif len_count_number_string == 3:
					if len(str(n)) == 1:
						n = "00" + str(n)
					elif len(str(n)) == 2:
						n = "0" + str(n)
			print str(n) + ". " + i.get('old') + ' --> ' + i.get('new')
			n = int(n)
			n +=1
		q_rename = raw_input('Are you ready to rename [y/n]: ')
		only_rename_list = []
		if len(str(q_rename).split(" ")) > 1:
			q_rename, only_rename = str(q_rename).split(" ")
			only_rename_list = only_rename.split(',')
		if 'y' in q_rename or 'Y' in q_rename or 'yes' in q_rename or 'Yes' in q_rename or 'YES' in q_rename:
			if only_rename_list:
				bulk_list_only = []
				for i in only_rename_list:
					bulk_list_only.append(bulk_list[int(i)-1])
				bulk_list = bulk_list_only
			for i in bulk_list:
				self.rename(i.get('old'), i.get('new'), path, overwrite, test)

	def rename(self, old, new, path, overwrite=False, test=False):
		overwrite_print = ''
		if overwrite:
			overwrite_print = make_colors("[OVERWRITE]", 'white' ,'yellow')
		if test:
			overwrite_print = make_colors("[TEST]", 'white', 'magenta')
		this_path = os.getcwd()
		os.chdir(path)
		if overwrite:
			if os.path.isfile(new):
				os.remove(new)
		print make_colors('RENAME%s:'%(overwrite_print), 'white', "lightred") + make_colors(' ', 'black', 'black') + make_colors(old, 'lightgreen') + make_colors(' ', 'black', 'black') + make_colors('==>', "lightred") + make_colors(' ', 'black', 'black') + make_colors(new, 'lightblue')
		if not test:
			os.rename(old, new)
			# pass

	def usage(self):
		global COUNT_ON_START
		global COUNT_ON_END
		parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
		parser.add_argument('-p', '--path', action='store', help='Full Path containt file to rename, default this directory for spesific Extention, you can use star character, example: c:\\data\\file*.mkv', default=os.getcwd())
		parser.add_argument('-N', '--new', action='store', help='New Name pattern given')
		parser.add_argument('-n', '--new-name', action='store', help='New Name given')
		parser.add_argument('-c', '--count', action='store', help='Add Count number, input is start count number, default=1', default=1)
		parser.add_argument('-t', '--step', action='store', help='Step count raise up number, default=1', default=1)
		parser.add_argument('-cs', '--count-on-start', action='store_true', help='Add count on start of new name')
		parser.add_argument('-ce', '--count-on-end', action='store_true', help='Add count on end of new name')
		parser.add_argument('-s', '--separator', action='store', help='Replace all separator wtih this, default is space', default='n')
		parser.add_argument('-e', '--extention', action='store', help='Replace all extention with this')
		parser.add_argument('-a', '--additional', action='store', help='Add Additional string to new name')
		parser.add_argument('-x', '--sort-by', action='store', help='Sort list by time|name, default: time', default='time')
		parser.add_argument('-o', '--overwrite', action='store_true', help='Overwrite Existing File')
		parser.add_argument('-fe', '--file-extentions', action='store', help='Only rename file with this extention', nargs='*')
		parser.add_argument('-fs', '--file-start-with', action='store', help='Only rename file start (prefix) with this name', nargs='*')
		parser.add_argument('-E', '--exceptions', action='store', help='Exception name', nargs='*')
		parser.add_argument('-T', '--test', action='store_true', help='Test Output, no actualy rename it !')
		parser.add_argument('-u', '--usage', action='store_true', help='Show Usage documetations with example')
		if len(sys.argv) == 1:
			parser.print_help()
			print "\n"
			print self.make_list.__doc__
		else:
			args = parser.parse_args()
			COUNT_ON_START = args.count_on_start
			COUNT_ON_END = args.count_on_end
			# print "COUNT_ON_START =", COUNT_ON_START
			# print "COUNT_ON_END   =", COUNT_ON_END
			pattern = []
			if args.usage:
				parser.print_help()
				print self.make_list.__doc__
				sys.exit(0)
			if args.new_name:
				pattern.append('N[%s]'%(args.new_name))
			if args.count:
				if args.count_on_start:
					pattern.append('C[%s][%s][%s]'%(args.count, args.step, args.count_on_start))
				elif args.count_on_end:
					pattern.append('C[%s][%s][%s]'%(args.count, args.step, args.count_on_end))
				else:
					pattern.append('C[%s][%s]'%(args.count, args.step))
			if args.separator:
				pattern.append('S[%s]'%(args.separator))
			if args.extention:
				if not args.extention[0] == '.':
					extention = "." + args.extention
				else:
					extention = args.extention
				pattern.append('E[%s]'%(extention))
			if args.additional:
				pattern.append('A[%s]'%(additional))
			# make_list(self, path, pattern, newname='', len_count_number_string=2, sort_by='time', overwrite=False):
			self.make_list(args.path, pattern, args.new, sort_by=args.sort_by, overwrite=args.overwrite, extentions=args.file_extentions, start_with=args.file_start_with, test=args.test, exceptions=args.exceptions)

if __name__ == '__main__':
	c = bulkrename()
	# N[n] = Name or Name with n new name
	# C[N][n][s|e] = Number or Count with N start then raise up with n step constant 
	# 			   and s = start position or e = end position of name of file
	# E[n] = [New] Extention with n Extention
	# S[n] = Seprator with n
	# A[n] = Additional String with n	
	# path = sys.argv[1]
	# pattern = ['N[movietv]', 'C[1][1]', "S[n]"]
	# new_name = "[N] S01E[C]"
	# c.make_list(path, pattern, new_name)
	c.usage()








