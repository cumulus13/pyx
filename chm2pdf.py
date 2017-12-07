import module002a,os
import traceback
import e_console

try:
	data = [os.getenv("ProgramFiles") +"\\"  + r"CHM To PDF Converter PRO\CHM To PDF Converter PRO.exe"]
	module002a.main(data)
	
except:
	data_e = traceback.format_exc()
	e_console.Dialog("CHM to PDF", str(data_e))


