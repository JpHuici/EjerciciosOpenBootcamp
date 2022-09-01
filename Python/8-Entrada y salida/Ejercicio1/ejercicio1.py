#En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.
f = open('archivotext.txt', 'w')
f.write('Escribo dentro del archivo\n')
f.close()

f = open('archivotext.txt','r+')
f.readline()
f.write('Vuelvo a escribir en el archivo.\n')
f.seek(0)
print(f.read())
f.close()
