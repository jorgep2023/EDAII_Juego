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
        print(f"\nBienvenido/a {self.nombre}, aquí sabrás, o no, tu próximo destino turístico.")
        
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
    ¡Enhorabuena! Has ganado la oportunidad de visitar un destino en España. ¡Sigue concursando por este destino!
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
    ¡Enhorabuena! Has ganado la oportunidad de visitar un destino en Italia. ¡Sigue concursando por este destino!
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
    ¡Enhorabuena! Has ganado la oportunidad de visitar un destino en México. ¡Sigue concursando por este destino!
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
        print("\n¡Bienvenido/a a la segunda fase! Ahora deberás resolver adivinanzas relacionadas con los destinos turísticos que has ganado.")

        paises_para_tercera_fase = []

        for pais in self.paises_acertados:
            adivinanza_usuario = input(f"\nAdivinanza para {pais}: {self.generar_adivinanza(pais)}\nTu respuesta: ")
            if self.verificar_adivinanza(pais, adivinanza_usuario):
                print(f"¡Correcto! Has acertado la adivinanza de {pais}. ¡Pasas a la tercera fase!")
                paises_para_tercera_fase.append(pais)
            else:
                print(f"Oh no, has fallado la adivinanza de {pais}. Mejor suerte la próxima vez.")

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


class TerceraFase:
    def __init__(self, ciudades_elegidas, nombre_viajero):
        self.ciudades_elegidas = ciudades_elegidas
        self.nombre_viajero = nombre_viajero

    def mostrar_info_ciudades(self):
        print("\n¡Felicidades por llegar a la fase final! Ahora, tendrás que elegir entre las siguientes ciudades:")
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
        print("\n¡Felicidades por llegar a la fase final en", self.ciudad_elegida + "! Ahora, tendrás que responder 3 preguntas sobre Ingeniería en Inteligencia Artificial.")
        print("Responde con 'si' o 'no'.\n")

        preguntas_ia = [
            "¿La IA es capaz de aprender por sí misma?",
            "¿La IA puede entender y procesar el lenguaje humano?",
            "¿La IA puede superar a los humanos en algunas tareas específicas?"
        ]

        respuestas_correctas_ia = ["si", "si", "si"]
        respuestas_usuario_ia = [input(f"{pregunta}\nTu respuesta: ").lower() for pregunta in preguntas_ia]

        if respuestas_usuario_ia == respuestas_correctas_ia:
            print("\n¡Enhorabuena! Has respondido correctamente las 3 preguntas sobre Ingeniería en Inteligencia Artificial.")
            print("\nTe presentamos tu billete de avión:\n")
            mostrar_billete_avion(self.nombre_viajero, self.ciudad_elegida)
            reproducir_cancion(canciones[self.ciudad_elegida], duracion=15)
        else:
            print("\nLo siento, has fallado en al menos una pregunta. El juego ha terminado. Mejor suerte la próxima vez.")


def mostrar_billete_avion(nombre_viajero, ciudad_destino):
    if ciudad_destino == "España":
        destino_ascii = """
Vuelo a España

                       __
                     /    \\
      ________|__|________
     |                                          |
     | Pasajero: {nombre_viajero}      |
     | Destino:   {ciudad_destino}       |
     |_________________________________|
"""
    elif ciudad_destino == "Italia":
        destino_ascii = """
Vuelo a Italia

                       __
                     /    \\
      ________|__|________
     |                                          |
     | Pasajero: {nombre_viajero}      |
     | Destino:   {ciudad_destino}        |
     |_________________________________|
"""
    elif ciudad_destino == "México":
        destino_ascii = """
Vuelo a México

                       __
                     /    \\
      ________|__|________
     |                                          |
     | Pasajero: {nombre_viajero}      |
     | Destino:   {ciudad_destino}       |
     |_________________________________|
"""
   

    print(destino_ascii)

class JuegoDestinos:
    def __init__(self):
        self.aciertos_por_pais = {}
        

    def reproducir_suspension_song(self):
        pygame.mixer.music.load("inicio_song.wav")
        pygame.mixer.music.play()
        time.sleep(2)
        pygame.mixer.music.stop()

  
    def adivinar_numero(self):
        numero_adivinanza = random.randint(1, 9)
        intentos = 3
        
        print("Bienvenido/a a Destined Chance, si ya has llegado hasta aquí, puede que tu próximo destino turístico esté más cerca de lo que te esperas.")
        print("En este juego, tendrás la oportunidad de ganar un viaje con todo incluido a destinos increíbles.")
        print("Si sabes algo de cultura general, seguro que ganas, pero ojo, también entra el azar y la suerte que te acompañe en el momento en el que lo intentes.")

        print("\nPrimero sabremos tu suerte, tienes 3 intentos para adivinar el número que la IA ha generado para ti (del 1 al 9):")

        while intentos > 0:
            try:
                intento_usuario = int(input("Por favor, teclea tu número: "))
            except ValueError:
                print("Por favor, ingresa un número válido.")
                continue

            if intento_usuario == numero_adivinanza:
                print("Genial, la suerte está de tu lado. Continuemos...")
                return True

            print("Lástima, la suerte no te acompaña, ¿otra vez?")
            intentos -= 1

        print("Lo siento, has agotado tus intentos y por lo visto, tu suerte.... Inténtalo de nuevo el próximo año.")
        return False


    




    def iniciar_juego(self):
        pygame.init()
        self.reproducir_suspension_song()  
        viajero = Viajero("")
        destinos = [
            DestinoTuristico("España", "La capital de España", ["¿Cuál es la capital de este país?", "¿Qué plato típico puedes encontrar aquí?", "¿En qué continente está este país?"], ["Madrid", "Paella", "Europa"]),
            DestinoTuristico("Italia", "La Ciudad Eterna", ["¿Cuál es la capital de este país?", "¿Qué famoso coliseo puedes visitar aquí?", "¿En qué continente está este país?"], ["Roma", "Coliseo", "Europa"]),
            DestinoTuristico("México", "La ciudad de la gente buena", ["¿Cuál es la capital de este país?", "¿Cuál es el evento más importante de esta ciudad?", "¿En qué continente está este país?"], ["Ciudad de México", "Feria de San Marcos", "América"]),
   
        ]

        if not self.adivinar_numero():
            return False

        viajero.obtener_nombre()
        viajero.inicio()

        self.aciertos_por_pais = {pais: 0 for pais in set(destino.pais for destino in destinos)}

        for destino in destinos:
            destino.mostrar_info_destino()
            respuestas_usuario = [input(f"Respuesta para '{pregunta}': ") for pregunta in destino.preguntas]
            aciertos = destino.hacer_preguntas(respuestas_usuario)

            print(f"Has acertado {aciertos} de {len(destino.preguntas)} preguntas.\n")

            if aciertos > 0:
                self.aciertos_por_pais[destino.pais] += 1
                mostrar_destino_ascii(destino.pais)
                print(f"\n¡Enhorabuena! Has ganado la oportunidad de visitar un destino en {destino.pais}. ¡Sigue concursando por este destino!")
                reproducir_cancion(canciones[destino.pais], duracion=15)
            else:
                mostrar_destino_ascii(destino.pais)
                print(f"\n¡Oh no! Has perdido la oportunidad de visitar un destino en {destino.pais}. Mejor suerte la próxima vez.")
                reproducir_cancion(canciones[destino.pais], duracion=15)

        paises_acertados = [pais for pais, aciertos in self.aciertos_por_pais.items() if aciertos >= 1]

        if paises_acertados:
            print("\n¡Felicidades! Has ganado la oportunidad de visitar los siguientes países:")
            for pais in paises_acertados:
                print(pais)
            print("\n¡Has pasado a la segunda fase con los destinos mencionados!")



        segunda_fase = SegundaFase(paises_acertados)
        paises_para_tercera_fase = segunda_fase.jugar_segunda_fase()

        if paises_para_tercera_fase:
            print("\n¡Felicidades! Has ganado la oportunidad de pasar a la tercera fase con los siguientes países:")
            for pais in paises_para_tercera_fase:
                print(pais)
            print("\n¡Buena suerte en la tercera fase!")

            if len(paises_para_tercera_fase) == 1:
                tercera_fase = TerceraFase(paises_para_tercera_fase[0], viajero.nombre)
                tercera_fase.realizar_preguntas_ia()
            else:
                tercera_fase = TerceraFase(paises_para_tercera_fase, viajero.nombre)
                tercera_fase.mostrar_info_ciudades()
                while not tercera_fase.elegir_ciudad():
                    pass  

                tercera_fase.realizar_preguntas_ia()

        else:
            print("\nPerdiste la oportunidad de visitar algunos destinos. ¡Pero no te preocupes, sigues concursando con el resto!")



        return paises_acertados


juego = JuegoDestinos()
juego.iniciar_juego()

tercera_fase = TerceraFase(paises_acertados, viajero.nombre)


if len(paises_acertados) == 1:
    tercera_fase.ciudad_elegida = paises_acertados[0]
    tercera_fase.realizar_preguntas_ia()
else:
    tercera_fase.mostrar_info_ciudades()
    while not tercera_fase.elegir_ciudad():
        pass  

    tercera_fase.realizar_preguntas_ia()