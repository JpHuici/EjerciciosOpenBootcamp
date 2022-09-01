#En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener una lista de elementos seleccionables, también debe de tener un label con el texto que queráis.

import tkinter as tk
app = tk.Tk()
element = tk.StringVar()
listbox = tk.Listbox(app)
for item in ["BMW", "Renault", "Peugeot", "Ford", "Chevrolet"]:
    listbox.insert(tk.END, item)
listbox.pack() # Lista Seleccionable
label = tk.Label(text=" -Marcas de autos- ") # Nombre de la lista
label.pack()
app.mainloop() # Ejecuto el programa