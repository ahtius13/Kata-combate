import random
from luchador import Luchador

class Luchador_Boss (Luchador):

    def __init__(self, nombre, tipo,  vida, fuerza, resistencia, agilidad):
        super().__init__(nombre, vida, fuerza, resistencia, agilidad)
        self.tipo = tipo 
        

    def preparar (self):
        self.vida = self.vida + random.randint (0, 50)
        self.fuerza = self.fuerza + random.randint (0, 50)
        self.resistencia = self.resistencia + random.randint (0, 50)
        self.agilidad = self.agilidad + random.randint (0, 50)
        
        return self.vida, self.fuerza, self.resistencia, self.agilidad