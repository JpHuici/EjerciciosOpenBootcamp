import sqlite3
db_alumnos = sqlite3.connect('ejercicio1.db') # Ejecuto base de datos
als = db_alumnos.cursor()

als.execute("""CREATE TABLE IF NOT EXISTS Alumnos 
            (ID INT,
            Nombre TEXT,
            Apellido TEXT)""") # Datos de las columnas

# Alumnos
als.execute("INSERT INTO Alumnos VALUES ('1', 'Héctor', 'Parra')")
als.execute("INSERT INTO Alumnos VALUES ('2', 'Pablo', 'Rodriguez')")
als.execute("INSERT INTO Alumnos VALUES ('3', 'Juan', 'Hierro')")
als.execute("INSERT INTO Alumnos VALUES ('4', 'Sofía', 'Leis')")
als.execute("INSERT INTO Alumnos VALUES ('5', 'Camila', 'Fernandez')")
als.execute("INSERT INTO Alumnos VALUES ('6', 'Daniel', 'Cara')")
als.execute("INSERT INTO Alumnos VALUES ('7', 'Sofía', 'Perez')")
als.execute("INSERT INTO Alumnos VALUES ('8', 'Macarena', 'Parra')")
als.execute("INSERT INTO Alumnos VALUES ('9', 'Jorge', 'Cordone')")
als.execute("INSERT INTO Alumnos VALUES ('10', 'Pedro', 'Maso')")

db_alumnos.commit()
als.execute("SELECT * FROM Alumnos WHERE Nombre = 'Daniel'") # Se muestra por consola el alumno seleccionado

alumnos_lista = als.fetchall()
print(alumnos_lista)

db_alumnos.close() # Cierro base de datos