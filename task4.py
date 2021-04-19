#!python3

import tkinter as tk 
from tkinter import *

window = tk.Tk()
window.title("Example")
window.geometry("400x200")

dogp = PhotoImage(file="dog.png")

label1 = Label(window, image=dogp)
label2 = Label(window, text="Pochacco!")
label3 = Label(window, text=" A cuddly little puppy! This is from the same ", background="#aaffff")
label4 = Label(window, text="creators who brought you Keropi and Kero Kero", background="#aaffff")

label1.place(x=130, y=40)
label2.place(x=190, y=75)
label3.place(x=70, y=140)
label4.place(x=60, y=160)

window.mainloop()