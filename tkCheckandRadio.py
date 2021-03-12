import tkinter as tk

win = tk.Tk()

c1= tk.IntVar()
c2= tk.IntVar()

cb = tk.Checkbutton(win, text='Music', offvalue=0, onvalue=1, height=5, width=10, variable=c1)
cb.pack()
cb1 = tk.Checkbutton(win, text='Video', offvalue=0, onvalue=1, height=5, width=10, variable=c2)
cb1.pack()

var = tk.IntVar()
r1 = tk.Radiobutton(win, text='option1', variable=var, value=1)
r1.pack()
r2 = tk.Radiobutton(win, text='option2', variable=var, value=2)
r2.pack()
r3 = tk.Radiobutton(win, text='option3', variable=var, value=3)
r3.pack()

win.mainloop()