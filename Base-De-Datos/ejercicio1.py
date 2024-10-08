# Creamos una lista de estudiantes con su edad
estudiantes = [
    {"nombre": "Pedro", "edad": 16},
    {"nombre": "María", "edad": 18},
    {"nombre": "Juan", "edad": 15},
    {"nombre": "Ana", "edad": 20},
    {"nombre": "Carlos", "edad": 17}
]

# Función que encuentra al estudiante con mayor y menor edad
def encontrar_mayor_menor(estudiantes):
    # Usamos la función min y max con una clave que indique la edad
    estudiante_menor = min(estudiantes, key=lambda x: x["edad"])
    estudiante_mayor = max(estudiantes, key=lambda x: x["edad"])
    return estudiante_menor, estudiante_mayor

# Obtenemos los estudiantes con mayor y menor edad
menor, mayor = encontrar_mayor_menor(estudiantes)

print(f"El estudiante con menor edad es: {menor['nombre']} con {menor['edad']} años.")
print(f"El estudiante con mayor edad es: {mayor['nombre']} con {mayor['edad']} años.")
