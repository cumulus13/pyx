import module002a,os

data = [("notepad " ,r"c:\TOOLS\license2.txt"),os.getenv("ProgramFiles") +"\\"  + r"TagScanner\Tagscan.exe",os.getenv("ProgramFiles") +"\\"  + r"MAF-Soft\MP3Test\MP3Test.exe"]

module002a.main(data)