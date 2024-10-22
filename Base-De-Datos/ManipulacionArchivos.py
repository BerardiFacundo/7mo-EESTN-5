# Ejercicio 1: Crear y leer un archivo de texto

# 1. Crear el archivo en modo escritura
with open("mi_archivo.txt", "w") as archivo:
    # 2. Escribir la frase en el archivo
    archivo.write("Hola, estoy aprendiendo Python")

# 3. Abrir el archivo en modo lectura
with open("mi_archivo.txt", "r") as archivo:
    # 5. Leer el contenido y mostrarlo en pantalla
    contenido = archivo.read()
    print(contenido)
