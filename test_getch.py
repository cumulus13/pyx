import  msvcrt
import  sys

def login_passw(prompt = "\t Password : "):
    write = sys.stdout.write

    for x in prompt:
        msvcrt.putch(x)
    passw = ""

    while 1:
        x = msvcrt.getch()
        if x == '\r' or x == '\n':
            break
        if x == '\b':
            # position of my error
            passw = passw[:-1]
        if x == '\x08':
            passw = passw.translate(None,passw[-2])
        else:
            write('*')
            passw = passw + x
    msvcrt.putch('\r')
    msvcrt.putch('\n')
    return passw

def test001(prompt = "input y|n: "):
    write = sys.stdout.write
    for x in  prompt:
        msvcrt.putch(x)
        
    z = msvcrt.getche()
    
    if z == '\r' or z == '\n':
        pass
    if z == '\b':
        # position of my error
        passwd = passw[:-1]
    #print z
        
    msvcrt.putch('\r')
    msvcrt.putch('\n')    
    
test001()
#login_passw()