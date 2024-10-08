# Registro de empleados con 10 ejemplos
empleados = [
    {'nombre': 'Carlos', 'apellido': 'Pérez', 'puesto': 'Desarrollador', 'edad': 30, 'dato_random': 'Gamer'},
    {'nombre': 'Lucía', 'apellido': 'González', 'puesto': 'Ingeniera de Redes', 'edad': 35, 'dato_random': 'Toca guitarra'},
    {'nombre': 'Juan', 'apellido': 'Martínez', 'puesto': 'Analista de Datos', 'edad': 28, 'dato_random': 'Le gusta el fútbol'},
    {'nombre': 'María', 'apellido': 'Rodríguez', 'puesto': 'Química', 'edad': 32, 'dato_random': 'Aficionada al cine'},
    {'nombre': 'Ana', 'apellido': 'López', 'puesto': 'Biotecnóloga', 'edad': 29, 'dato_random': 'Habla tres idiomas'},
    {'nombre': 'Pedro', 'apellido': 'Hernández', 'puesto': 'Arquitecto', 'edad': 40, 'dato_random': 'Fan del baloncesto'},
    {'nombre': 'Sofía', 'apellido': 'Ramírez', 'puesto': 'Ingeniera Civil', 'edad': 36, 'dato_random': 'Le encanta leer'},
    {'nombre': 'Miguel', 'apellido': 'Jiménez', 'puesto': 'Diseñador Gráfico', 'edad': 27, 'dato_random': 'Aficionado al dibujo'},
    {'nombre': 'Laura', 'apellido': 'Ortiz', 'puesto': 'Administradora', 'edad': 33, 'dato_random': 'Escritora amateur'},
    {'nombre': 'Diego', 'apellido': 'Morales', 'puesto': 'Programador', 'edad': 31, 'dato_random': 'Corredor aficionado'}
]

# Función para agregar un empleado
def agregar_empleado(nombre, apellido, puesto, edad, dato_random):
    empleado = {
        'nombre': nombre,
        'apellido': apellido,
        'puesto': puesto,
        'edad': edad,
        'dato_random': dato_random  # Campo donde el usuario ingresa un dato aleatorio
    }
    empleados.append(empleado)
    print(f"Empleado {nombre} {apellido} agregado con éxito.")

# Función para listar todos los empleados
def listar_empleados():
    if empleados:
        for i, empleado in enumerate(empleados, 1):
            print(f"{i}. Nombre: {empleado['nombre']} {empleado['apellido']}, Puesto: {empleado['puesto']}, Edad: {empleado['edad']}, Dato Random: {empleado['dato_random']}")
    else:
        print("No hay empleados en el registro.")

# Función para actualizar la información de un empleado
def actualizar_empleado(nombre, nuevo_puesto=None, nueva_edad=None, nuevo_dato_random=None):
    for empleado in empleados:
        if empleado['nombre'] == nombre:
            if nuevo_puesto:
                empleado['puesto'] = nuevo_puesto
                print(f"Puesto de {nombre} actualizado a {nuevo_puesto}.")
            if nueva_edad:
                empleado['edad'] = nueva_edad
                print(f"Edad de {nombre} actualizada a {nueva_edad}.")
            if nuevo_dato_random:
                empleado['dato_random'] = nuevo_dato_random
                print(f"Dato random de {nombre} actualizado a {nuevo_dato_random}.")
            return
    print(f"Empleado con nombre {nombre} no encontrado.")

# Función para eliminar un empleado
def eliminar_empleado(nombre):
    for empleado in empleados:
        if empleado['nombre'] == nombre:
            empleados.remove(empleado)
            print(f"Empleado {nombre} eliminado con éxito.")
            return
    print(f"Empleado con nombre {nombre} no encontrado.")

# Menú de opciones
def menu():
    while True:
        print("\n--- Menú de Opciones ---")
        print("1. Agregar empleado")
        print("2. Listar empleados")
        print("3. Actualizar empleado")
        print("4. Eliminar empleado")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            puesto = input("Puesto: ")
            edad = int(input("Edad: "))
            dato_random = input("Dato random: ")  # El usuario ingresa cualquier valor aquí
            agregar_empleado(nombre, apellido, puesto, edad, dato_random)
        
        elif opcion == '2':
            listar_empleados()
        
        elif opcion == '3':
            nombre = input("Nombre del empleado a actualizar: ")
            nuevo_puesto = input("Nuevo puesto (dejar vacío para no actualizar): ")
            nueva_edad = input("Nueva edad (dejar vacío para no actualizar): ")
            nuevo_dato_random = input("Nuevo dato random (dejar vacío para no actualizar): ")
            actualizar_empleado(nombre, nuevo_puesto if nuevo_puesto else None, int(nueva_edad) if nueva_edad else None, nuevo_dato_random if nuevo_dato_random else None)
        
        elif opcion == '4':
            nombre = input("Nombre del empleado a eliminar: ")
            eliminar_empleado(nombre)
        
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida, intenta de nuevo.")

# Ejecutar el programa
menu()
