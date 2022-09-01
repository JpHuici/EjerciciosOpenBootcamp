#Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros y otra función que calcule el área de un círculo recibiendo el radio del mismo.
import math
def areaT(): # Área del triángulo : (base * altura) / 2
# Declaración de variables
    float_altura = float(input("Coloque la altura del triángulo: "))
    float_base = float(input("Coloque la base del triángulo: "))
    float_area_triangulo = float((float_base * float_altura) / 2)
    print("El área del triángulo es de: %1.2f" %(float_area_triangulo) )

def areaC(): # Área del círculo : pi * (radio **2)
    float_radio = float(input("Coloque el radio del círculo: ")) #Declaración de la variable
    float_area_circulo = float(math.pi * float_radio ** 2)
    print("El área del circulo es de: %1.2f" %(float_area_circulo))
# Invoco las funciones    
areaT()
areaC()