# Creación de las clases
class Vehiculo():
    def __init__(self,color,ruedas,puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
    def __str__(self):
        return f"El vehículo es de color {self.color}, tiene {self.ruedas} ruedas y {self.puertas} puertas."

class Coche(Vehiculo):
    def __init__(self,color,ruedas,puertas,velocidad,cilindrada):
        Vehiculo.__init__(self,color,ruedas,puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return Vehiculo.__str__(self) + f" Su velocidad máxima es de {self.velocidad} km/h y su cilindrada de {self.cilindrada} cc."
# Creo objeto
obj_mi_automóvil = Coche('rojo',4,2,180,1300)
print(obj_mi_automóvil)