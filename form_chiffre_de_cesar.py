from tkinter import * 
from chiffre_de_cesar import *

def button_chiffrer_callback():
    liste=decoupage(value.get())
    textarea.delete("0.0",END)
    textarea.insert(END, chiffrage(liste))

def button_dechiffrer_callback():
    liste=decoupage(value.get())
    textarea.delete("0.0",END)
    textarea.insert(END, dechiffrage(liste))

frame = Tk()
frame.title("Chiffrement de Cesar")

value = StringVar() 
value.set("texte par défaut")
entry = Entry(frame, textvariable=value, width=30)
entry.grid(column=0, row=0,columnspan=2) 

button_chiffrer = Button(frame, text="Chiffrer", command=button_chiffrer_callback)
button_chiffrer.grid(column=0, row=1)

button_dechiffrer = Button(frame, text="Dechiffrer", command=button_dechiffrer_callback)
button_dechiffrer.grid(column=1, row=1)

textarea = Text(frame, wrap='word')
textarea.grid(column=0,row=2,columnspan=2)
textarea.insert(END, "Hello World")

frame.mainloop()
