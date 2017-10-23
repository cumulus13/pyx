import os
import sys
import argparse

class list_tail(object):
	def __init__(self):
		super(list_tail, self)

	def limited(self, path):
		length 		= len(os.listdir(path))
		length_div 	= length/10


	def tail(self, path=None, sortby=None, recursive=None, verbose=None, limit=None):
		limit_dict = {1:'0-50', 2:'51-100', 3:'101-150', 4:'151-200', 
					  5:'201-250', 6:'251-300', 7:'301-350', 8:'351-400',
					  9:'401-450', 10:'451-500'}
		sort_dict = {'t':'time', 's':'size', 'n':'name', 'f':'file'}
		r_sort_dict = {'time':'t', 'size':'s', 'name':'n', 'file':'f'}
		sortby = sort_dict.get(str(sortby).lower())
		if sortby == 'time' or sortby == 't':
			if recursive:
				if verbose:
					print "list by time [recursive]"
				app = 'dir /o:-d '
			else:
				if verbose:
					print "list by time"
				app = 'dir /o:d '
		elif sortby == 'name' or sortby == 'n':
			if recursive:
				if verbose:
					print "list by name [recursive]"
				app = 'dir /o:-n '
			else:
				if verbose:
					print "list by name"
				app = 'dir /o:n '
		elif sortby == 'size' or sortby == 's':
			if recursive:
				if verbose:
					print "list by size [recursive]"
				app = 'dir /o:-s '
			else:
				if verbose:
					print "list by size"
				app = 'dir /o:s '
		elif sortby == 'file' or sortby == 'f':
			if verbose:
				print "list by file only"
			app = 'dir /a:a '
		else:
			if verbose:
				print "list by file only"
			app = 'dir /a:a '

		if path == None:
			path = os.getcwd()
		if sortby == None:
			sortby = 'f'
		if limit == None:
			limit = 1

		print "BBB"
		print "app						=", app
		print "app2						=", sort_dict.get(str(sortby).lower())
		print "sortby 						=", sortby
		print "path 						=", path
		print "limit 						=", limit
		print "limit_dict.get(int(limit)) 	=", limit_dict.get(int(limit))

		if len(sortby) == 1:
			print "AAA 01"
			os.system(app + '"' + path + '" | tail -n ' + limit_dict.get(int(limit)))
		elif len(sortby) > 1:
			print "AAA 02"
			try:
				os.system(app + path + ' | tail -n ' + limit_dict.get(int(limit)))
			except:
				if verbose:
					import traceback
					print traceback.format_exc()
				return None
		else:
			return None


	def usage(self):
		parser = argparse.ArgumentParser()
		parser.add_argument('-p', '--path', help='Path list to (optional), default current directory', action='store')
		parser.add_argument('-s', '--sort', help='Sort list by [t=time,n=name,size=s,default=fileonly]', action='store')
		parser.add_argument('-l', '--limit', help='Limit sorted by 50 item', default=1, action='store')
		parser.add_argument('-r', '--recursive', help='Sort recursive', action='store_true')
		parser.add_argument('-v', '--verbose', help='Show detail process', action='store_true')
		if len(sys.argv) == 1:
			parser.print_help()
			print "\n"
			self.tail()
		else:
			options = parser.parse_args()
			# print "options.limit =", options.limit
			# def tail(self, path=None, sortby=None, recursive=None, verbose=None, limit=None):
			self.tail(options.path, options.sort, options.recursive, options.verbose, options.limit)

if __name__ == '__main__':
	c = list_tail()
	c.usage()