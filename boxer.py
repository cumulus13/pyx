import module001

usage = """test"""

if __name__ == '__main__':
    me = os.getenv("ProgramFiles") +"\\"  + r'Boxer Text Editor\\b.exe'
    #module001.usage(usage)
    module001.main(me)