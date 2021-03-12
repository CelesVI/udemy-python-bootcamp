import tkinter as tk
from tkinter import messagebox

win = tk.Tk()

#b=0
#for i in range(6):
#    for j in range(6):
#        b += 1
#        tk.Button(win, text=str(b), borderwidth=1).grid(row=i, column=j)

l1 = tk.Label(win, text='Maths')
l1.place(x=10, y=10)
e2 = tk.Entry(win, bd=5)
e2.place(x=60, y=10)
l1 = tk.Label(win, text='English')
l1.place(x=10, y=60)
e2 = tk.Entry(win, bd=5)
e2.place(x=60, y=60)

win.mainloop()