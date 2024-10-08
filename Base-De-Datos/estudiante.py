# Registro de estudiantes
estudiantes = [
    {'nombre': 'Luca', 'apellido': 'Lopez', 'apodo': 'xluca', 'especialidad': 'Informática', 'edad': 19, 'dato_random': 'Gamer'},
    {'nombre': 'Nataly', 'apellido': 'Sado', 'apodo': 'Negra', 'especialidad': 'Sacarse los piojos', 'edad': 19, 'dato_random': 'Hace uñas'},
    {'nombre': 'Alan', 'apellido': 'Barbé', 'apodo': 'Gordo', 'especialidad': 'Dormir', 'edad': 18, 'dato_random': 'Es autista (le gustan los autos)'},
    {'nombre': 'Camila', 'apellido': 'Ricardo', 'apodo': 'Minion', 'especialidad': 'Chismear', 'edad': 18, 'dato_random': 'Anda en moto'},
    {'nombre': 'Tomas', 'apellido': 'Di Mauro', 'apodo': 'Frenton', 'especialidad': 'Informatica', 'edad': 19, 'dato_random': 'Adicto al trabajo'},
    {'nombre': 'Juan', 'apellido': 'Fidanza', 'apodo': 'Lamas', 'especialidad': 'Politica e historia', 'edad': 19, 'dato_random': 'Fan de Rosas'},
    {'nombre': 'Matias', 'apellido': 'Celiz', 'apodo': 'Celizin', 'especialidad': 'Jugar lol', 'edad': 19, 'dato_random': 'Adicto al lol'},
    {'nombre': 'Thiago', 'apellido': 'Almiron', 'apodo': 'Type', 'especialidad': 'Rascarse el higo', 'edad': 19, 'dato_random': 'Es de river'},
    {'nombre': 'Alan', 'apellido': 'Cordoba', 'apodo': 'Alita', 'especialidad': 'Programar', 'edad': 19, 'dato_random': 'Programa y juega al lol (hace bien ambas cosas)'},
    {'nombre': 'Facundo', 'apellido': 'Berardi', 'apodo': 'Fakita', 'especialidad': 'Programación', 'edad': 18, 'dato_random': 'Hace bjj y es un crack (Se merece un 10 en la materia)'}
]
# Función para agregar un estudiante
def agregar_estudiante(nombre, apellido, apodo, especialidad, edad, dato_random):
    estudiante = {
        'nombre': nombre,
        'apellido': apellido,
        'apodo': apodo,
        'especialidad': especialidad,
        'edad': edad,
        'dato_random': dato_random  # Campo donde el usuario ingresa un dato aleatorio
    }
    estudiantes.append(estudiante)
    print(f"Estudiante {nombre} {apellido} agregado con éxito.")

# Función para listar todos los estudiantes
def listar_estudiantes():
    if estudiantes:
        for i, estudiante in enumerate(estudiantes, 1):
            print(f"{i}. Nombre: {estudiante['nombre']} {estudiante['apellido']}, Apodo: {estudiante['apodo']}, Especialidad: {estudiante['especialidad']}, Edad: {estudiante['edad']}, Dato Random: {estudiante['dato_random']}")
    else:
        print("No hay estudiantes en el registro.")

# Función para actualizar la información de un estudiante
def actualizar_estudiante(apodo, nueva_edad=None, nueva_especialidad=None, nuevo_dato_random=None):
    for estudiante in estudiantes:
        if estudiante['apodo'] == apodo:
            if nueva_edad:
                estudiante['edad'] = nueva_edad
                print(f"Edad de {apodo} actualizada a {nueva_edad}.")
            if nueva_especialidad:
                estudiante['especialidad'] = nueva_especialidad
                print(f"Especialidad de {apodo} actualizada a {nueva_especialidad}.")
            if nuevo_dato_random:
                estudiante['dato_random'] = nuevo_dato_random
                print(f"Dato random de {apodo} actualizado a {nuevo_dato_random}.")
            return
    print(f"Estudiante con apodo {apodo} no encontrado.")

# Función para eliminar un estudiante
def eliminar_estudiante(apodo):
    for estudiante in estudiantes:
        if estudiante['apodo'] == apodo:
            estudiantes.remove(estudiante)
            print(f"Estudiante con apodo {apodo} eliminado con éxito.")
            return
    print(f"Estudiante con apodo {apodo} no encontrado.")

# Menú de opciones
def menu():
    while True:
        print("\n--- Menú de Opciones ---")
        print("1. Agregar estudiante")
        print("2. Listar estudiantes")
        print("3. Actualizar estudiante")
        print("4. Eliminar estudiante")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            apodo = input("Apodo: ")
            especialidad = input("Especialidad: ")
            edad = int(input("Edad: "))
            dato_random = input("Dato random: ")  # El usuario ingresa cualquier valor aquí
            agregar_estudiante(nombre, apellido, apodo, especialidad, edad, dato_random)
        
        elif opcion == '2':
            listar_estudiantes()
        
        elif opcion == '3':
            apodo = input("Apodo del estudiante a actualizar: ")
            nueva_edad = input("Nueva edad (dejar vacío para no actualizar): ")
            nueva_especialidad = input("Nueva especialidad (dejar vacío para no actualizar): ")
            nuevo_dato_random = input("Nuevo dato random (dejar vacío para no actualizar): ")
            actualizar_estudiante(apodo, int(nueva_edad) if nueva_edad else None, nueva_especialidad if nueva_especialidad else None, nuevo_dato_random if nuevo_dato_random else None)
        
        elif opcion == '4':
            apodo = input("Apodo del estudiante a eliminar: ")
            eliminar_estudiante(apodo)
        
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida, intenta de nuevo.")

# Ejecutar el programa
menu()
