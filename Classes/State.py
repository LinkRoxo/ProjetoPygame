from enum import Enum

class State(Enum):
    Andando = 0
    Parado = 1
    Batalhando = 2
    Pulando = 3
    Caindo = 4
    Morrendo = 5