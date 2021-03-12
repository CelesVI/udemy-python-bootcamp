import tkinter as tk
from tkinter import messagebox

win = tk.Tk()

def hello():
    messagebox.showinfo('From computer', 'Hello!')

b = tk.Button(win, text='popup', command=hello)
b.pack()
win.mainloop()