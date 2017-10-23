import module002
import module003
import os
import sys

data_privoxy = r"d:\pyx\privoxy_bat.bat"
data_ccproxy = r"C:\CCProxy\CCProxy.exe"
data_proxyplus = "ProxyPlus"
data_squid = "squid"
data_winproxy = "winproxy"
data_proxomitron = r"c:\Program Files\Proxomitron Naoko-4\Proxomitron.exe"
data_httpproxy = r"C:\Program Files\DPA_PROXY\DPAHTTPProxy.exe"
data_proxyway = r"c:\Program Files\ProxyWay\proxyway.exe"
data_free_proxy = r"C:\Program Files\Hand-Crafted Software\FreeProxy\FreeProxyClient.exe"
data_analogx_proxy = r"c:\Program Files\AnalogX\Proxy\proxy.exe"
data_paros = r"c:\Program Files\Paros\startserver.bat"
data_proxy_elhttp = r"C:\Program Files\Etlin HTTP Proxy\HTTPProxy.exe"


me_name = os.path.split(sys.argv[0])
filename = me_name[1]
usage = "\t use " + filename + " [Number Of List] "

headlist = """
	1. Privoxy         [port default : 8118] \n
	2. CCProxy 6       [port default : 808 ] \n
	3. Proxy+          [port default : 4480] \n
	4. Squid           [port default : 3128] \n
	5. WinProxy        [port default : 8484] \n
	6. The Proxomitron [port default : 8889] \n
	7. HTTPProxy       [port default : 8585 & SSL = 444] \n
	8. ProxyWay        [port default : 81  ] \n
	9. Free Proxy      [port default : 8282] \n
       10. AnalogX Proxy   [port default : 6588] \n
       11. Paros           [port default : 8383] \n
       12. elHttp Proxy    [port default : 8585] \n
  
"""

os.system("cls")

try:
		if(len(sys.argv) > 1):
			if (sys.argv[1] == "1"):
				module002.main(data_privoxy)
				print "\n"
				print "\t Privoxy being STARTER . . . .\n"
			elif (sys.argv[1] == "2"):
				module002.main(data_ccproxy)
				print "\n"
				print "\t CCProxy being STARTER . . . .\n"
			elif (sys.argv[1] == "3"):
				module003.main(data_proxyplus)
				print "\n"
				print "\t Proxy Plus being STARTER . . . .\n"
			elif (sys.argv[1] == "4"):
				module003.main(squid)
				print "\n"
				print "\t Squid being STARTER . . . .\n"
			elif (sys.argv[1] == "5"):
				module003.main(winproxy)
				print "\n"
				print "\t WinProxy being STARTER . . . .\n"
			elif (sys.argv[1] == "6"):
				module002.main(data_proxomitron)
				print "\n"
				print "\t Proxomitron Proxy being STARTER . . . .\n"
			elif (sys.argv[1] == "7"):
				module002.main(data_httpproxy)
				print "\n"
				print "\t HTTPProxy being STARTER . . . .\n"
			elif (sys.argv[1] == "8"):
				module002.main(data_proxyway)
				print "\n"
				print "\t ProxyWay being STARTER . . . .\n"
			elif (sys.argv[1] == "9"):
				module002.main(data_free_proxy)
				print "\n"
				print "\t Free Proxy being STARTER . . . .\n"
			elif (sys.argv[1] == "10"):
				module002.main(data_analogx_proxy)
				print "\n"
				print "\t AnalogX Proxy being STARTER . . . .\n"
			elif (sys.argv[1] == "11"):
				module002.main(data_paros)
				print "\n"
				print "\t Paros being STARTER . . . .\n"
			elif (sys.argv[1] == "12"):
				module002.main(data_proxy_trace)
				print "\n"
				print "\t elHttp Proxy being STARTER . . . .\n"
			else:
				print "\n"
				print "\t Youre Not Fill with Correct Option !, Please Try Agains ! \n"
				print usage
		else:
			print "\n"
			print headlist
			print "\n"
			choise = raw_input("\t Please Choice Youre Option : ")
			if (choise == ''):
				os.system("cls")
				print "\n"
				print headlist
				print "\n"
				print "\t Youre Not Fill with Correct Option !, Please Try Agains ! \n"
				print usage
			else:
				if (choise == "1"):
					os.system("cls")
					print "\n"
					print headlist
					print "\n"
					print "\t Privoxy being STARTER . . . .\n"
					module002.main(data_privoxy)
				elif (choise == "2"):
					os.system("cls")
					print "\n"
					print headlist
					print "\n"
					print "\t CCproxy being STARTER . . . .\n"
					module002.main(data_ccproxy)
					
				elif (choise == "3"):
					os.system("cls")
					print "\n"
					print headlist
					print "\n"
					print "\t ProxyPlus being STARTER . . . .\n"
					module003.main(data_proxyplus)
					
				elif (choise == "4"):
					os.system("cls")
					print "\n"
					print headlist
					print "\n"
					print "\t Squid being STARTER . . . .\n"
					module003.main(squid)
					
				elif (choise == "5"):
					os.system("cls")
					print "\n"
					print headlist
					print "\n"
					print "\t WinProxy being STARTER . . . .\n"
					module003.main(winproxy)
					
				elif (choise == "6"):
					os.system("cls")
					print "\n"
					print headlist
					print "\n"
					print "\t Proxomitron Proxy being STARTER . . . .\n"
					module002.main(data_proxomitron)
					
				elif (choise == "7"):
					os.system("cls")
					print "\n"
					print headlist
					print "\n"
					print "\t HTTPProxy being STARTER . . . .\n"
					module002.main(data_httpproxy)
					
				elif (choise == "8"):
					os.system("cls")
					print "\n"
					print headlist
					print "\n"
					print "\t ProxyWay being STARTER . . . .\n"
					module002.main(data_proxyway)
					
				elif (choise == "9"):
					os.system("cls")
					print "\n"
					print headlist
					print "\n"
					print "\t FreeProxy being STARTER . . . .\n"
					module002.main(data_free_proxy)
					
				elif (choise == "10"):
					os.system("cls")
					print "\n"
					print headlist
					print "\n"
					print "\t AnalogX Proxy being STARTER . . . .\n"
					module002.main(data_analogx_proxy)
					
				elif (choise == "11"):
					os.system("cls")
					print "\n"
					print headlist
					print "\n"
					print "\t Paros being STARTER . . . .\n"
					module002.main(data_paros)
					
				elif (choise == "12"):
					os.system("cls")
					print "\n"
					print headlist
					print "\n"
					print "\t elHttp Proxy being STARTER . . . .\n"
					module002.main(data_proxy_trace)
					
				else:
					print "\n"
					print "\t Youre Not Fill with Correct Option !, Please Try Agains ! \n"
					print usage
			
except IndexError, e:
	os.system("cls")
	print "\n"
	print usage
				


