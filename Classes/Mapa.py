import random
import pygame

from enum import Enum
from Classes.Monstros import Monstro
from Classes.Obstaculos import Obstaculo
from Classes.State import State
from Classes.Jogador import Jogador
jogador = Jogador()

class Mapa:
    def __init__(self, map_id, vel, surface) -> None:
        self.map_id = map_id
        
        self.velocidade = vel
        self.mobs_do_mapa = pygame.sprite.Group()
        self.lista_mob = []

        self.bg_img = None
        self.assets = []

        self.Boss = None

        self.obstaculos = pygame.sprite.Group()
        
        self.tessouro = []
        self.chance_tessouro = 1

        #ESTADOS
        self.moving = False
        
        self.surface = surface

        self.contador = 100
        self.state = State.Andando


    def update(self):
        self.contador -= 1

        if self.contador <= 0 and self.state == State.Andando:
            self.spawn_mob()
            self.contador = 100
            self.spawn_obstaculo() 
            pass

        if jogador.Vida == 0:
            jogador.die()

        if jogador.pos[1] == 200 and jogador.state == State.Pulando:
            jogador.change_state(4)

        jogador.update(self.surface)


        self.mobs_do_mapa.update(self.surface, self.state)
        self.mobs_do_mapa.draw(surface)


        for i in self.mobs_do_mapa:
            index = 0
            index += 1
            i.update(self.surface, self.state)
            
            if i.Vida == 0:
                xp = i.die()
                jogador.addXp(xp, 0)
                self.destroy_mob(index)
                print(str(index))
            
            if jogador.battle_rect.colliderect(i.rect) and jogador.state == State.Andando:
                self.state = State.Parado
                jogador.change_state(2)
                dano = jogador.ataque()
                i.hit(dano)
            
            if i.state == State.Batalhando:
                if jogador.Vida <= 0:
                    dano = i.ataque()
                    jogador.hit(dano)

            self.obstaculos.update(self.surface, self.state)
            self.obstaculos.draw(self.surface)



        """ for i in self.obstaculos:
            i.update(self.surface, self.state)
            if jogador.rect.colliderect(i.rect):
                if i.relou == False:
                    dano = i.ataque()
                    jogador.hit(dano) """
        

        
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
        self.mobs_do_mapa.add(mob)
    
    def spawn_obstaculo(self):
        obs = Obstaculo(100,100)
        self.obstaculos.add(obs)

    def destroy_mob(self, mob):
        self.mobs_do_mapa.pop(mob)
        print("poped")

    def botao(self):
        jogador.change_state(3)