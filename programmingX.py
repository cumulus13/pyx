import os, errno
import sys
import AppList


programmingx = """
                        1.  Python
			2.  Perl
			3.  Java
			4.  Ruby
			5.  Pascal
			6.  TCL
			7.  Visual Basic
			8.  Eiffel
			9.  Seccia
			10. NSIS
			11. C/C++
			12. Klorofil
			13. BAT
			14. BASH
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
		AppList.utama()

def utama():
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
		AppList.utama()

if __name__ == '__main__':
	main()