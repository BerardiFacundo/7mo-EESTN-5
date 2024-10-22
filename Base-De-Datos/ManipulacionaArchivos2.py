# Ejercicio 2: Escribir y leer varias líneas

# 1. Crear el archivo en modo escritura
with open("notas.txt", "w") as archivo:
    # 2. Escribir tres líneas con información de materias favoritas
    archivo.write("Matemáticas\n")
    archivo.write("Física\n")
    archivo.write("Programación\n")

# 4. Abrir el archivo en modo lectura y mostrar cada línea
with open("notas.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())