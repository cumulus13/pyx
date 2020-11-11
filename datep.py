from __future__ import print_function
import os
import sys
import calendar
import datetime
from make_colors import make_colors
PID = os.getpid()

class Datep(object):
	"""docstring for Datep"""
	def __init__(self):
		super(Datep, self).__init__()
		self.now = datetime.datetime.now()
		
	def get_this_day_numbers(self):
		pass

	def check_milli_seconds(self, milli_seconds_before, milli_seconds_after, format):
		if milli_seconds_before:
			format = format + ':%f'
			before_datetime + before_datetime + ':%s'%(str(milli_seconds_before))
		if milli_seconds_after:
			format = format + ':%f'
			after_datetime + after_datetime + ':%s'%(str(milli_seconds_after))

	def diff_datetime(self, before_datetime, after_datetime, format='%d-%m-%Y %H:%M:%S', milli_seconds_before=None, milli_seconds_after=None):
		if not format:
			format = '%d-%m-%Y %H:%M:%S'
		if isinstance(before_datetime, datetime.datetime) and isinstance(after_datetime, datetime.datetime):
			diff = after_datetime - before_datetime
			return True, diff

		elif isinstance(before_datetime, str) and isinstance(after_datetime, str):
			self.check_milli_seconds(milli_seconds_before, milli_seconds_after, format)
			if milli_seconds_before and not milli_seconds_after:
				return False, "NOT MATCH mili seconds"
			elif not milli_seconds_before and milli_seconds_after:
				return False, "NOT MATCH mili seconds"

			a = datetime.datetime.strptime(before_datetime, format)
			b = datetime.datetime.strptime(after_datetime, format)
			diff = b - a
			return True, diff

		elif isinstance(before_datetime, str) and isinstance(after_datetime, datetime.datetime):
			self.check_milli_seconds(milli_seconds_before, milli_seconds_after, format)
			after_datetime = datetime.datetime.strftime(after_datetime, format)
			if milli_seconds_before and not milli_seconds_after:
				return False, "NOT MATCH mili seconds"
			elif not milli_seconds_before and milli_seconds_after:
				return False, "NOT MATCH mili seconds"

			a = datetime.datetime.strptime(before_datetime, format)
			b = datetime.datetime.strptime(after_datetime, format)
			diff = b - a
			return True, diff
		elif isinstance(before_datetime, datetime.datetime) and isinstance(after_datetime, str):
			self.check_milli_seconds(milli_seconds_before, milli_seconds_after, format)
			before_datetime = datetime.datetime.strftime(before_datetime, format)
			if milli_seconds_before and not milli_seconds_after:
				return False, "NOT MATCH mili seconds"
			elif not milli_seconds_before and milli_seconds_after:
				return False, "NOT MATCH mili seconds"

			a = datetime.datetime.strptime(before_datetime, format)
			b = datetime.datetime.strptime(after_datetime, format)
			diff = b - a
			return True, diff
		elif isinstance(before_datetime, str) and not after_datetime:
			self.check_milli_seconds(milli_seconds_before, milli_seconds_after, format)
			num_days_december = calendar.monthrange(datetime.datetime.now().year, 12)[1]
			after_datetime = datetime.datetime(2018, 12, num_days_december)
			before_datetime = datetime.datetime.strftime(before_datetime, format)
			after_datetime = datetime.datetime.strftime(after_datetime, format)
			if milli_seconds_before and not milli_seconds_after:
				return False, "NOT MATCH mili seconds"
			elif not milli_seconds_before and milli_seconds_after:
				return False, "NOT MATCH mili seconds"

			a = datetime.datetime.strptime(before_datetime, format)
			b = datetime.datetime.strptime(after_datetime, format)
			diff = b - a
			return True, diff
		elif not before_datetime and isinstance(after_datetime, str):
			self.check_milli_seconds(milli_seconds_before, milli_seconds_after, format)
			before_datetime = datetime.datetime.now()
			before_datetime = datetime.datetime.strftime(before_datetime, format)
			after_datetime = datetime.datetime.strftime(after_datetime, format)
			if milli_seconds_before and not milli_seconds_after:
				return False, "NOT MATCH mili seconds"
			elif not milli_seconds_before and milli_seconds_after:
				return False, "NOT MATCH mili seconds"

			a = datetime.datetime.strptime(before_datetime, format)
			b = datetime.datetime.strptime(after_datetime, format)
			diff = b - a
			return True, diff
		elif not before_datetime and not after_datetime:
			self.check_milli_seconds(milli_seconds_before, milli_seconds_after, format)
			before_datetime = datetime.datetime.now()
			before_datetime = datetime.datetime.strftime(before_datetime, format)
			num_days_december = calendar.monthrange(datetime.datetime.now().year, 12)[1]
			after_datetime = datetime.datetime(2018, 12, num_days_december)
			after_datetime = datetime.datetime.strftime(after_datetime, format)
			if milli_seconds_before and not milli_seconds_after:
				return False, "NOT MATCH mili seconds"
			elif not milli_seconds_before and milli_seconds_after:
				return False, "NOT MATCH mili seconds"

			a = datetime.datetime.strptime(before_datetime, format)
			b = datetime.datetime.strptime(after_datetime, format)
			diff = b - a
			return True, diff

		return False, None

	def datetime_to_str(self, format, datetime):
		pass

	def str_to_datetime(self, format, datetime):
		pass

	def get_days(self, datetime, format):
		pass

	def print_now(self):
		sep = make_colors(" ", 'white', 'black')
		date_format = '%a [%d]. %B (%m) - %Y'
		now = datetime.datetime.now()
		print (make_colors("DATE", 'black', 'green') + sep + ":" + sep + make_colors(datetime.datetime.strftime(datetime.datetime.now(), date_format), 'lightgreen'))
		print (make_colors("TIME", 'black', 'lightcyan') + sep + ":" + sep + make_colors(datetime.datetime.strftime(datetime.datetime.now(), '%H:%M:%S, %f'), 'lightcyan'))
		days = self.diff_datetime(None, None)[1].days
		print (make_colors('DAYS', 'white', 'magenta') + sep + ":" + sep + make_colors("%s Days"%(days), 'lightmagenta'))

	def usage(self):
		pass

if __name__ == '__main__':
	c = Datep()
	# c.usage()
	c.print_now()
		
