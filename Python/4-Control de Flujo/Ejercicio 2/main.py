# Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.
# Variables
int_numero_inicial = int(input("Ingrese el número menor: "))
int_numero_final = int(input("Ingrese el número mayor: "))
print("Los números impares entre ambos son: ")
# Inicio programa
while int_numero_inicial <= int_numero_final:
    if int_numero_inicial %2 == 1:
        print(int_numero_inicial)
    int_numero_inicial += 1
# Fin programa