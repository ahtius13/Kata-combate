# Kata-combate

El objetivo de esta kata es crear clases y objetos que puedan luchar entre ellas y visualizar el resultado.

## Entidades

### Luchador
Los luchadores son los combatientes y poseeran los siguientes atributos:

- Vida: el total de puntos de golpe que pueden resistir
- Fuerza: El daño que pueden hacer
- Resistencia: El daño que pueden mitigar
- Agilidad: La capacidad de esquivar un ataque y la iniciativa en cada turno

Cada 10 puntos en una de las estadisticas se añade D10 a la tirada en el combate.

La vida es la suma total de los puntos en las otras estadisticas más una tirada de resistencia (1D10 * (Resistencia/10)) 

#### Acciones
- Atacar
- Defender
- Moverse
- Recibir Daño

### Arena
La Arena es el lugar donde se realiza el combate:

- Bonus
- Debuff
- Tamaño

### Ataques
Son los movimientos que realizan los luchadores:

- Potencia
- Alcance

### Defensas
Son las distintas formas de defenderse de los luchadores:

- Fluidez
- Estabilidad

### Combate
Es la propia batalla en si:

- Combatientes
- Turnos
- Ganador
- Perdedor

