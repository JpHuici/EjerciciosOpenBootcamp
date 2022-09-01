#Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.
def esbisiesto():
  int_year= int(input("Introduce un año:"))

  if(int_year % 4 == 0 and (int_year % 100 != 0 or int_year % 400 == 0)):
      print(f"El año {int_year} es bisiesto")
  else:
      print(f"El año {int_year} no es bisiesto")
# Llamo a la función
esbisiesto()
