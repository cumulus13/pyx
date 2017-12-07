#!/usr/bin/python
import math
import os
import sys

def convertSize(size):
  size_name = ("KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
  i = int(math.floor(math.log(size,1024)))
  p = math.pow(1024,i)
  s = round(size/p,2)
  if (s > 0):
    return '%s %s' % (s,size_name[i])
  else:
    return '0B'

def sizeof_fmt(num, suffix='B'):
  for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
      if abs(num) < 1024.0:
          return "%3.1f%s%s" % (num, unit, suffix)
      num /= 1024.0
  return "%.1f%s%s" % (num, 'Yi', suffix)

from math import log
unit_list = zip(['bytes', 'kB', 'MB', 'GB', 'TB', 'PB'], [0, 0, 1, 2, 2, 2])
def sizeof_fmt1(num):
    """Human friendly file size"""
    if num > 1:
        exponent = min(int(log(num, 1024)), len(unit_list) - 1)
        quotient = float(num) / 1024**exponent
        unit, num_decimals = unit_list[exponent]
        format_string = '{:.%sf} {}' % (num_decimals)
        return format_string.format(quotient, unit)
    if num == 0:
      return '0 bytes'
    if num == 1:
      return '1 byte'

from math import log as log2

_suffixes = ['bytes', 'KiB', 'MiB', 'GiB', 'TiB', 'EiB', 'ZiB']

def file_size(size):
   # determine binary order in steps of size 10
   # (coerce to int, // still returns a float)
  order = int(log2(size) / 10) if size else 0
   # format file size
   # (.4g results in rounded numbers for exact matches and max 3 decimals,
   # should never resort to exponent values)
  return '{:.4g} {}'.format(size / (1 << (order * 10)), _suffixes[order])

def human_size(size_bytes):
  """
    format a size in bytes into a 'human' file size, e.g. bytes, KB, MB, GB, TB, PB
    Note that bytes/KB will be reported in whole numbers but MB and above will have greater precision
    e.g. 1 byte, 43 bytes, 443 KB, 4.3 MB, 4.43 GB, etc
  """
  if size_bytes == 1:
     # because I really hate unnecessary plurals
    return "1 byte"

  suffixes_table = [('bytes',0),('KB',0),('MB',1),('GB',2),('TB',2), ('PB',2)]

  num = float(size_bytes)
  for suffix, precision in suffixes_table:
    if num < 1024.0:
      break
    num /= 1024.0

  if precision == 0:
    formatted_size = "%d" % num
  else:
    formatted_size = str(round(num, ndigits=precision))

  return "%s %s" % (formatted_size, suffix)

def msize001(file):
  import win32file
  desiredAccess       = win32file.GENERIC_READ
  shareMode           = win32file.FILE_SHARE_READ
  CreationDisposition = win32file.OPEN_EXISTING
  flagsAndAttributes  = win32file.FILE_ATTRIBUTE_READONLY
  attributes          = None
  hTemplateFile       = 0
  h = win32file.CreateFile(file, desiredAccess , shareMode , attributes , CreationDisposition , flagsAndAttributes , hTemplateFile)
  return win32file.GetFileSize(h)


def stats(file):
  # print GetHumanReadable(int(os.stat(file).st_size))
  # print human_size(os.stat(sys.argv[1]).st_size)
  print human_size(msize001(sys.argv[1]))
  # print sizeof_fmt(msize001(sys.argv[1]))
  # print sizeof_fmt1(msize001(sys.argv[1]))
  # print convertSize(msize001(sys.argv[1]))

stats(sys.argv[1])