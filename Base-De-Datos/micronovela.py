import random

def bosque():
    print("Te encuentras en un bosque oscuro y misterioso. La niebla cubre el suelo, y los árboles susurran al viento.")
    print("De repente llegas a una bifurcación en el camino.")
    eleccion1 = input("¿Quieres ir a la izquierda o a la derecha? (izquierda/derecha): ").lower()

    if eleccion1 == "izquierda":
        print("\nCaminas hacia la izquierda, adentrándote más en el bosque.")
        print("Escuchas un crujido detrás de ti, y cuando te giras, ves una sombra moviéndose entre los árboles.")
        eleccion2 = input("¿Quieres seguir la sombra o correr en dirección opuesta? (seguir/correr): ").lower()

        if eleccion2 == "seguir":
            print("\nSigues a la sombra, moviéndote rápidamente entre los árboles.")
            print("La sombra te lleva a una cueva oculta en el bosque. Dentro, encuentras un cofre lleno de oro.")
            eleccion3 = input("¿Quieres abrir el cofre o salir de la cueva? (abrir/salir): ").lower()

            if eleccion3 == "abrir":
                print("\nAbres el cofre y encuentras un tesoro antiguo. Eres rico, pero la sombra nunca te dejará en paz.")
                print("FIN: Riqueza maldita.")
            else:
                print("\nDecides no abrir el cofre y sales de la cueva. Vuelves al bosque, sano y salvo, pero con la sensación de haber perdido algo.")
                print("FIN: Escapaste de la sombra.")
        else:
            print("\nCorres en dirección opuesta, alejándote de la sombra. De repente, encuentras una salida del bosque.")
            print("FIN: Has escapado del bosque oscuro.")
    
    elif eleccion1 == "derecha":
        print("\nVas hacia la derecha, el camino parece más tranquilo.")
        print("De repente, ves una cabaña vieja y destartalada en el claro del bosque.")
        eleccion2 = input("¿Quieres entrar a la cabaña o seguir caminando? (entrar/seguir): ").lower()

        if eleccion2 == "entrar":
            print("\nEntras en la cabaña. Todo está en silencio. Encuentras un libro antiguo sobre la mesa.")
            eleccion3 = input("¿Quieres leer el libro o dejarlo? (leer/dejar): ").lower()

            if eleccion3 == "leer":
                print("\nLees el libro y te das cuenta de que es un grimorio antiguo. Despiertas un poder oscuro y el bosque empieza a temblar. Te sangran los ojos y un antiguo sentimiento de odio y maldad empieza a surgir.")
                print("FIN: Has liberado una maldición, que te carcome cada día más.")
            else:
                print("\nDecides no tocar el libro y salir rápidamente de la cabaña. Escuchas un susurro en el viento.")
                eleccion4 = input("¿Quieres darte vuelta o huir? (girarte/huir): ").lower()

                if eleccion4 == "girarte":
                    print("\nTe das vuelta y ves una figura oscura que desaparece en la niebla. El susurro cesa, y el bosque queda en silencio, poco a poco empiezas a perder tu cordura.")
                    print("FIN: Has sido capturado por la presencia y te volviste loco.")
                elif eleccion4 == "huir":
                    print("\nDecides correr tan rápido como puedes, huyendo de la cabaña.")
                    numero_aleatorio = random.randint(1, 21)
                    print(f"Generas un número aleatorio: {numero_aleatorio}")
                    
                    if numero_aleatorio > 10:
                        print("¡Logras escapar exitosamente del bosque!")
                        print("FIN: Has escapado con vida.")
                    else:
                        print("Tropiezas mientras corres y la sombra te alcanza. Sientes su frío abrazo mientras tu vida se apaga.")
                        print("FIN: Has muerto en el bosque.")
        else:
            print("\nSigues caminando por el bosque y finalmente llegas a un pequeño lago. El agua es cristalina y pacífica.")
            print("FIN: Has encontrado un lugar tranquilo en el bosque, ya puedes descansar.")
    else:
        print("\nNo has tomado una decisión válida, y te quedas parado en medio del bosque hasta que anochece.")
        print("FIN: El bosque te atrapa para siempre.")

bosque()
