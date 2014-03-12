import module002
import sys,os

data = r"d:\pyx\Netmeter\netmeter.exe"

def reset():
	os.system('taskkill /f /im netmeter.exe')
	os.system('del ' + r"d:\pyx\Netmeter\NetMeter.tlg")
	os.system(data)

try:
	if len(sys.argv) > 1:
		if sys.argv[1] == 'reset':
			reset()
		else:
			pass
	else:
		print "\n"
		ask_input = raw_input('\t Do you want to start netmeter ? = ')
		if ask_input == "y":
			module002.main(data)
			sys.exit()
		elif ask_input == "n":
			sys.exit()
			print "\n"
			print "\t Script by BL4CK1D \n"
		else:
			print '\n'
			print "\t" + """Please input y/n \n"""
except IndexError,e:
	print "\n"
	print "\t Error : " + str(e)