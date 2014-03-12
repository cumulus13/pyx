import os, errno
import sys
import ABBYY_PDF_Transformer
import Able2Doc
import SolidConverterPDF
import SolidConverterPDF2
import All_Office_Converter

ket = """
            1. ABBYY PDF Transformer 1.0
            2. Able2Doc Professional
	    3. Solid Converter PDF 2
	    4. Solid Converter PDF 5
	    5. All Office Converter Platinum
            0. Main Menu
            00.Exit
            99.Back
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
		ABBYY_PDF_Transformer.main()
		
	elif (pilih == '2'):
		Able2Doc.main()
			
	elif (pilih == '3'):
		SolidConverterPDF.main()
			
	elif (pilih == '4'):
		SolidConverterPDF2.main()
		
	elif (pilih == '5'):
		All_Office_Converter.main()
		
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
