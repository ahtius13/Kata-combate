from luchador_agresivo import Luchador_Agresivo
from luchador_defensivo import Luchador_Defensivo
from luchador_agil import Luchador_Agil
from luchador_boss import Luchador_Boss
import random


ninja = Luchador_Agil ("Hattori", "agilidad", 100, 30, 30, 30)

tercio = Luchador_Agresivo ("Santiago", "ataque", 100, 30, 30, 30 )

caballero = Luchador_Defensivo ("Reinhart", "defensa", 100, 30, 30, 30)

angel = Luchador_Boss ("Azrael", "boss", 100, 30, 30, 30)

contendientes = [ninja, tercio, caballero, angel]

#contendientes_random = contendientes[:]
#random.shuffle (contendientes_random)
#player1 = contendientes_random[0]
#player2 = contendientes_random[1]

player1, player2 = random.sample(contendientes, 2)


#player1 = random.choice(contendientes)

#player2 = random.choice(contendientes)


player1.preparar()

player2.preparar()

if __name__ == "__main__":
    
    print (f"{player1.nombre} vs {player2.nombre}")
    turno = 1

    player1Speed = player1.iniciativa()
    player2Speed = player2.iniciativa()
   
    while player1.vida > 0 and player2.vida > 0:
        print (f"Turno {turno}")
        if player1Speed > player2Speed:
          
            player2.lifeLost(player1)
            print (f"{player1.nombre} ataca a {player2.nombre} cuya vida restante es {player2.vida} ")
            
            
        else:
           
            player1.lifeLost(player2)
            print (f"{player2.nombre} ataca a {player1.nombre} cuya vida restante es {player1.vida} ")

        turno = turno + 1
        
            

    if player1.vida <= 0:
        print (f"¡{player1.nombre} ha sido derrotado, {player2.nombre} gana!")

    if player2.vida <= 0:
        print (f"¡{player2.nombre} ha sido derrotado, {player1.nombre} gana!")