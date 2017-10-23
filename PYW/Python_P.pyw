import os, errno
import sys
import AppList

ket = """
            1. Wing IDE
            2. PyScripter
            3. Komodo IDE
            4. pythonWin
            5. Jython
            6. Qt-Assistant
            7. Qt-Designer
            0. Main Menu
            00.Exit
            99.Back
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