import tkinter as tk
from tkinter import messagebox

win = tk.Tk()

#s = tk.Scale(win)
#s.pack()

#sb = tk.Spinbox(win, from_ = 0, to=10)
#sb.pack()

scrollbar = tk.Scrollbar(win)
scrollbar.pack(side='right',fill='y')

lst = tk.Listbox(win, yscrollcommand=scrollbar.set)

for line in range(100):
    lst.insert('end', 'This is line number '+ str(line))

lst.pack(side='left',fill='both')

win.mainloop()