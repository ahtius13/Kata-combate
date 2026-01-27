from luchador import Luchador
import random

ninja = Luchador ("Hattori", random.randrange (10,300,10),random.randrange (10,300,10), random.randrange (10,300,10), random.randrange (10,300,10) )

tercio = Luchador ("Santiago", random.randrange (10,300,10),random.randrange (10,300,10), random.randrange (10,300,10), random.randrange (10,300,10) )


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