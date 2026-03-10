from random import randint

from PyQt6.QtWidgets import QApplication
import random

class ArticuloFaker:
    _descripciones = [
        "Martillo",
        "Destornillador plano",
        "Destornillador Phillips",
        "Llave inglesa",
        "Llave fija",
        "Llave Allen",
        "Alicates",
        "Alicates de punta",
        "Alicates de corte",
        "Taladro",
        "Broca para madera",
        "Broca para metal",
        "Broca para concreto",
        "Sierra manual",
        "Serrucho",
        "Cinta métrica",
        "Nivel de burbuja",
        "Escuadra",
        "Cutter",
        "Navaja multiusos",
        "Lija",
        "Lija para madera",
        "Lija para metal",
        "Clavos",
        "Tornillos",
        "Tarugos",
        "Arandelas",
        "Tuercas",
        "Pernos",
        "Bisagras",
        "Cerradura",
        "Candado",
        "Cadena",
        "Abrazaderas",
        "Silicona",
        "Pistola de silicona",
        "Pegamento de contacto",
        "Cinta aislante",
        "Cinta de teflón",
        "Extensión eléctrica",
        "Multímetro",
        "Soldador eléctrico",
        "Estaño para soldar",
        "Compresor de aire",
        "Pistola de aire",
        "Rodillo para pintar",
        "Brocha",
        "Espátula",
        "Paleta de albañil",
        "Carretilla"
    ]

    _observaciones = """Cuenta la leyenda que Skibidi Toilet nació en el baño de una discoteca a las 3:17 de la madrugada, justo cuando alguien dijo:
“Este baño tiene demasiado eco…”

En ese preciso instante, del inodoro emergió una cabeza cantando:

“Skibidi dop dop yes yes” 🎶

Y así empezó todo.

Infancia turbulenta

Desde pequeño, Skibidi Toilet tuvo una vida complicada.
Mientras otros inodoros soñaban con una vida tranquila en baños familiares, él quería dominar el mundo desde la fontanería.

Sus padres intentaron educarlo:

Su madre: “Hijo, deja de cantar en el baño.”

Su padre: “Y por favor, deja de asustar a los invitados.”

Pero ya era tarde. El destino estaba escrito… en la cisterna.

Juventud rebelde

Durante su adolescencia, Skibidi Toilet formó su primera banda musical:

“Los Desagües del Ritmo”

Su mayor éxito fue el single:

“Dop Dop en el WC”

La crítica musical dijo que era:

10% música

90% eco de baño público

Pero en internet fue un éxito.

La gran guerra del baño

Un día aparecieron sus enemigos mortales:

los Cameramen 📷

los Speakermen 🔊

los TV Men 📺

Nadie sabe exactamente por qué empezó la guerra.
Algunos historiadores creen que todo comenzó porque alguien olvidó tirar de la cadena.

Desde entonces, Skibidi Toilet lidera un ejército de sanitarios cantantes intentando conquistar el mundo.

Personalidad

Skibidi Toilet es conocido por ser:

Dramático 🎭

Muy ruidoso 🔊

Incapaz de cantar en tono normal

Y extremadamente orgulloso de su porcelana

Curiosidad histórica

Los científicos siguen investigando una gran pregunta:

¿Skibidi Toilet es un cantante atrapado en un inodoro…
o un inodoro que descubrió el karaoke?

Nadie lo sabe.

Pero lo que sí sabemos es que si alguna noche escuchas en el baño:

 Skibidi dop dop yes yes…

Tal vez…
no estés solo. 🚽👀"""
    @staticmethod
    def _generar_referencia():
        return random.randint(100000,9999999)

    @staticmethod
    def _generar_precio():
        return random.randint(100, 9999)

    @staticmethod
    def _generar_stock():
        return random.randint(100, 9999)
    @classmethod
    def _generar_descripciones(cls):
        return random.choice(cls._descripciones)

    @classmethod
    def _generar_observaciones(cls, num_palabras=15):
        palabras = cls._observaciones.split()
        return " ".join(random.sample(palabras, num_palabras))

    @classmethod
    def generar(cls):

        return {
            "referencia" : cls._generar_referencia(),
            "precio" : cls._generar_precio(),
            "stock" : cls._generar_stock(),
            "descripcion" : cls._generar_descripciones(),
            "observaciones" : cls._generar_observaciones(),
        }
    @classmethod
    def generar_lote(cls, n):
        return [cls.generar() for _ in range(n)]


if __name__ == '__main__':
    print(ArticuloFaker().generar())