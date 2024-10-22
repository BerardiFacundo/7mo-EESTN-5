import sqlite3

# Ejercicio 3: Crear base de datos y tabla de alumnos

# 1. Conectar o crear la base de datos
conexion = sqlite3.connect("escuela.db")

# 2. Crear un cursor para ejecutar comandos SQL
cursor = conexion.cursor()

# 3. Crear la tabla 'alumnos' con columnas id, nombre, y curso
cursor.execute("""
CREATE TABLE IF NOT EXISTS alumnos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    curso TEXT NOT NULL
)
""")

# 4. Insertar 3 alumnos
cursor.execute("INSERT INTO alumnos (nombre, curso) VALUES ('Juan', 'Matemáticas')")
cursor.execute("INSERT INTO alumnos (nombre, curso) VALUES ('Ana', 'Física')")
cursor.execute("INSERT INTO alumnos (nombre, curso) VALUES ('Pedro', 'Programación')")

conexion.commit()

conexion.close()
