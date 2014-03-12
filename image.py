from PIL import Image
import glob, os
import sys
import traceback
#from pyparsing import commaSeparatedList

filename = os.path.split(sys.argv[0])[1]
usage = "\t use : " + filename + " option [image file]\n\n\t option : [resize]"

def resize(data, mode=None):
	try:
		if mode == None:
			mode = "ANTIALIAS"
			ix = Image.open(str(data))	
		print "\n"
		print "\t This image have size : ", ix.size
		print "\n"
		#print im.mode
		#print im.format
		rsize = raw_input("\r\t Do want to resize it ?\n\r\t Please insert size you want \n\r\t exp: 250,250] | 250x250 | 250|250\n\r\t Or type \"exit\" or \"quit\" to Exit or end this : ")
		if rsize == "exit" or rsize == "Exit" or rsize == "EXIT" or rsize == "quit" or rsize == "Quit" or rsize == "QUIT":
			os.system("cls")
			print "\n"
			print "\t Image failed resize ! \n"
			print "\t Exit ... ! "
			sys.exit()
		elif "x" in rsize:
			if " " in rsize:
				pass
			else:
				pdata = str(rsize).split("x")
				#print "pdataA = ", pdata
				im = Image.open(str(data)).resize((int(pdata[0]), int(pdata[1])))
				im.save(data)
				print "\n"
				print "\t Image succesfull resize ! \n"
		elif "|" in rsize:
			if " " in rsize:
				pass
			else:
				pdata = str(rsize).split("|")
				#print "pdataB = ", pdata
				im = Image.open(str(data)).resize((int(pdata[0]), int(pdata[1])))
				im.save(data)
				print "\n"
				print "\t Image succesfull resize ! \n"
		else:
			pdata = str(rsize).split(",")
			#print "pdataC = ", pdata
			im = Image.open(str(data)).resize((int(pdata[0]), int(pdata[1])))
			im.save(data)
			print "\n"
			print "\t Image succesfull resize ! \n"
	except:
		print "\n"
		print usage
		if len(sys.argv) > 2:
			if sys.argv[-1] == "-v":
				data_e = traceback.format_exc()
				print "\n"
				print "ERROR : "
				print "\t " + str(data_e)
			else:
				pass
		else:
			pass

		
if __name__ == "__main__":
	try:
		if len(sys.argv) > 1:
			if sys.argv[1] == "resize":
				resize(sys.argv[2])
			else:
				print "\n"
				print "\t Not yet implementation !, sorry, it's still development :)"
				print "\n"
				print usage
		else:
			print "\n"
			print usage
	except:
		data_e = traceback.format_exc()
		print "\n"
		print usage
		print "-"*80
		print "ERROR : "
		print "\t " + str(data_e)