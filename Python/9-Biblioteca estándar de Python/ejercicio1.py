str_script = input("Ingrese los páises separados por comas: ")
list_lista = [pais for pais in str_script.split(" ")]
print(",".join(list(set(sorted (list_lista)))))

