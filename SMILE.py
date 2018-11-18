from tkinter import *
from tkinter import ttk

def Prov(*args):
     msg_label.set(msg_entry.get())
     msg_entry.set('')

root=Tk()
root.title("bestemminetor-2000")

mainframe=ttk.Frame(root, padding="12 20 12 20")
mainframe.grid(column=0, row=0)

msg_entry= StringVar()
msg_label=StringVar()
ttk.Entry(mainframe, width=8,textvariable=msg_entry ).grid(column=0, row=5)
ttk.Button(mainframe, text="la madonna è fatta di...", command=Prov).grid(column=0, row=0)

ttk.Label(mainframe, text="ella", textvariable=msg_label).grid(column=0, row=1)

root.mainloop()