import tkinter as tk

win = tk.Tk()
frame = tk.Frame(win)
frame.pack()

frame2 = tk.Frame(win)
frame2.pack()

rb = tk.Button(frame, text='red',fg='red')
rb.pack(side='left')

gb = tk.Button(frame, text='red',fg='green')
gb.pack(side='bottom')

bb = tk.Button(frame, text='red',fg='black')
bb.pack(side='bottom')

blb = tk.Button(frame, text='red',fg='blue')
blb.pack(side='bottom')

win.mainloop()