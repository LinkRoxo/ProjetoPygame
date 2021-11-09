import sys
import Monstros as mob
from enum import Enum

class Mapa:
    def __init__(self) -> None:
        self.map_id = -1
        
        self.velocidade = 10
        self.mobs_do_mapa = []
        self.lista_mob = []

        self.bg_img = None
        self.assets = []

        self.Boss = None

        self.armadilhas = []
        
        self.tessouro = []
        self.chance_tessouro = 1

        #ESTADOS
        self.moving = False


    def update(self):
        if self.moving == True:
            pass

    def spawn_mob(self, mob):
        #criar a variavel que vai conter o mob, passar parametros apartir do ID (pegar na lista de mob)
        #adicionar no vetor mobs_do_mapa
        
        mob = ()
        pass

    def spawn_tessouro(self):
        pass

class monstrosId(Enum):
    Slime = 1    
    pass