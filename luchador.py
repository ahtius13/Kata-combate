import random

class Luchador:
    

    def __init__(self, nombre, vida, fuerza, resistencia, agilidad):

        self.nombre = nombre
        self.vida = int(vida)
        self.fuerza = int(fuerza)
        self.resistencia = int(resistencia)
        self.agilidad = int(agilidad)

    


    def preparar (self):
        self.vida = self.vida + random.randint (0, 10)
        self.fuerza = self.fuerza + random.randint (0, 10)
        self.resistencia = self.resistencia + random.randint (0, 10)
        self.agilidad = self.agilidad + random.randint (0, 10)
        
        return self.vida, self.fuerza, self.resistencia, self.agilidad
        
        
    

    def atacar (self):
         dados = self.fuerza / 10
         i = 1
         dice = random.randint(1,10)
         while i <= dados:
            damage = 0 + dice
            i += 1
            dice = random.randint(1,10)
        
         return damage 

    def defender (self):
         dados = self.resistencia / 10
         i = 1
         dice = random.randint(1,10)
         while i <= dados:
            bloqueado = 0 + dice
            i += 1
            dice = random.randint(1,10)
            
         return bloqueado 

    def iniciativa (self):
        dados = self.agilidad / 10
        i = 1
        dice = random.randint(1,10)
        while i <= dados:
            velocidad = 0 + dice
            i += 1
            dice = random.randint(1,10)

        return velocidad
    
    def lifeLost (self, Luchador):

        damage = Luchador.atacar()
        bloqueo = self.defender()

        dañorecibido = damage - bloqueo
        if dañorecibido >= 0:
            self.vida = self.vida - dañorecibido

        return self.vida