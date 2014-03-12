import os, errno
import sys
import AppList
import RSS_Publisher
import pdfFactory_Pro_Dispatcher
import ABBYY_PDF_Transformer
import Advanced_Font_Viewer
import AnFX
import WinChm
import foxid_Reader
import CHM2Word_2008
import MOffice
import SolidConverterPDF
import Adobe_Reader_8
import Adobe_Reader_8_Pro
import WinDjView

ket = """
                        1.  RSS Publisher
			2.  pdfFactory Pro
			3.  ABBYY PDF Transformer 1.0
			4.  Advanced Font Viewer
			5.  AnFX
			6.  WinCHM
			7.  Foxit Reader
			8.  CHM-2-Word 2008 Macrobject
			9.  Microsoft Office
			10. SolidConverterPDF
			11. Adobe Reader 8
			12. Adobe Reader 8 Professional
			13. WinDjView-0.5
			 0. Main Menu
			00. Exit
			99. Back
"""


def main():
	os.system("cls")
	print "\n\n"
	print ket
	print "\n\n"
	print "\n\n"
	pilih = raw_input("\t\t\tMasukkan Nomor Application !  : ")
	print "\n"
	if (pilih == '1'):
		RSS_Publisher.main()
		
	elif (pilih == '2'):
		pdfFactory_Pro_Dispatcher.main()
			
	elif (pilih == '3'):
		ABBYY_PDF_Transformer.main()
		
	elif (pilih == '4'):
		Advanced_Font_Viewer.main()
		
	elif (pilih == '5'):
		AnFX.main()
		
	elif (pilih == '6'):
		WinChm.main()
		
	elif (pilih == '7'):
		foxid_Reader.main()
	
	elif (pilih == '8'):
		CHM2Word_2008.main()
			
	elif (pilih == '9'):
		MOffice.main()
		
	elif (pilih == '10'):
		SolidConverterPDF.main()
		
	elif (pilih == '11'):
		Adobe_Reader_8.main()
		
	elif (pilih == '12'):
		Adobe_Reader_8_Pro.main()
		
	elif (pilih == '13'):
		WinDjView.main()
			
	elif (pilih == '0'):
		AppList.main()
		
	elif (pilih == '00'):
		sys.exit()
		
	elif (pilih == '99'):
		AppList.main()
		
	else:
		os.system("cls")
		print "\n\n"
		print AppList.warning
		print "\n\n"

if __name__ == '__main__':
	main()