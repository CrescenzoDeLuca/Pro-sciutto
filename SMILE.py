from tkinter import *
from tkinter import ttk

def Prov(*args):
     msg_entry.set(msg_entry.get())

root=Tk()
root.title("yuop")

mainframe=ttk.Frame(root, padding="12 20 12 20")
mainframe.grid(column=0, row=0)

msg_entry= StringVar()
ttk.Entry(mainframe, width=8,textvariable=msg_entry ).grid(column=0, row=5)
ttk.Button(mainframe, text="la madonna è fatta di...", command=Prov).grid(column=0, row=0)

ttk.Label(mainframe, text="ella", textvariable=msg_entry).grid(column=0, row=1)

root.mainloop()