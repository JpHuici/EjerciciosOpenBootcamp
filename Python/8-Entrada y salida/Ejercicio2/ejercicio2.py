# En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo, haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.
from pickle import *

class Vehiculo:
    def __init__(self,color,ruedas,puertas,cilindrada,velocidad):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        self.cilindrada = cilindrada
        self.velocidad = velocidad
    
    def __str__(self):
        return "Ferrari color " + self.color +" con "+ self.ruedas +" ruedas, "+ self.puertas +" puertas y una cilindrada de "+ self.cilindrada +", su velocidad máxima es de "+ self.velocidad + "."

obj_ferrari = Vehiculo('roja', '4', '2', '3.9L', '340 km/h')
print(obj_ferrari)

file = open('objeto_ferrari', 'w+b')
dump(obj_ferrari, file)
file.seek(0)
nuevo_ferrari = load(file)

print(nuevo_ferrari)
file.close()