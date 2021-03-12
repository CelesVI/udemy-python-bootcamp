import tkinter as tk

win = tk.Tk()

win.title('first')
top = tk.Toplevel()
top.title('second')

lb = tk.Listbox(win)
lb.insert(1, 'python')
lb.insert(2, 'c')
lb.insert(3, 'c++')
lb.insert(4, 'jquery')
lb.insert(5, 'ruby')

lb.pack()

win.mainloop()