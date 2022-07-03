from tkinter import *
master = Tk()
elemento = StringVar()
listbox = Listbox(master)
for item in ["Pan", "Arroz", "Leche", "Pollo", "Carne", "Verduras", "Frutas", "Pasta"]:
 listbox.insert(END, item)
listbox.pack()
label = Label(text="Lista de compras")
label.pack()
master.mainloop()