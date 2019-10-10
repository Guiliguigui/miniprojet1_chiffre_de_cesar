from tkinter import * 
from chiffre_de_cesar import *

def button_chiffrer_callback():
    cle=int(cle_entry.get())
    liste=decoupage(value.get())
    textarea.delete("0.0",END)
    textarea.insert(END, chiffrage(liste,cle))

def button_dechiffrer_callback():
    cle=int(cle_entry.get())
    liste=decoupage(value.get())
    textarea.delete("0.0",END)
    textarea.insert(END, dechiffrage(liste,cle))

def button_chiffrer_circulaire_callback():
    cle=int(cle_entry.get())
    liste=decoupage(value.get())
    textarea.delete("0.0",END)
    textarea.insert(END, chiffrage_circulaire(liste,cle))

def button_dechiffrer_circulaire_callback():
    cle=int(cle_entry.get())
    liste=decoupage(value.get())
    textarea.delete("0.0",END)
    textarea.insert(END, dechiffrage_circulaire(liste,cle))

frame = Tk()
frame.title("Chiffrement de Cesar")

value = StringVar() 
value.set("texte par defaut")
entry = Entry(frame, textvariable=value, width=30)
entry.grid(column=0, row=0) 

cle=IntVar()
cle.set(8)
cle_entry=Entry(frame, textvariable=cle, width=10)
cle_entry.grid(column=1,row=0)

button_chiffrer = Button(frame, text="Chiffrer", command=button_chiffrer_callback)
button_chiffrer.grid(column=0, row=1)

button_dechiffrer = Button(frame, text="Dechiffrer", command=button_dechiffrer_callback)
button_dechiffrer.grid(column=1, row=1)

button_chiffrer_circulaire = Button(frame, text="Chiffrer_circulaire", command=button_chiffrer_circulaire_callback)
button_chiffrer_circulaire.grid(column=0, row=2)

button_dechiffrer_circulaire = Button(frame, text="Dechiffrer_circulaire", command=button_dechiffrer_circulaire_callback)
button_dechiffrer_circulaire.grid(column=1, row=2)


textarea = Text(frame, wrap='word')
textarea.grid(column=0,row=3,columnspan=2)
textarea.insert(END, "Hello World")

frame.mainloop()
