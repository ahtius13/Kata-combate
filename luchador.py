import random

class Luchador:
    

    def __init__(self, nombre, vida, fuerza, resistencia, agilidad):

        self.nombre = nombre
        self.vida = int(vida)
        self.fuerza = int(fuerza)
        self.resistencia = int(resistencia)
        self.agilidad = int(agilidad)


    def atacar (self):
         dados = self.fuerza / 10
         i = 1
         dice = random.randit(1,10)
         while i <= dados:
            damage = 0 + dice
            i += 1
            dice = random.randit(1,10)
        
         return damage 

    def defender (self):
         dados = self.resistencia / 10
         i = 1
         dice = random.randit(1,10)
         while i <= dados:
            bloqueado = 0 + dice
            i += 1
            dice = random.randit(1,10)
            
         return bloqueado 
