import random

# Clase para Personajes
class Personaje:
    def __init__(self, nombre, mana, vida, armadura, velocidad, ataque, ataque_especial, nombre_ataque, nombre_ataque_especial):
        self.nombre = nombre
        self.mana = mana
        self.vida = vida
        self.armadura = armadura
        self.velocidad = velocidad
        self.ataque = ataque
        self.ataque_especial = ataque_especial
        self.nombre_ataque = nombre_ataque
        self.nombre_ataque_especial = nombre_ataque_especial

    def mostrar_estadisticas(self):
        print(f"{self.nombre}: Mana: {self.mana}, Vida: {self.vida}, Armadura: {self.armadura}, Velocidad: {self.velocidad}, Ataque: {self.ataque}, Ataque especial: {self.ataque_especial}")

    def atacar(self, enemigo, especial=False):
        if especial and self.mana >= 20:
            dano = self.ataque_especial - enemigo.vida
            self.mana -= 20
            print(f"{self.nombre} usa su {self.nombre_ataque_especial} y causa {self.ataque_especial} de daño.")
        else:
            dano = self.ataque - enemigo.vida
            print(f"{self.nombre} usa su {self.nombre_ataque} y causa {self.ataque} de daño.")

        enemigo.vida -= max(dano, 0)

        if enemigo.vida <= 0:
            print(f"¡Has derrotado al {enemigo.nombre}!")
        else:
            print(f"El {enemigo.nombre} tiene {enemigo.vida} de vida restante.")

# Clase para Enemigos
class Enemigo:
    def __init__(self, nombre, vida, ataque, ataque_especial, nombre_ataque, nombre_ataque_especial):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.ataque_especial = ataque_especial
        self.nombre_ataque = nombre_ataque
        self.nombre_ataque_especial = nombre_ataque_especial

    def atacar(self, personaje):
        if random.randint(1, 10) > 7:  # Probabilidad de activar el ataque especial
            dano = self.ataque_especial - personaje.armadura
            print(f"{self.nombre} usa su {self.nombre_ataque_especial} y causa {self.ataque_especial} de daño.")
        else:
            dano = self.ataque - personaje.armadura
            print(f"{self.nombre} usa su {self.nombre_ataque} y causa {self.ataque} de daño.")

        personaje.vida -= max(dano, 0)
        
        if personaje.vida <= 0:
            print(f"{personaje.nombre} ha sido derrotado.")
        else:
            print(f"{personaje.nombre} tiene {personaje.vida} de vida restante.")

# Crear Personajes
def seleccionar_personaje():
    print("Selecciona tu personaje:")
    print("1. Mago\n2. Arquero\n3. Guerrero\n4. Esqueleto")
    eleccion = input("Elige un número: ")

    # Definir los personajes con nombres de ataques
    mago = Personaje("Mago", 100, 1000, 10, 1.75, 50, 100, "Bola de Fuego", "Explosión Arcana")
    arquero = Personaje("Arquero", 50, 1500, 25, 2.00, 75, 150, "Flecha Veloz", "Lluvia de Flechas")
    guerrero = Personaje("Guerrero", 0, 3000, 100, 1.25, 100, 200, "Espadazo", "Golpe Brutal")
    esqueleto = Personaje("Esqueleto", 20, 1500, 50, 1.50, 60, 120, "Mandoble", "Maldición Oscura")

    if eleccion == "1":
        return mago
    elif eleccion == "2":
        return arquero
    elif eleccion == "3":
        return guerrero
    elif eleccion == "4":
        return esqueleto
    else:
        print("Opción no válida. Se selecciona Guerrero por defecto.")
        return guerrero

# Batalla en la Mazmorra
def entrar_mazmorra(personaje):
    # Enfrentamientos aleatorios según lo especificado
    enemigos_comunes = [
        Enemigo("Slime", 50, 10, 20, "Golpe Baboso", "Desbordamiento Ácido"),
        Enemigo("Mimic", 100, 25, 40, "Mordida", "Aplastamiento")
    ]
    
    enemigos_raros = [
        Enemigo("Dragón", 200, 50, 100, "Llamarada", "Aliento de Fuego"),
        Enemigo("Orco", 500, 200, 400, "Mazazo", "Martillazo Aplastante"),
        Enemigo("BOSS -Rey Mago-", 1000, 400, 800, "Rayo Oscuro", "Tormenta Arcana")
    ]

    probabilidad = random.randint(1, 21)
    
    if probabilidad > 16:
        enemigo = random.choice(enemigos_raros) if probabilidad >= 20 else random.choice(enemigos_raros[:-1])
    else:
        enemigo = random.choice(enemigos_comunes)

    print(f"\nTe encuentras con un {enemigo.nombre}. ¡Prepárate para luchar!")

    # Batalla por turnos
    while enemigo.vida > 0 and personaje.vida > 0:
        print("\n--- Tu turno ---")
        accion = input("¿Qué quieres hacer? (atacar/ataque especial/huir): ").lower()
        
        if accion == "atacar":
            personaje.atacar(enemigo)
        elif accion == "ataque especial":
            if personaje.mana >= 20:
                personaje.atacar(enemigo, especial=True)
            else:
                print(f"{personaje.nombre} no tiene suficiente mana para un ataque especial.")
                continue  # El turno del personaje no avanza si no tiene mana suficiente
        elif accion == "huir":
            print("Intentas huir de la batalla...")
            if random.randint(1, 10) > 5:
                print("¡Has logrado huir!")
                break
            else:
                print("No logras escapar. ¡El enemigo te ataca!")
        else:
            print("Opción no válida. El enemigo aprovecha para atacar.")
        
        if enemigo.vida > 0:
            print("\n--- Turno del enemigo ---")
            enemigo.atacar(personaje)

# Iniciar el juego
def iniciar_juego():
    print("Bienvenido al juego de rol en el mundo de fantasía.")
    personaje = seleccionar_personaje()
    personaje.mostrar_estadisticas()

    print("\nTe adentras en la mazmorra...")
    entrar_mazmorra(personaje)

iniciar_juego()
