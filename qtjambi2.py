import os
import sys
import argparse

os.remove(os.path.join(os.getenv('TEMP'), 'qtjambi_stdout.txt'))
if not os.path.isfile(os.path.join(os.getenv('TEMP'), 'qtjambi_stdout.txt')):
    f = open(os.path.join(os.getenv('TEMP'), 'qtjambi_stdout.txt'), 'w')
    f.close()
sys.stdout = f
fname = os.path.join(os.getenv('TEMP'), 'qtjambi_stdout.txt')

QTJAMBI_PATH = r'e:\qtjambi\qtjambi-4.4.3_01.jar'
QTJAMBI_DIR = os.path.dirname(QTJAMBI_PATH)
BASE_PATH = os.getcwd()
JAVA_PATH = r'c:\Java\jdk1.8.0\bin\java.exe'
JAVAC_PATH = r'c:\Java\jdk1.8.0\bin\javac.exe'

if os.path.isfile(QTJAMBI_PATH):
    pass
else:
    raise SystemError('Please definition QTJAMBI_PATH !')

def start(argv):
    dll = ['com_trolltech_qt_core.dll', 
    'com_trolltech_qt_gui.dll', 
    'com_trolltech_qt_network.dll', 
    'com_trolltech_qt_opengl.dll', 
    'com_trolltech_qt_phonon.dll', 
    'com_trolltech_qt_sql.dll', 
    'com_trolltech_qt_svg.dll', 
    'com_trolltech_qt_webkit.dll', 
    'com_trolltech_qt_xml.dll', 
    'com_trolltech_qt_xmlpatterns.dll', 
    'com_trolltech_tools_designer.dll', 
    'qtjambi.dll']
    for i in dll:
        if not os.path.isfile(os.path.join(BASE_PATH, i)):
            if os.path.isfile(os.path.join(QTJAMBI_DIR, 'lib', i)):
                os.system('mklink ' + ' \"' + os.path.join(BASE_PATH, i) + "\" \"" + os.path.join(QTJAMBI_DIR, 'lib', i) + "\"")
            
    datafile = os.path.splitext(argv)
    filename = os.path.basename(datafile[0])
    if datafile[1] == str('.class').lower():
        os.system(JAVA_PATH + " -classpath " + QTJAMBI_PATH + "; " + filename)
        os.system("DEL *.log")
        os.system("DEL *.dll")
    elif datafile[1] == str('.java').lower():
        os.system(JAVAC_PATH + " -classpath " + QTJAMBI_PATH + "; " + argv)
        os.system(JAVA_PATH + " -classpath " + QTJAMBI_PATH + "; " + filename)
        os.system("DEL *.log")
        os.system("DEL *.dll")        
    

def usage():
    parser = argparse.ArgumentParser()
    parser.add_argument('FILE', )
    
start(sys.argv[1])