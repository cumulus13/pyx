import os, errno
import sys
import Game
import tigad
import boottools
import browser_tools
import burning_tools
import cd_dvd_tools
import compression_tools
import desktop_appereance
import Office



head = """
			###########################################################
			#                                                         #
			#                     ALL Application                     #
			#                                                         #
			#                       by BLACKID                        #
			#                                                         #
			###########################################################
"""
ket = """
			1.  3D Designer                         21. Manager & Commander Tools
			2.  Boot Tools                          22. Misc
			3.  Browser Tools                       23. Monitoring Hardware
			4.  Burning Tools                       24. Music Video Player & Tools                           
			5.  Cd & DVD Tools                      25. Networking Tools
			6.  Copmression Tools                   26. Network emulator
			7.  Desktop Appereance                  27. Office Tools
			8.  Editor & IDE                        28. OS Symulator
			9.  Email & Chat Tools                  29. Programming
			10. Encryption Tools                    30. Programming Professional
			11. Error Cek                           31. Rebuild Tools
			12. Firewall                            32. Recovery Tools
			13. Flash Tools                         33. Repair Tools
			14. Game                                34. Searching Tools
			15. Grafis Tools                        35. Secure Tools
			16. Hack & Crack                        36. Server Tools
			17. Handphone Tools                     37. SQL Tools
			18. Islamic Tools                       38. System Analisis Search
			19. Kamus & Toofel                      39. Uninstaller Tools
			20. Maintenance                         00. Exit
		
"""



editor_ide = """
                        1.  EditPlus 2
			2.  Emacs
			3.  Notepad++
			4.  Vim 6.4
			5.  Arachno Ruby IDE
			6.  EngInSite CSS Editor
			7.  EngInSite Perl Editor
			8.  NuSphere
			9.  JCreator Pro
			10. PyScripter
			11. Wing IDE 3.0
			12. wx-devcpp
			13. Aset TCL IDE
			14. Xo TCL IDE
			15. ActiveState Komodo IDE 5
			16. Programmer's Notepad
			0.  Main Menu
"""

email_chat_tools = """
                        1.  IceWarp Outlook Connector
			2.  IndigoMail
			3.  Sendmail
			4.  MDGUI
			5.  PSI
			6.  Chat Anywhere
			7.  Easy Chat Server
			8.  mIRC
			9.  ParaChat Server Standard Edition
			10. RealChat
			11. SendMail
			12. VisualChat
			13. Pidgin
			0. Main Menu
"""

encryption_tools = """
                        1. Kruptos 2
			0. Main Menu
"""

error_cek = """
                        1. Error Messages for Windows
			0. Main Menu
"""

firewall = """
                        1. GhostWall
			0. Main Menu
"""
flash_tools = """
                        1. SWF 'n Slide Pro
			2. SWFKit Pro 3
			0. Main Menu
"""


			
grafis_tools = """
                        1. Adobe Web Premium CS3
			2. CorelDRAW Graphics Suite X3
			3. IcoFX
			4. AnFX
			5. Paint.NET
			0. Main Menu
"""

hack_crack = """
                        1. Unlocker
			2. PASSWORD TOOLS
			3. 007 STARR
			4. PE Explorer
			5. Resource Hacker (reshacker)
			0. Main Menu
"""

islamic_tools = """
                        1. Bukhari, Muslim, Malik, and Dawud Hadith Collection
			0. Main Menu
"""

handphone_tools = """
                        1. Xilisoft Mobile Phone Manager
			2. Siemens Mobile Control
			0. Main Menu
"""

kamus_toofel = """
                        1. uKamus
			2. 4 in 1 Euro Dictionary
			3. ORS
			4. Oxford CompLex
			0. Main Menu
"""

maintenance = """
                        1. CCleaner
			2. FreeRAM XP Pro
			3. RegCure
			4. Webroot
			5. Registry Cleaner
			6. Registry Mechanic
			7. System Mechanic
			8. Auslogics BootSpeeder
			9. O&O Defrag
			0. Main Menu
"""

manager_tools = """ 
                        1. Far Manager
			2. Total Commander
			0. Main Menu
"""

misc = """
                        1. Baku
			2. Shutter
			3. Total Commander
			0. Main Menu
"""

monitor_tools = """
                        1. Hmonitor
			0. Main Menu
"""

music_video_player_tools = """
			1.  DRM & RIPPER
			2.  DrmRemoval
			3.  FLV Player
			4.  iTunes
			5.  iZotope
			6.  Kantaris
			7.  KaraFun
			8.  K-Lite Codec Pack
			9.  Media Player Classic
			10. Total Video Converter OJOsoft
			11. QuickTime
			12. Realtek Sound Manager
			13. SoundTaxi
			14. Swiff Point Player
			15. Tunebite
			16. Video mp3 Extractor Pro
			17. ConvertXtoDVD 3 VSO
			18. Winamp
			19. Applian FLV Player
			20. Windows Movie Maker
			21. AIXcoustic - Electri-Q
			22. DFX Audio Enhancer
			23. MP3Test
			24. Playlist Creator 3
			25. Steinberg WaveLab
			26. Windows Media Player
			0. Main Menu
"""

network_emulator = """
			1. Boson Software
			2. Dynamips & Dynagen
			0. Main Menu
"""

networking_tools = """
                        1.  Boson Software
			2.  Earth Bridge
			3.  Connection Keeper
			4.  GFI LANguard Network Security Scanner 5.0
			5.  LanCalculator LanTricks
			6.  Net Control 2
			7.  RealVNC
			8.  SecureCRT 3.4
			9.  Simple DNS Plus
			10. WinSCP3
			11. Xshell 3
			12. Cisco TFTP Server
			13. NetworkActiv Sniffer 1.4
			14. Angryziber
			15. IP Subnet Calculator 3 Net3 Group
			16. Net Meter
			17. Nmap
			18. Remote Assistance
			0. Main Menu
"""



os_simulator = """
                        1. VMware
			2. VFD Control Panel
			0. Main Menu
"""

programming = """
                        1.  aaxComponents
			2.  Bloodshed Dev-C++
			3.  CodeBlocks
			4.  Perl Master Golabs
			5.  Java Web Start
			6.  MinGW Developer Studio
			7.  NSIS
			8.  PyQt GPL v4.4.2 for Python v2.5
			9.  Ruby-186-27
			10. Ruby-GNOME2
			11. Glade
			12. ActivePerl 5.8.8 Build 824
			13. ActiveState ActivePython 2.5
			14. ActiveState ActiveTcl 8.4.10.1
			15. ActiveState ActiveTcl 8.4.19.1
			16. ActiveState Tcl Dev Kit 5.0.1
			17. Aspell
			18. Cygwin
			19. Cygwin-X
			20. EiffelStudio 6.4 (x86)
			21. Gtk+
			22. Klorofil
			23. Quick Batch File Compiler
			24. Resource Database Editor
			25. SharpDevelop 2.2
			26. Singular CAS
			27. Sylvain Seccia
			28. Inno Pascal
			29. Microsoft Visual Basic 2005 Express Edition
			0. Main Menu
"""

rebuild_tools = """
                        1. Windows Unattended CD Creator
			0. Main Menu
"""

repair_tools = """
			1. Advanced RAR Repair
			2. RAR Repair
			0. Main Menu
"""

recovery_tools = """
                        1. Auslogics
			2. EasyRecovery Professional Edition
			3. Rar Repair Tool
			4. Advance Rar Repair Tool
			0. Main Menu
"""

secure_tools = """
                        1. Hide Folders XP
			2. HideWindowPlus
			3. Taskbar Hide
			0. Main Menu
"""

searching_tools = """
                        1. Google Desktop
			2. SearchSpy
			3. Effective File Search
			0. Main Menu
"""

server_tools = """
                        1. Abyss Web Server
			2. IceWarp Merak Mail Server
			3. MailDetective 2.x
			4. Proxy+
			5. WAMP Server
			6. Xming
			0. Main Menu
"""

sql_tools = """
                        1. DBDesigner 4
			2. MySQL Query Browser
			3. OpenLink Software
			4. PostgreSQL 8.3
			5. SQLite Expert
			6. SQLyog Enterprise
			7. Sybase Power Designer
			0. Main Menu
"""
system_analisis_tools = """
                        1. System Restore Control Camtech
			2. Effective File Search
			3. RegSnap
			4. VFD Control Panel
			0. Main Menu
"""
uninstaller_tools = """
                        1. Absolute Uninstaller
			2. Your Uninstaller! 2008
			0. Main Menu
"""





warning = """
			Tidak ada pilihan yang cocok dengan yang anda masukkan ! ! ! !

			Masukkan Nomor Application dengan benar !!!!!

									enjoy by BLACKID
									-----------------
	"""

def main():
	os.system("cls")
	os.system("title Application List")
	print "\n\n"
	print head, "\n\n"
	print ket
	print "\n\n"
	pilih = raw_input("\t\t\tMasukkan Nomor Application !  : ")
	print "\n"

	if (pilih == '1'):
		tigad.main()
	
	elif (pilih == '2'):
		boottools.main()
	
	elif (pilih == '3'):
		browser_tools.main()
	
	elif (pilih == '4'):
		burning_tools.main()
	
	elif (pilih == '5'):
		cd_dvd_tools.main()
	
	elif (pilih == '6'):
		compression_tools.main()
	
	elif (pilih == '7'):
		desktop_appereance.main()
	
	elif (pilih == '8'):
		editor_ide()
	
	elif (pilih == '9'):
		email_chat_tools()
	
	elif (pilih == '10'):
		encryption_tools()
	
	elif (pilih == '11'):
		error_cek()
	
	elif (pilih == '12'):
		firewall()
	
	elif (pilih == '13'):
		FLASH_TOOLS()
	
	elif (pilih == '14'):
		Game.main()
	
	elif (pilih== '15'):
		grafis_tools()
	
	elif (pilih == '16'):
		hack_crack()
	
	elif (pilih == '17'):
		handphone_tools()
	
	elif (pilih == '18'):
		islamic_tools()
	
	elif (pilih == '19'):
		kamus_toofel()	
	
	elif (pilih == '20'):
		maintenance()
		
	elif (pilih == '20'):
		maintenance()
		
	elif (pilih == '21'):
		manager_tools()
	
	elif (pilih == '22'):
		misc()
	
	elif (pilih == '23'):
		monitor_tools()
	
	elif (pilih == '24'):
		music_video_player_tools()
	
	elif (pilih == '25'):
		networking_tools()
	
	elif (pilih == '26'):
		network_emulator()
	
	elif (pilih == '27'):
		Office.main()
	
	elif (pilih == '28'):
		os_simulator()
	
	elif (pilih == '29'):
		programming()
	
	elif (pilih == '30'):
		programmingx()
	
	elif (pilih == '31'):
		rebuild_tools()
	
	elif (pilih == '32'):
		recovery_tools()
	
	elif (pilih == '33'):
		repair_tools()
	
	elif (pilih== '34'):
		searching_tools()
	
	elif (pilih == '35'):
		secure_tools()
	
	elif (pilih == '36'):
		server_tools()
	
	elif (pilih == '37'):
		sql_tools()
	
	elif (pilih == '38'):
		system_analisis_tools()	
	
	elif (pilih == '39'):
		uninstaller_tools()
		
	elif (pilih == '40'):
		os.system("cls")
		exit()
	else:
		os.system("cls")
		print "\n\n"
		print warning

def utama():
	os.system("cls")
	os.system("title Application List")
	print "\n\n"
	print head, "\n\n"
	print ket
	print "\n\n"
	pilih = raw_input("\t\t\tMasukkan Nomor Application !  : ")
	print "\n"

	if (pilih == '1'):
		tigad.main()
	
	elif (pilih == '2'):
		boottools.main()
	
	elif (pilih == '3'):
		browser_tools.main()
	
	elif (pilih == '4'):
		burning_tools.main()
	
	elif (pilih == '5'):
		cd_dvd_tools.main()
	
	elif (pilih == '6'):
		compression_tools.main()
	
	elif (pilih == '7'):
		desktop_appereance.main()
	
	elif (pilih == '8'):
		editor_ide()
	
	elif (pilih == '9'):
		email_chat_tools()
	
	elif (pilih == '10'):
		encryption_tools()
	
	elif (pilih == '11'):
		error_cek()
	
	elif (pilih == '12'):
		firewall()
	
	elif (pilih == '13'):
		FLASH_TOOLS()
	
	elif (pilih == '14'):
		Game.main()
	
	elif (pilih== '15'):
		grafis_tools()
	
	elif (pilih == '16'):
		hack_crack()
	
	elif (pilih == '17'):
		handphone_tools()
	
	elif (pilih == '18'):
		islamic_tools()
	
	elif (pilih == '19'):
		kamus_toofel()	
	
	elif (pilih == '20'):
		maintenance()
		
	elif (pilih == '20'):
		maintenance()
		
	elif (pilih == '21'):
		manager_tools()
	
	elif (pilih == '22'):
		misc()
	
	elif (pilih == '23'):
		monitor_tools()
	
	elif (pilih == '24'):
		music_video_player_tools()
	
	elif (pilih == '25'):
		networking_tools()
	
	elif (pilih == '26'):
		network_emulator()
	
	elif (pilih == '27'):
		Office.main()
	
	elif (pilih == '28'):
		os_simulator()
	
	elif (pilih == '29'):
		programming()
	
	elif (pilih == '30'):
		programmingx()
	
	elif (pilih == '31'):
		rebuild_tools()
	
	elif (pilih == '32'):
		recovery_tools()
	
	elif (pilih == '33'):
		repair_tools()
	
	elif (pilih== '34'):
		searching_tools()
	
	elif (pilih == '35'):
		secure_tools()
	
	elif (pilih == '36'):
		server_tools()
	
	elif (pilih == '37'):
		sql_tools()
	
	elif (pilih == '38'):
		system_analisis_tools()	
	
	elif (pilih == '39'):
		uninstaller_tools()
		
	elif (pilih == '40'):
		os.system("cls")
		exit()
	else:
		os.system("cls")
		print "\n\n"
		print warning


if __name__ == '__main__' :
	main()
	
