import tkinter as tk
import dataBackend as back

def getSelectedRow(event):
    global selected_row
    index = lst.curselection()[0]
    selected_row = lst.get(index)
    e1.delete(0,tk.END)
    e1.insert(tk.END,selected_row[1])
    e2.delete(0,tk.END)
    e2.insert(tk.END,selected_row[2])
    e3.delete(0,tk.END)
    e3.insert(tk.END,selected_row[3])
    e4.delete(0,tk.END)
    e4.insert(tk.END,selected_row[4])
    e5.delete(0,tk.END)
    e5.insert(tk.END,selected_row[5])
    e6.delete(0,tk.END)
    e6.insert(tk.END,selected_row[6])

def viewCommand():
    lst.delete(0,tk.END)
    for row in back.view():
        lst.insert(tk.END,row)

def searchCommand():
    lst.delete(0,tk.END)
    for row in back.search(date_text.get(),earning_text.get(),exercise_text.get(),study_text.get(),diet_text.get(),python_text.get()):
        lst.insert(tk.END,row)

def insertCommand():
    back.insert(date_text.get(),earning_text.get(),exercise_text.get(),study_text.get(),diet_text.get(),python_text.get())
    lst.delete(0,tk.END)
    lst.insert(tk.END,date_text.get(),earning_text.get(),exercise_text.get(),study_text.get(),diet_text.get(),python_text.get())

def deleteCommand():
    back.delete(selected_row[0])

win = tk.Tk()

win.wm_title('First database')

l1 = tk.Label(win, text='Date')
l1.grid(row=0,column=0)
l2 = tk.Label(win, text='Earning')
l2.grid(row=0,column=2)
l3 = tk.Label(win, text='Exercise')
l3.grid(row=1,column=0)
l4 = tk.Label(win, text='Study')
l4.grid(row=1,column=2)
l5 = tk.Label(win, text='Diet')
l5.grid(row=2,column=0)
l6 = tk.Label(win, text='Python')
l6.grid(row=2,column=2)

date_text = tk.StringVar()
e1 = tk.Entry(win, textvariable=date_text)
e1.grid(row=0,column=1)

earning_text = tk.StringVar()
e2 = tk.Entry(win, textvariable=earning_text)
e2.grid(row=0,column=3)

exercise_text = tk.StringVar()
e3 = tk.Entry(win, textvariable=exercise_text)
e3.grid(row=1,column=1)

study_text = tk.StringVar()
e4 = tk.Entry(win, textvariable=study_text)
e4.grid(row=1,column=3)

diet_text = tk.StringVar()
e5 = tk.Entry(win, textvariable=diet_text)
e5.grid(row=2,column=1)

python_text = tk.StringVar()
e6 = tk.Entry(win, textvariable=python_text)
e6.grid(row=2,column=3)

lst = tk.Listbox(win,height=8,width=35)
lst.grid(row=3,column=0,rowspan=9,columnspan=2)

sb = tk.Scrollbar(win)
sb.grid(row=3,column=2,rowspan=9)

lst.bind('<<ListboxSelect>>',getSelectedRow)

b1 = tk.Button(win,text='Add',width=12,pady=5, command=insertCommand)
b1.grid(row=3,column=3)

b2 = tk.Button(win,text='Search',width=12,pady=5, command=searchCommand)
b2.grid(row=4,column=3)

b3 = tk.Button(win,text='Delete',width=12,pady=5)
b3.grid(row=5,column=3)

b4 = tk.Button(win,text='View all',width=12,pady=5, command=viewCommand)
b4.grid(row=6,column=3)

b5 = tk.Button(win,text='Close',width=12,pady=5, command=win.destroy)
b5.grid(row=7,column=3)


win.mainloop()