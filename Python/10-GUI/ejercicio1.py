#En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado y que contenga un botón de reinicio para que deje todo como al principio.Al principio no tiene que haber una opción seleccionada.
import tkinter as tk 

# Funciones
def select():
    display.config(text="{}".format(option.get()))
def reset():
    option.set(None)
    display.config(text="")
    
coordenadas = tk.Tk()
coordenadas.geometry('400x400') # Tamaño de la ventana

option = tk.StringVar()
option.set(None)
# Botones Seleccionables
radioButtonW = tk.Radiobutton(coordenadas, text = 'West',value = 'West',var = option, width = 20, command = select).pack(side = 'left')

radioButtonE = tk.Radiobutton(coordenadas, text = 'East',value = 'East',var = option, width = 20, command = select).pack(side = 'right')

radioButtonN = tk.Radiobutton(coordenadas, text = 'North',value = 'North',var = option, width = 20, command = select).pack(side = 'top')

radioButtonS = tk.Radiobutton(coordenadas, text = 'South',value = 'South',var = option, width = 20, command = select).pack(side = 'bottom')

display = tk.Label(coordenadas) # Se muestra en la ventana
display.pack()
buttonR = tk.Button(coordenadas, text = 'reset', command=reset,width = 25).pack(side='bottom') # Botón de reseteo
coordenadas.mainloop() # Ejecuto el programa