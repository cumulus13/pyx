import msvcrt

def getPutch(prompt="\t please input a word : "):
    for x in prompt:
        msvcrt.putch(x)

    z = msvcrt.getch()
    msvcrt.putch("\n")
    print "z =", z
    return z

# getPutch()
msvcrt.putch('\x20')