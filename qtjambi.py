import os
import sys
import optparse

QTJAMBI_PATH = r'e:\qtjambi\qtjambi-4.4.3_01.jar'
QTJAMBI_DIR = os.path.dirname(QTJAMBI_PATH)
BASE_PATH = os.getcwd()
JAVA_PATH = r'c:\Java\jdk1.8.0\bin\java.exe'
JAVAC_PATH = r'c:\Java\jdk1.8.0\bin\javac.exe'

os.remove(os.path.join(os.getenv('TEMP'), 'qtjambi_stdout.txt'))
if not os.path.isfile(os.path.join(os.getenv('TEMP'), 'qtjambi_stdout.txt')):
    f = open(os.path.join(os.getenv('TEMP'), 'qtjambi_stdout.txt'), 'w')
    f.close()
fname = os.path.join(os.getenv('TEMP'), 'qtjambi_stdout.txt')

if os.path.isfile(QTJAMBI_PATH):
    pass
else:
    raise SystemError('Please definition QTJAMBI_PATH !')

def start(argv, classpath=''):
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
                os.system('mklink ' + ' \"' + os.path.join(BASE_PATH, i) + "\" \"" + os.path.join(QTJAMBI_DIR, 'lib', i) + "\" >>" + str(fname))
    datafile = os.path.splitext(argv)
    filename = os.path.basename(datafile[0])
    if datafile[1] == str('.class').lower():
        os.system(JAVA_PATH + " -classpath " + QTJAMBI_PATH + ";" + str(classpath) + ";" + filename + " >>" + str(fname))
        os.system("DEL *.log")
        os.system("DEL *.dll")
    elif datafile[1] == str('.java').lower():
        os.system(JAVAC_PATH + " -classpath " + QTJAMBI_PATH + ";"  + str(classpath) + ";" + argv)
        os.system(JAVA_PATH + " -classpath " + QTJAMBI_PATH + ";"  + str(classpath) +  ";" + filename + " >>" + str(fname))
        os.system("DEL *.log")
        os.system("DEL *.dll")
    else:
        os.system(JAVAC_PATH + " -classpath " + QTJAMBI_PATH + ";"  + str(classpath) + ";" + argv)
        os.system(JAVA_PATH + " -classpath " + QTJAMBI_PATH + ";" + str(classpath) +  ";" + filename + " >>" + str(fname))
        os.system("DEL *.log")
        os.system("DEL *.dll")            

def usage():
    parser = optparse.OptionParser()
    parser.add_option('-f', '--file', help='file with extension *.java or *.class, but can app name too')
    parser.add_option('-c', '--classpath', help='path to archive (.jar|.zip) or path\'s directory it')
    options, args = parser.parse_args()
    if len(sys.argv) < 2:
        parser.print_help()
    else:
        if options.file:
            if options.classpath:
                start(options.file, options.classpath)
            else:
                start(options.file)                
        else:
            parser.print_help()

usage()    