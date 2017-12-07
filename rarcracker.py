import os
import sys
import winsound
import pyttsx3 as pyttsx
import time
import argparse
from make_colors import make_colors
import subprocess

#usage = "\t\tUsage : " + filename + " rar_file  wordlist[*.*] \n\n" + "\t\t#################################################################\n" + "\t\t#\t\t\t\t\t\t\t\t#\n" + "\t\t#       This Only For Archieve With Containt A Password !       #\n" + "\t\t#\t\t\t\t\t\t\t\t#\n" +"\t\t#     Please make sure youre Archieve Containt A Password !     #\n" + "\t\t#\t\t\t\t\t\t\t\t#\n" + "\t\t#################################################################\n"
ZIP7_PATH = r''
if not ZIP7_PATH:
	ZIP7_PATH = '7z'
	
try:
	a = subprocess.check_call([ZIP7_PATH], stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True)
except:
	print make_colors('PLEASE INSTALL OR DEFINITION 7Zip PATH BEFORE OR INSERT IT TO PATH ENVIRONMENT !', 'white', 'red', ['bold', 'blink'])
	sys.exit(0)
	
def usage():
	os.system("cls")
	parser = argparse.ArgumentParser(formatter_class= argparse.RawTextHelpFormatter, version= '2.0')
	parser.add_argument('PACKFILE', help = 'Compression file', action = 'store')
	parser.add_argument('PASSFILE', help = 'Wordlist Password file', action = 'store')
	if len(sys.argv) == 1:
		parser.print_help()
	else:
		args = parser.parse_args()
		#rst_cek = ["Wrong password", "Sub items Errors", "Can't open as archive"]
		
		print "\n"
		print make_colors("\t File Pack  : ", 'cyan') + make_colors(args.PACKFILE, 'green')
		print make_colors("\t Wordlist   : ", 'green') + make_colors(args.PASSFILE, 'cyan')
		print "\n"
		if os.path.isfile(args.PASSFILE):
			cek_pass = open(args.PASSFILE).readlines()
			#print "cek_pass =", cek_pass
		else:
			print make_colors("PASSFILE NOT FOUND", 'white', 'red', ['bold', 'blink'])
			parser.print_help()
			sys.exit()
		for i in cek_pass:
			if not str(i).strip() == "":
				pass1 = str(i).strip()
				break
		cek_rar = os.popen("7z t \"" + args.PACKFILE + "\" -p\"" + pass1 + "\"").readlines()
		if "Everything is Ok" in cek_rar:
			print "\t " + make_colors("This file is Not have Password :)", 'white', 'blue')
			sys.exit("\t NOT PASSWORED :)")
		for i in cek_pass:
			cek_rar = os.popen("7z t \"" + args.PACKFILE + "\" -p\"" + str(i).strip() + "\"").readlines()
			#print "cek_rar =", cek_rar
			if "Everything is Ok\n" in cek_rar:
				print "\t " + make_colors("PASSWORD FOUND !", 'white', 'yellow', ['bold', 'blink'])
				print "\t " + make_colors("Cek For Password : ", 'green') + ' "' + make_colors(str(i).strip(), 'yellow') + '" ' + make_colors("is True", 'white', 'yellow')
				dNotsound = r"f:\SOUNDS\Pass Found.wav"
				winsound.PlaySound(dNotsound, winsound.SND_ALIAS)
				engine = pyttsx.init()
				rate = engine.getProperty('rate')
				engine.setProperty('rate', rate-30)
				engine.say("The password is " + str(i).strip())
				engine.runAndWait()
				print "\n"
				print "\t " + make_colors("Password file ", 'white', 'green') + make_colors(args.PACKFILE, 'red') + make_colors(": ", 'green') + '"' + make_colors(str(i).strip(), 'white', 'yellow') + '"'
				print "\n"
				sys.exit("\t PASSWORD FOUND :)")
			else:
				print "\t " + make_colors("Cek For Password : ", 'green') + ' "' + make_colors(str(i).strip(), 'white') + '" is ' + make_colors("FALSE", 'white', 'red')
					
		print "\n"
		print "\t "+ make_colors("Sorry, PASSWORD NOT FOUND ! ", 'white', 'red', ['bold', 'blink']) + "\n\n"
		dNotsound = r"f:\SOUNDS\Pass Not  Found.wav"
		winsound.PlaySound(dNotsound, winsound.SND_ALIAS)
		sys.exit("\t PASSWORD NOT FOUND (:\n\n\t\t----- RarCracker V2 -----\n\t\t---- Sript By BL4CK1D ----")
		
if __name__ == '__main__':
	usage()