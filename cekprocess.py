import sys
import os
import winsound

def cekint(data_cek, dsound, nsound):
	data = os.popen("processx").readlines()
	len_data = len(data)
	try:
		if (len(sys.argv) > 1):
			#cek = sys.argv[1]
			cek = data_cek
			for i in range(0, len_data):
				if (cek in data[i]):
					#print "\t TRUE \n"
					winsound.PlaySound(dsound, winsound.SND_ALIAS)
					
					#winsound.PlaySound(nsound, winsound.SND_ALIAS)
					break
					sys.exit()
				else:
					pass
					
		else:
			print "\t Please insert a argument ! \n"
	except IndexError, e:
		print "\t ", str(e)
		
if __name__ == '__main__':
	cekint(sys.argv[1], sys.argv[2], sys.argv[3])
	