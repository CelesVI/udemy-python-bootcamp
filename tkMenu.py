import tkinter as tk
from tkinter import messagebox

win = tk.Tk()

#Menu options from top of the window.
#nb = tk.Menubutton(win, text='File')
#nb.grid()
#nb.menu = tk.Menu(nb)
#nb['menu'] = nb.menu

#x1 = tk.IntVar()
#x2 = tk.IntVar()

#nb.menu.add_checkbutton(label='open',variable=x1)
#nb.menu.add_checkbutton(label='close',variable=x2)

def nothing():
    file = tk.Toplevel(win)
    button = tk.Button(file,text='Do nothing')
    button.pack()

menubar = tk.Menu(win)

filemenu = tk.Menu(menubar)
filemenu.add_command(label='New Window', command='nothing')
filemenu.add_command(label='New File', command='nothing')
filemenu.add_command(label='New Open', command='nothing')
filemenu.add_separator()
filemenu.add_command(label='Close', command='nothing')
filemenu.add_command(label='Save', command='nothing')
filemenu.add_command(label='Save as', command='nothing')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=win.quit)

editmenu = tk.Menu(menubar)

editmenu.add_command(label='New Window', command='nothing')
editmenu.add_command(label='New Window', command='nothing')
editmenu.add_command(label='New Window', command='nothing')
editmenu.add_command(label='New Window', command='nothing')
editmenu.add_command(label='New Window', command='nothing')


menubar.add_cascade(label='File', menu = filemenu)
menubar.add_cascade(label='Edit', menu = editmenu)

win.config(menu=menubar)

win.mainloop()