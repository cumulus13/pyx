from bs4 import BeautifulSoup as bs
import sys
import os

def convert(html_file):
	with open(html_file, 'r') as f:
		b = bs(f.read(),'lxml')
	print(b.text)
	return b.text
	
if __name__ == '__main__':
	c = convert(sys.argv[1])