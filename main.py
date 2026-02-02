from luchador import Luchador
import random

ninja = Luchador ("Hattori", "agilidad", 100, 30, 30, 30)

tercio = Luchador ("Santiago", "fuerza", 100, 30, 30, 30 )

ninja.preparar
tercio.preparar

if __name__ == "__main__":

    turno = 1

    while ninja.vida > 0 & tercio.vida > 0:
        if ninja.iniciativa > tercio.iniciativa:
            ninja.atacar
            tercio.defender
            print (f"Turno {turno}")
            print (f"{ninja.nombre} ataca a {tercio.nombre} cuya vida restante es {tercio.lifeLost} ")
            turno =+ 1
        else:
            tercio.atacar
            ninja.defender
            print (f"Turno {turno}")
            print (f"{tercio.nombre} ataca a {ninja.nombre} cuya vida restante es {ninja.lifeLost} ")
            turno =+ 1

    if ninja.vida <= 0:
        print (f"¡{ninja.nombre} ha sido derrotado, {tercio.nombre} gana!")

    if tercio.vida <= 0:
        print (f"¡{tercio.nombre} ha sido derrotado, {ninja.nombre} gana!")