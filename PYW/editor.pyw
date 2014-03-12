import os,sys,errno

os.system('cls')

list = """

1.  Boxer Text Editor      = Universal Text  Editor (All Language)

2.  AptEdit Pro            = 32-bit full-featured text, HEX, HTML, PHP, Java, Perl, 
                              Ruby, Scala, Python, Javascript, VBScript, SQL, 
                              
3.  ConTEXT Editor         = A small, fast and powerful freeware text editor, 
                              developed to serve as a secondary tool for software developers. 
                              (All Language) 
                              
4.  Syn Editor             = Open Source Text- and Programming Editor with Syntaxhighlight 
                              for many Languages, and some IDE Features, like starting a program
                              (e.g. Compiler) and capture the output, support for Projects etc. 
                              syn is written in Delphi (Version 5, Updatepack 1) for maximum performance,
                              stability and filesize, hence it doesn't require any bulky VC++/VB Runtime 
                              or MFC libraries! (All Language)
                              
5.  Total Edit             = A Unicode based text and code editor that offers the following functionality
                              (xml, xsl, sql, php ,java, html, cs, bat, c, cpp, h, vbs)

6.  Zion Editor            = ZionEdit will parse standard Scintilla type call tip files, but in true 
                              ZionEdit style adds a few nifty extensions of its own. (All Language)
                              
7.  CopyWriter             = RTF, TXT, DOC Other Editor (txt, rft, doc)

8.  EditPad Lite           = HTML Other Editor (html)

9.  NaviCoder Editor       = NaviCoder Editor is a professional source code editor for Windows and 
                              is useful for people who work with various programming environments. 
                              It supports various programming languages/ script files such as HTML, 
                              C/C++, Perl, Python, Java, PHP, ASP, VBScript and more, up to 46 types.

10. RJ TextEd              = RJ TextEd is a Unicode text and source code editor. 
                              It is also a simple web development tool. 
                              The editor uses syntax definition files to recognize keywords, 
                              tags, strings and other items for syntax highlighting in the source. 
                              The editor is also able to handle and detect Unicode.
                              The editor can use auto completion and hints to assist you in editing 
                              your source code. You can preview Html/ASP/PHP... code using one of the 
                              preview tabs or open a document in a browser. The editor does not only 
                              handle source code. It also handles true ASCII files, binary files and 
                              of course plain text files. (nfo, diz, syx, ini, asp, aspx, cf, cfscript,
                              cpp, c, h, cs, css, html, java, js, jsp, pas, perl, php, reg, vb, vbs, wsf,
                              xml, xsl)
                              
11. nPad2                  = Simple Programmer Editor (All Language)

12. SuperEdi               = Simple Programmer Editor With Function List (bat, C#, C/C++, CSS, HHP, 
                              HTML, IDL, INI, InnoSetup, Java, JScript, Makefile, perl, php, reg,
                              rc, sql, syn, vbs, xml, xsl

13. DocPad                 = Simple Editor For (.ini, .log, .bat, .txt)

14. Metapad                = Other Notepad (No Installer)

15. TinyEdit               = Simple Programmer Editor With Syntax Higlight but No Need Installer (All Language)

16. Ezdit                  = TCL/Tk Editor Only with Synax Higlight & Can using TCLKit & SDk For make Exe(.exe) File (Tcl/Tk)

17. JTPad                  = Java Simple Editor with Compiler & Run (Java)

18. BatEdit                = Bat or Batch Editor with Simple & Highlight Syntax Color, for Bat Only (Bat)

19. ProgEdit               = Simple Editor For Many Program (No Installer) (All Langauge)

20. CA Editor              = Simple Java Class Editor for Edit Identify Class File (.class)

21. ML                     = Tcl/Tk Very Simple Editor (Tcl/Tk)

22. KEdit                  = KDE Edit For Windows

23. Notepad 2              = Notepad For Programmer Editor With Syntax Highlight (All Language) 

"""

data = open('d:\pyx\editor_list.txt').read()

data2 = open('d:\pyx\editor_list2.txt').read()

data3 = open('d:\pyx\editor_list.txt').readlines()


#for i in range(0, len(data)):
#	if (data[i] == '3'):
#		print data[i]


#print 'Banyak Baris = ', len(data2), "\n"
#print 'Banyak Huruf = ', len(data)

#print list
try:
	if (sys.argv[1] == '1'):
		os.system('cls')
		print data
	elif (sys.argv[1] == '2'):
		os.system('cls')
		print data2
	else:
		os.system('cls')
		print "\n"
		print "\t\t usage : option 1 : For Detail List"
		print "\n"
		print "\t\t usage : option 2 : For Simple List"

except IndexError, e:
	os.system('cls')
	print "\n\n"
	print data2

except IOError, e:
	os.system('cls')
	print "\n\n"
	print "\t\t File Tidak di temukan ! "


#print data
