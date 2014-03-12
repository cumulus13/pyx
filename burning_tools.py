import os, errno
import sys
import gburner
import Nero
import ultraiso
import AppList

burning_tools = """
                        1. gBurner
			2. Nero 7 Premium
			3. UltraISO
			0. Main Menu
"""

def main():
	os.system("cls")
	print "\n\n"
	print burning_tools
	print "\n\n"
	print "\n\n"
	pilih = raw_input("\t\t\tMasukkan Nomor Application !  : ")
	print "\n"
	if (pilih == '1'):
		gburner.main()
		
	elif (pilih == '2'):
		Nero.main()
			
	elif (pilih == '3'):
		ultraiso.main()
		
	elif (pilih == '4'):
		AppList.main()
			
	else:
		os.system("cls")
		print "\n\n"
		print AppList.warning
		print "\n\n"

if __name__ == '__main__':
	main()