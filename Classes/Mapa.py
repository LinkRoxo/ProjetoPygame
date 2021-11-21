import random
from enum import Enum
from Classes.Monstros import Monstro
from Classes.Obstaculo import Obstaculo

class Mapa:
    def __init__(self, map_id, vel, surface, jogador) -> None:
        self.map_id = map_id
        
        self.velocidade = vel
        self.mobs_do_mapa = []
        self.lista_mob = []

        self.bg_img = None
        self.assets = []

        self.Boss = None

        self.obstaculos = []
        
        self.tessouro = []
        self.chance_tessouro = 1

        #ESTADOS
        self.moving = False
        
        self.surface = surface

        self.jogador = jogador
        self.contador = 100


    def update(self):
        self.contador -= 1

        if self.contador <= 0:
            self.spawn_mob()
            self.contador = 100

        if self.moving == True:
            pass

        for i in self.mobs_do_mapa:
            i.update(self.surface)
        
        for i in self.obstaculos:
            i.update(self.surface)

    def spawn_tessouro(self):
        pass

    def setMob(self, mid, surface):
        if mid == 1:
            mob = Monstro(1, "Slime", 1, 1, 1, 10, 10, 10, 1, surface)
            return mob
        if mid == 2:
            mob = Monstro(2, "Goblin", 3, 3, 3, 15, 15, 20, 5, surface)
            return mob
        if mid == 3:
            mob = Monstro(3,"cyclops bat",5,5,5,18,20,30,10,surface)
            return mob
        if mid == 4:
            mob = Monstro(4,"hell worm",8,8,8,22,25,40,20,surface)
            return mob
        if mid == 5:
            mob = Monstro(5,"demonic trunk",11,11,11,26,20,50,30,surface)
            return mob
        if mid == 6:
            mob = Monstro(6,"black wolf",15,15,15,30,25,60,40,surface)
            return mob
        if mid == 7:
            mob = Monstro(7,"flying slug",18,18,18,36,30,70,50,surface)
            return mob
        if mid == 8:
            mob = Monstro(8,"Golen",21,21,21,42,35,80,60,surface)
            return mob
        if mid == 9:
            mob = Monstro(9,"cave spider",26,26,26,48,30,90,70,surface)
            return mob
        if mid == 10:
            mob = Monstro(10,"leftover hunter",30,30,30,52,35,100,80,surface)
            return mob
        else:
            print("ID ERRADO")

    def spawn_mob(self):
        #criar a variavel que vai conter o mob, passar parametros apartir do ID (pegar na lista de mob)
        #adicionar no vetor mobs_do_mapa
        mob_id = random.randint(1,10)
        mob = self.setMob(mob_id, self.surface)
        self.mobs_do_mapa.append(mob)
    
    def spawn_obstaculo(self):
        obs = Obstaculo()
        self.obstaculos.append(obs)


class monstrosId(Enum):
    Slime = 1    
    pass