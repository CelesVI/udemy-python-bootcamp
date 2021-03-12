import tkinter as tk
from functools import partial
win = tk.Tk()

#l = tk.Label(win, text='username')
#l.pack(side='left')
#e = tk.Entry(win)
#e.pack(side='right')
#t = tk.Text(win)
#t.insert('insert','hello')
#t.pack()

def sum(label, x1, x2):
    n1 = (x1.get())
    n2 = (x2.get())
    sum = int(n1) + int(n2)
    label.config(text='Sum is %d' %sum)
    return

l1 = tk.Label(win, text='First no')
l1.grid(row=1,column=0)
l2 = tk.Label(win, text='Second no')
l2.grid(row=2,column=0)
label = tk.Label(win)
label.grid(row=6, column=2)

x1 = tk.StringVar()
x2 = tk.StringVar()

e1 = tk.Entry(win, textvariable=x1)
e1.grid(row=1,column=2)
e2 = tk.Entry(win, textvariable=x2)
e2.grid(row=2,column=2)

sum = partial(sum,label,x1,x2)


button = tk.Button(win, text='calculate', command=sum)
button.grid(row=3,column=0)

win.mainloop()