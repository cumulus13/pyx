from anygui import *
app = Application()
w = Window()
w.title = 'Hello, world!'
w.size = (200, 100)
#w = Window(title='Hello, world!', size=(200,100))
app.add(w)
app.run()

