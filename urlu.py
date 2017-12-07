import sys
import clipboard
import urllib2
from make_colors import make_colors

if len(sys.argv) == 2:
	clipboard.copy(urllib2.unquote(sys.argv[1]))
	print make_colors(urllib2.unquote(sys.argv[1]), 'white', 'red')
else:
	clipboard.copy(urllib2.unquote(clipboard.paste()))
	print make_colors(clipboard.paste(), 'white', 'red')