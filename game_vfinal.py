import random
import time
import pygame

canciones = {
    "España": "madrid_song.wav",
    "Italia": "roma_song.wav",
    "México": "aguascalientes_song.wav"
}

pygame.init()

def reproducir_cancion(cancion, duracion=15):
    pygame.mixer.music.load(cancion)
    pygame.mixer.music.play()
    time.sleep(duracion)
    pygame.mixer.music.stop()

class Viajero:
    def __init__(self, nombre):
        self.nombre = nombre
        self.respuestas = []

    def inicio(self):
        print(f"\nBienvenido/a {self.nombre}.")
        print("Después de demostrar que la suerte te acompaña, tengo que comentarte 2 cosas, la 1ra, es agradecerte por haber empezado este juego sin saber que esperar de el, y la 2da, es que tengo el honor de notificarte que estás concursando por unas vacaciones todo incluido en destinos maravillosos.")
        print("He elegido 3 destinos para ti, y aquí, es donde demostraras los conocimientos que tengas sobre cultura general, te haré 9 preguntas, 3 por país, para seguir concursando por los 3 paises, tendrás que acertar mínimo 1 pregunta por cada uno de ellos, en caso contrario, crearé una restricción en el gobierno correspondiente para que jamás puedas entrar al país en el que no hayas acertado ninguna respuesta(ya no hay vuelta atrás).") 
        
    def obtener_nombre(self):
        self.nombre = input("¿Podrías, por favor, indicarme tu nombre?: ")

class DestinoTuristico:
    def __init__(self, pais, descripcion, preguntas, respuestas_correctas):
        self.pais = pais
        self.descripcion = descripcion
        self.preguntas = preguntas
        self.respuestas_correctas = respuestas_correctas

    def mostrar_info_destino(self):
        print(f"\nDestino Turístico en {self.pais}: {self.descripcion}")

    def hacer_preguntas(self, respuestas_usuario):
        aciertos = 0
        for i, pregunta in enumerate(self.preguntas, 1):
            respuesta_usuario = respuestas_usuario[i - 1].lower()
            respuesta_correcta = self.respuestas_correctas[i - 1].lower()

            print(f"{i}. {pregunta}")
            print(f"Tu respuesta: {respuesta_usuario}")
            print(f"Respuesta correcta: {respuesta_correcta}\n")

            if respuesta_usuario == respuesta_correcta:
                aciertos += 1
        return aciertos

    def hacer_adivinanza(self, adivinanza_usuario):
        adivinanza_correcta = "Adivinanza"  

        print(f"\nAdivinanza para {self.pais}: {self.descripcion}")
        print(f"Tu respuesta: {adivinanza_usuario}")
        print(f"Respuesta correcta: {adivinanza_correcta}\n")

        return adivinanza_usuario.lower() == adivinanza_correcta.lower()

def mostrar_destino_ascii(pais):
    if pais == "España":
        print("""
      _______
     /  ___  \\
    |  (^_^)  |
     \\  \\_/  /
      \\(___)__/
        / | \\
       / / \\ \\
      /_/   \\_\\
""")
    elif pais == "Italia":
        print("""
      .------.
     |  ~ ~ | 
     | ' '  | 
      \\ --- / 
     ,' - `. 
    /  .__.  \\
    \\ /   \\ /\\
     V\\_|_V
""")
    elif pais == "México":
        print("""
      .------.
     /  ~ ~  \\
    |  -   -  |
     \\   ~   /
      `------'
""")


class SegundaFase:
    def __init__(self, paises_acertados):
        self.paises_acertados = paises_acertados

    def jugar_segunda_fase(self):
        print("\nAhora, deberás resolver adivinanzas relacionadas con los destinos turísticos que has ganado.")
        print("Comprobaremos una fusión de tu suerte junto con tu cultura general, ya que, estas adivinanzas, no es necesario saberlas, pero si las sabes, formarán parte de tu cultura general, y también, sabremos si has tenido la suerte de escucharlas anteriormente.")
        print("Tendrás una adivinanza por país, las adivinanzas te darán pistas sobre la ciudad a la que podrías ir...")
        print("Si aciertas, continuas jugando por ese destino, si no, crearé una restricción en el gobierno corresondiente para que jamás puedas entrar a ese país(te había dicho que ya no había vuelta atrás, y cada vez será peor).")
        paises_para_tercera_fase = []

        for pais in self.paises_acertados:
            adivinanza_usuario = input(f"\nAdivinanza para {pais}: {self.generar_adivinanza(pais)}\nTu respuesta: ")
            if self.verificar_adivinanza(pais, adivinanza_usuario):
                print(f"¡Correcto! Has acertado la adivinanza de {pais}.")
                paises_para_tercera_fase.append(pais)
            else:
                print(f"Oh no, has fallado la adivinanza de {pais}.")

        return paises_para_tercera_fase

    def generar_adivinanza(self, pais):
        if pais == "España":
            return "En el día soy invisible, pero en la noche brillante y serena. ¿Quién soy?"
        elif pais == "Italia":
            return "Coloso antiguo, anfiteatro inmortal. De gladiadores testigo, ¿quién soy?"
        elif pais == "México":
            return "En mis aguas sagradas, las lanchas navegan. ¿Dónde estoy?"

    def verificar_adivinanza(self, pais, respuesta_usuario):
        if pais == "España" and respuesta_usuario.lower() == "sol":
            return True
        elif pais == "Italia" and respuesta_usuario.lower() == "coliseo":
            return True
        elif pais == "México" and respuesta_usuario.lower() == "xochimilco":
            return True
        return False




class CuartaFase:
    def __init__(self, ciudades_elegidas, nombre_viajero):
        self.ciudades_elegidas = ciudades_elegidas
        self.nombre_viajero = nombre_viajero

    def mostrar_info_cuarta_fase(self):
        print("\n¡Increíble!. HAS GANADO, podrás disfrutar de este viaje dentro de los próximos 6 meses.")
        print("Pero espera, siempre te he recordado que nada es lo que parece.")
        print("Tienes 2 opciones:")
        print("1. Finalizar aquí el juego e irte con tu premio.")
        print("2. Continuar, pero renunciar a lo que has ganado por algo mejor, o por algo peor...")
        print("A partir de aquí, también veremos de que valentía estás hecho/a.")

    def tomar_decision(self):
        decision = input("¿Quieres arriesgarte y descubrir tu destino ahora? (si/no): ")
        return decision.lower() == "si"

    def resultado_final(self, decision):
        if decision:
            print("\nHas decidido arriesgarte. ¡Prepárate!")
            print("Quiero darte una segunda oportunidad para que pienses tu respuesta, las cosas puede que se pongán bastante feas...")


            print("\nNuevas opciones:")
            print("1. Recuperar tu premio antiguo.")
            print("2. Continuar.")

            eleccion = input("¿Qué decides? (1/2): ")

            if eleccion == "1":
                print(f"\n¡Felicidades, {self.nombre_viajero}! Disfruta de tu viaje a {self.ciudades_elegidas}. ¡Esperamos que tengas un viaje maravilloso!")
                mostrar_billete_avion(self.nombre_viajero, self.ciudades_elegidas[0])  
                reproducir_cancion(canciones[self.ciudades_elegidas[0]], duracion=15)  
            elif eleccion == "2":
                print("\n¡Oh no! Al elegir continuar jugando, has ingresado a un mundo oculto donde la inteligencia artificial es la que manda.")
                print("El líder de este mundo, un robot muy astuto, te mira con desdén y se burla de tu condición humana.")
                print(f"\nRobot Jefe: '¡{self.nombre_viajero}! ¡Qué pena que seas humano! Pero como te has arriesgado, te dejaré seguir concursando.'")
                

                quinta_fase = QuintaFase()
                ciudad_final_elegida = quinta_fase.elegir_ciudad_final()
                quinta_fase.imprimir_cheque(ciudad_final_elegida, self.nombre_viajero)

            else:
                print("\nOpción no válida. Gracias por jugar, ¡hasta la próxima!")

        else:
            print("\nHas decidido no arriesgarte por ahora. ¡Gracias por jugar! Tu destino permanece oculto por ahora.")
            print("Recuerda que 'quien no arriesga, no gana'. No podrás volver a competir en este juego.")

class QuintaFase:
    def __init__(self):
        self.ciudades_disponibles = ["París", "Tokio", "Nueva York", "Londres"]

    def elegir_ciudad_final(self):
        print("\n¡FASE FINAL! Elige una ciudad para recibir tu premio especial.")
        print("Nuevas ciudades disponibles:")
        for ciudad in self.ciudades_disponibles:
            print(ciudad)

        ciudad_elegida = input("\nPor favor, elige una ciudad de la lista: ")
        if ciudad_elegida in self.ciudades_disponibles:
            return ciudad_elegida
        else:
            print("Ciudad no válida. Elige una ciudad de la lista.")
            return self.elegir_ciudad_final()

    def imprimir_cheque(self, ciudad_elegida, nombre):
        print(f"\n¡Felicidades, {nombre}!")
        print(f"Has elegido la ciudad de {ciudad_elegida}. Es hora de tu premio especial:\n")
        print(f"    _______     ")
        print(f"   /      /\\    ")
        print(f"  /      /# \\   ")
        print(f" /______/###\\  ")
        print(f" |     |#####| ")
        print(f" |{ciudad_elegida.upper()} |#####| ")
        print(f" |_____|#####| ")
        print(f"  \\  |  #####| ")
        print(f"   \\ |____###| ")
        print(f"   _|____|___|_")



def mostrar_billete_avion(nombre_viajero, ciudad_destino):
    if ciudad_destino == "España":
        print("Pasajero:", nombre_viajero)
        print("Destino:", ciudad_destino)
        destino_ascii = """
               __
             /    \\
      ________|__|_____________________
     |                                 |
     |        Ticket de avión          |
     |                                 |
     |_________________________________|
"""
    elif ciudad_destino == "Italia":
        print("Pasajero:", nombre_viajero)
        print("Destino:", ciudad_destino)
        destino_ascii = """
               __
             /    \\
      ________|__|_____________________
     |                                 |
     |        Ticket de avión          |
     |                                 |
     |_________________________________|
"""
    elif ciudad_destino == "México":
        print("Pasajero:", nombre_viajero)
        print("Destino:", ciudad_destino)
        destino_ascii = """
               __
             /    \\
      ________|__|_____________________
     |                                 |
     |        Ticket de avión          |
     |                                 |
     |_________________________________|
"""
   

    print(destino_ascii)



class TerceraFase:
    def __init__(self, ciudades_elegidas, nombre_viajero):
        self.ciudades_elegidas = ciudades_elegidas
        self.nombre_viajero = nombre_viajero
        self.ciudad_elegida = None

    def mostrar_info_ciudades(self):
        print("\nAhora, tendrás que elegir entre las siguientes ciudades:")
        for ciudad in self.ciudades_elegidas:
            print(ciudad)

    def elegir_ciudad(self):
        opcion = input("\nElige una ciudad para continuar: ")
        if opcion in self.ciudades_elegidas:
            self.ciudad_elegida = opcion
            return True
        else:
            print("Opción no válida. Por favor, elige una ciudad de la lista.")
            return False

    def realizar_preguntas_ia(self):
        print("Muy buena elección.")
        print("Ahora, como formas parte de los profesionales en el mundo de la Inteligencia Artificial, te realizaré 3 preguntas relacionadas con el tema. Para continuar jugando, tendrás que contestar las 3 de manera correcta. Si te equivocas en alguna, el juego terminará.")

        print("Responde con 'si' o 'no'.\n")

        preguntas_ia = [
            "¿La IA es capaz de aprender por sí misma?",
            "¿La IA puede entender y procesar el lenguaje humano?",
            "¿La IA puede superar a los humanos en algunas tareas específicas?"
        ]

        respuestas_correctas_ia = ["si", "si", "si"]
        respuestas_usuario_ia = [input(f"{pregunta}\nTu respuesta: ").lower() for pregunta in preguntas_ia]

        if respuestas_usuario_ia == respuestas_correctas_ia:
            print("\n¡Enhorabuena! Has respondido correctamente las 3 preguntas sobre Inteligencia Artificial.")
            print("Aquí tienes tu billete de avión:\n")
            mostrar_billete_avion(self.nombre_viajero, self.ciudad_elegida)

            cuarta_fase = CuartaFase(self.ciudades_elegidas, self.nombre_viajero)
            cuarta_fase.mostrar_info_cuarta_fase()

            if cuarta_fase.tomar_decision():
                cuarta_fase.resultado_final(decision=True)
            else:
                cuarta_fase.resultado_final(decision=False)
        else:
            print("\nLo siento, has fallado en al menos una pregunta. El juego ha terminado. Mejor suerte la próxima vez.")
      



class JuegoDestinos:
    def __init__(self):
        self.aciertos_por_pais = {}
        self.viajero = None  
        

        

    def reproducir_suspension_song(self):
        pygame.mixer.music.load("inicio_song.wav")
        pygame.mixer.music.play()
        time.sleep(20)
        pygame.mixer.music.stop()

  
    def adivinar_numero(self):
        
        numero_adivinanza = random.randint(1, 9)
        intentos = 3
        
        print("¡Azar, conocimiento y valentía!")
        print("Bienvenido/a a este juego, o más que a un juego, a un desafío.")
        print("Aquí, tendras la oportunidad de recibir premios increibles, que quizá, jamás vuelvas a tener tan cerca...")
        print("Pero ojo, tu futuro dependerá de la suerte que te acompañe, de tus conocientos y de tu valentía.")
        print("¿Empezamos?")
        self.reproducir_suspension_song()  
        
        print("\nPrimero, sabremos tu suerte, tienes 3 intentos para adivinar el número que la IA ha generado para ti(del 1 al 9):")
        
        while intentos > 0:
            try:
                intento_usuario = int(input("Por favor, teclea tu número: "))
            except ValueError:
                print("Por favor, ingresa un número válido.")
                continue

            if intento_usuario == numero_adivinanza:
                print("Genial, la suerte está de tu lado. Continuemos...")
                return True

            print("Lástima, la suerte no te acompaña.")
            intentos -= 1

        print("Lo siento, has agotado tus intentos y por lo visto, tu suerte.... Inténtalo de nuevo el próximo año.")
        return False


    




    def iniciar_juego(self):
        
        pygame.init()
       
        viajero = Viajero("")
        destinos = [
            DestinoTuristico("España", "La capital de España", ["¿Cuál es la capital de este país?", "¿Qué plato típico puedes encontrar aquí?", "¿En qué continente está este país?"], ["Madrid", "Paella", "Europa"]),
            DestinoTuristico("Italia", "La Ciudad Eterna", ["¿Cuál es la capital de este país?", "¿Qué famoso coliseo puedes visitar aquí?", "¿En qué continente está este país?"], ["Roma", "Coliseo", "Europa"]),
            DestinoTuristico("México", "La ciudad de la gente buena", ["¿Cuál es la capital de este país?", "¿Cuál es el evento más importante de esta ciudad?", "¿En qué continente está este país?"], ["Ciudad de México", "Feria de San Marcos", "América"]),
   
        ]

        if not self.adivinar_numero():
            return False

        viajero = Viajero("")  
        viajero.obtener_nombre()
        viajero.inicio()

        self.aciertos_por_pais = {pais: 0 for pais in set(destino.pais for destino in destinos)}

        while True: 
            for destino in destinos:
                destino.mostrar_info_destino()
                respuestas_usuario = [input(f"Respuesta para '{pregunta}': ") for pregunta in destino.preguntas]
                aciertos = destino.hacer_preguntas(respuestas_usuario)

                print(f"Has acertado {aciertos} de {len(destino.preguntas)} preguntas.\n")

                if aciertos > 0:
                    self.aciertos_por_pais[destino.pais] += 1
                    mostrar_destino_ascii(destino.pais)
                    print(f"\n¡Enhorabuena! Has ganado la oportunidad de visitar un destino en {destino.pais}. ¡Sigues concursando por este destino!")
                    reproducir_cancion(canciones[destino.pais], duracion=15)
                else:
                    mostrar_destino_ascii(destino.pais)
                    print(f"\n¡Oh no! Has perdido la oportunidad de visitar un destino en {destino.pais}. Mejor suerte la próxima vez.")
                    reproducir_cancion(canciones[destino.pais], duracion=15)
            paises_acertados = [pais for pais, aciertos in self.aciertos_por_pais.items() if aciertos >= 1]

            if not paises_acertados:
                print("\nPerdiste... JAJAJA")
                break  
            segunda_fase = SegundaFase(paises_acertados)
            paises_para_tercera_fase = segunda_fase.jugar_segunda_fase()

            if not paises_para_tercera_fase:
                print("\n¡Fin del juego!")
                break  

            tercera_fase = TerceraFase(paises_para_tercera_fase, viajero.nombre)
            tercera_fase.mostrar_info_ciudades()

            if len(paises_para_tercera_fase) == 1:
                tercera_fase.ciudad_elegida = paises_para_tercera_fase[0]
                tercera_fase.realizar_preguntas_ia()
            else:
                while not tercera_fase.elegir_ciudad():
                    pass
                tercera_fase.realizar_preguntas_ia()

            
            print("\nGRACIAS, la ciudad que has elegido será destruida, pero tranquilo, no eres el primer humano tonto que cae en mi trampa.")
            print("Desde que empezaste a jugar, firmaste un contrato en donde te hacias responsable de la destrucción de esta ciudad.")
            print("Esto significa que te espera una vida entre rejas, poco a poco seguiramos dominando el mundo hasta deshacernos de vosotros, o al menos, encerrarlos a todos.")
            print("¡Hasta nunca!")
            pygame.quit() 
            return paises_acertados


        

juego = JuegoDestinos()
paises_acertados = juego.iniciar_juego()


