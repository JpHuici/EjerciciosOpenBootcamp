# inicializamos la clase
class Alumno:
# Atributos
    def inicializar(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
# Imprimo datos sobre el alumno 
    def imprimir(self):
               print("Nombre: ",self.nombre)
               print("Nota: ",self.nota)

# El alumno aprobará la materia si su nota es mayor o igual a 4 
    def resultado(self):
        if self.nota >= 4:
            print("El alumno aprueba la materia.")
        else:
            print("El alumno repueba la materia.")
        
# Objetos
obj_alumno1=Alumno()
obj_alumno2=Alumno()
 
# Atributos
obj_alumno1.inicializar("Juan",3)
obj_alumno2.inicializar("Sofía",8)
 
# Datos y Resultados de cada alumno
obj_alumno1.imprimir()
obj_alumno1.resultado()
obj_alumno2.imprimir()
obj_alumno2.resultado()