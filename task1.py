#!python3

import tkinter as tk 
from tkinter import *

window = tk.Tk()
window.title("tk")
window.geometry("600x50")

nF = Frame()

fentry1 = tk.Entry(nF,text="num 1")
flabel1 = tk.Label(nF,text="x", borderwidth=6)
fentry2 = tk.Entry(nF,text="num 2")
fbutton1 = tk.Button(nF,text="=")
fentry3 = tk.Entry(nF,text="answer")

nF.pack()
fentry1.pack(side=LEFT)
flabel1.pack(side=LEFT)
fentry2.pack(side=LEFT)
fbutton1.pack(side=LEFT)
fentry3.pack(side=LEFT)


window.mainloop()