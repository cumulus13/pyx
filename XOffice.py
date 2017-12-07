from anygui.backends.mswgui import *
#from anygui import *
import wordx
import Accessx
import excelx
import PowerPointx
import visiox
import OneNotex

def great1(**args):
    wordx.main()

def great2(**args):
    Accessx.main()
    
def great3(**args):
    excelx.main()
    
def great4(**args):
    PowerPointx.main()
    
def great5(**args):
    visiox.main()
    
def great6(**args):
    OneNotex.main()

def keluar(**args):
    win.destroy()
def main():
    win = Window()
    win.title = "X-Office"
    win.size = (350, 350)
    opt1 = Options(left=500, width=70, height=50, position=(180, 150), text= 'Microsoft Office Word 2007')
    opt2 = Options(left=50, width=70, height=50, text= 'Microsoft Office Access 2007')
    opt3 = Options(left=50, width=70, height=50, text= 'Microsoft Office Excel 2007')
    opt4 = Options(left=50, width=70, height=50, text= 'Microsoft Office PowerPoint 2007')
    opt5 = Options(left=50, width=70, height=50, text= 'Microsoft Office Visio 2007')
    opt6 = Options(left=50, width=70, height=50, text= 'Microsoft Office OneNote 2007')
    opt7 = Options(left=50, width=70, height=50, text= 'Exit / Quit')
    #bt = Button(left=50, width=70, height=50, text='button1')
    label = Label(text='blackid')
    bt1 = Button(opt1)
    bt2 = Button(opt2)
    bt3 = Button(opt3)
    bt4 = Button(opt4)
    bt5 = Button(opt5)
    bt6 = Button(opt6)
    bt7 = Button(opt7)
    #btn = Button(left=50, width=70, height=50, text='button3')
    rect = [400, 400, 70, 50]
    #rect[3] = 100
    bt1.refresh()
    bt2.refresh()
    bt3.refresh()
    bt4.refresh()
    bt5.refresh()
    bt6.refresh()
    bt7.refresh()
    bt1.geometry = rect
    #win.title = 'blackid'
    #win.size = (500, 500)
    #win.set(title = 'guigui', size = (300, 300))
    #win.add(bt)
    #win.add(label, position=(180, 150))
    #win.add(label, left=180, top=150)
    #win.add(label, top=180, right=150)
    win.add(label, position=(180, 150), right=1 ,hstretch=1)
    win.add((bt1, bt2, bt3, bt4, bt5, bt6, bt7), position=(10,10), direction='right', space=10)
    #win.add(bt2)
    link(bt1, great1)
    link(bt2, great2)
    link(bt3, great3)
    link(bt4, great4)
    link(bt5, great5)
    link(bt6, great6)
    link(bt7, keluar)
    app = Application()
    app.add(win)
    app.run()

if __name__ == '__main__':
	main()