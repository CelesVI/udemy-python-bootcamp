import tkinter as tk

win = tk.Tk()

def pr():
    print("Hi")

win.geometry("640x480")

b = tk.Button(win, text='button', command=pr, padx=20, pady=30, activeforeground='red')
b.place(x=100,y=200)
b1 = tk.Button(win, text='button1')
b1.place(x=300,y=200)

win.mainloop()
