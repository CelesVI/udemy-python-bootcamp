import tkinter as tk
from tkinter import messagebox

win = tk.Tk()

pw = tk.PanedWindow()
pw.pack(fill='both', expand=1)

left = tk.Entry(pw,bd=5)
pw.add(left)

pw2 = tk.PanedWindow(pw, orient='vertical')
pw.add(pw2)

top = tk.Scale(pw2, orient='horizontal')
pw2.add(top)

button = tk.Button(pw2, text='ok')
pw2.add(button)

win.mainloop()