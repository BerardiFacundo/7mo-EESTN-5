# Creamos un diccionario para registrar personas con su nombre, edad y correo
personas = {
    "Juan": {"edad": 20, "correo": "juan@gmail.com"},
    "Ana": {"edad": 17, "correo": "ana@gmail.com"},
    "Carlos": {"edad": 25, "correo": "carlos@gmail.com"}
}

# Función que filtra a las personas mayores de 18 años
def filtrar_mayores(personas):
    mayores = {nombre: info for nombre, info in personas.items() if info["edad"] >= 18}
    return mayores

# Obtenemos las personas mayores de 18 años
mayores_de_edad = filtrar_mayores(personas)
print("Personas mayores de 18 años:")
for nombre, info in mayores_de_edad.items():
    print(f"{nombre} - Edad: {info['edad']}, Correo: {info['correo']}")
