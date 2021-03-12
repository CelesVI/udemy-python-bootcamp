import tkinter as tk

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def mod(a,b):
    return a%b

def lcm(a,b):
    l = a if a>b else b
    while l <= a*b:
        if l%a == 0 and l%b == 0:
            return l
        l+=1

def hcf(a,b):
    h = a if a<b else b
    while h >= 1:
        if a%h == 0 and a%h == 0:
            return h
        h-=1

def extratFromText(text):
    l = []
    for i in text.split(' '):
        try:
            l.append(float(i))

        except ValueError:
            pass
    return l

def calculate():
    text = textin.get()
    for word in text.split(' '):
        if word.lower() in operations.keys():
            try:
                l = extratFromText(text)
                r = operations[word.lower()](l[0], l[1])
                lst.delete(0,tk.END)
                lst.insert(tk.END,r)
            except:
                lst.delete(0,tk.END)
                lst.insert(tk.END,'Somethin went wrong.Try again')
            finally:
                break
        elif word.lower() not in operations.keys():
            lst.delete(0,tk.END)
            lst.insert(tk.END,'Somethin went wrong.Try again')

operations = {'add':add, 'addition':add, 'sum':add, 'plus':add,
                'sub':sub, 'difference':sub, 'minus':sub, 'subtract':sub,
                'lcm':lcm, 'hcf':hcf, 'product':mul, 'multiplication':mul,
                'multiply':mul, 'division':div, 'div':div, 'mod':mod,
                'remander':mod, 'modulus':mod}

win = tk.Tk()
win.geometry('500x300')
win.title('Smart Calcu')
win.configure(bg='blue')

l1 = tk.Label(win, text='Smart calculator', padx=3)
l1.place(x=150,y=10) 
l2 = tk.Label(win, text='How can i help you?', padx=3)
l2.place(x=150,y=130) 

textin = tk.StringVar()
e1 = tk.Entry(win, width=30, textvariable = textin)
e1.place(x=100,y=160)

b1 = tk.Button(win, text='Just this', command=calculate)
b1.place(x=210,y=200)

lst = tk.Listbox(win,width=20,height=3)
lst.place(x=150,y=230) 

win.mainloop()