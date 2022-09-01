from functools import reduce
def mifuncion(lista):
    int_impares = list(filter((lambda x: x % 2), lista))
    print(int_impares)
    int_impares = reduce((lambda x,y: x + y), int_impares)
    print(int_impares)
list_lista = list(range(100))
mifuncion(list_lista)