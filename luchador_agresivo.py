import random
from luchador import Luchador

class Luchador_Agresivo (Luchador):

    def __init__(self, nombre, tipo,  vida, fuerza, resistencia, agilidad):
        super().__init__(nombre, vida, fuerza, resistencia, agilidad)
        self.tipo = tipo 
        

    def preparar (self):
        self.vida = self.vida + random.randint (0, 20)
        self.fuerza = self.fuerza + random.randint (0, 50)
        self.resistencia = self.resistencia + random.randint (0, 10)
        self.agilidad = self.agilidad + random.randint (0, 30)

        return self.vida, self.fuerza, self.resistencia, self.agilidad