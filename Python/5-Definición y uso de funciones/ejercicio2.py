#Escribe una función que pueda decirte si un número (número entero) es primo o no.
def numero_primo():
# Declaracion de variables
  int_numero= int(input('Ingresa un número entero: '))
  
  if int_numero > 1:
    for i in range(2,int(int_numero)): # Evalua el rango de números enteros desde 2 hasta (int_numero - 1)
        if (int(int_numero) % i) == 0:
            print(f"El número {int_numero} no es primo, es divisible por {i}.")
            break
        else:
            print(f"El número {int_numero} es primo.")
            break
  else:
    print("El número ingresado no es primo, los números primos son mayores que 1.")
#Llamo a la función
numero_primo()