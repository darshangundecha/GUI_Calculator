from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if(text=="C"):
        scvalue.set("")
    elif(text=="="):
        scvalue.set(eval(scvalue.get()))
    else:
        scvalue.set(scvalue.get() + text)
    screen.update()
top=Tk()
top.geometry("400x500")
top.minsize(width=400, height=500)
top.maxsize(width=400, height=500)
top.title("Calculator by Darshan Gundecha")
scvalue=StringVar()
scvalue.set("")

screen = Entry(top, textvar=scvalue, font="lucida 40", relief="sunken")
screen.pack(padx="20", pady="10")
f = Frame(top,bg="grey")
b = Button(f, text="9", height=5, width=10, font="10")
b.pack(side="left")
b.bind("<Button-1>", click)
b = Button(f, text="8", height=5, width=10, font="10")
b.pack(side="left")
b.bind("<Button-1>", click)
b = Button(f, text="7", height=5, width=10, font="10")
b.pack(side="left")
b.bind("<Button-1>", click)
b = Button(f, text="C", height=5, width=10, font="10")
b.pack(side="left")
b.bind("<Button-1>", click)
f.pack()
f = Frame(top,bg="grey")
b = Button(f, text="6", height=5, width=10, font="10")
b.pack(side="left")
b.bind("<Button-1>", click)
b = Button(f, text="5", height=5, width=10, font="10")
b.pack(side="left")
b.bind("<Button-1>", click)
b = Button(f, text="4", height=5, width=10, font="10")
b.pack(side="left")
b.bind("<Button-1>", click)
b = Button(f, text="/", height=5, width=10, font="10")
b.pack(side="left")
b.bind("<Button-1>", click)
f.pack()
f = Frame(top,bg="grey")
b = Button(f, text="3", height=5, width=10, font="10")
b.pack(side="left")
b.bind("<Button-1>", click)
b = Button(f, text="2", height=5, width=10, font="10")
b.pack(side="left")
b.bind("<Button-1>", click)
b = Button(f, text="1", height=5, width=10, font="10")
b.pack(side="left")
b.bind("<Button-1>", click)
b = Button(f, text="*", height=5, width=10, font="10")
b.pack(side="left")
b.bind("<Button-1>", click)
f.pack()
f = Frame(top,bg="grey")
b = Button(f, text="0", height=5, width=10, font="10")
b.pack(side="left")
b.bind("<Button-1>", click)
b = Button(f, text="+", height=5, width=10, font="10")
b.pack(side="left")
b.bind("<Button-1>", click)
b = Button(f, text="-", height=5, width=10, font="10")
b.pack(side="left")
b.bind("<Button-1>", click)
b = Button(f, text="=", height=5, width=10, font="10")
b.pack(side="left")
b.bind("<Button-1>", click)
f.pack()
top.mainloop()