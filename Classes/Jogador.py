import pygame
from pygame import surface

class Jogador:
    #Stuff de controle do objeto
    Vel = 10
    pos = (50, 50)
        
    #Parametros de controle
    STATE = None
    walking = False
    jumping = False

    #Sprites
    sprite = None 
    
    def __init__(self):
        #Stats in game do Jogador
        self.base_level = 1
        self.base_xp = 0
        self.base_next_level = 10

        self.job_level = 1
        self.job_xp = 0
        self.job_next_level = 10

        self.gold = 0

        self.Vida = 50
        self.MVida = 50

        self.Mana = 10
        self.MMana = 10

        self.forca = 0 #dano_fisico
        self.dextreza = 0 #chance_crit
        self.agilidade = 0 #velocidade_ataque
        self.inteligencia = 0 #Mana / dano_magico
        self.vitalidade = 0 # HP / Vigor
        self.sorte = 0 #chance_drop / chance_crit

        #FORMULAS
        self.dano_fisico = (self.forca * 0.1)
        self.dano_magico = 0
        self.dano_critico = self.dano_fisico * 2

        self.velocidade_ataque = 10

        self.vigor = 0
        self.chance_crit = 0
        self.chance_drop = 0.01

    def get_pos(self):
        return self.pos

    def update(self) -> None:
        if self.Vida == 0:
            self.die()

        if self.base_xp == self.base_next_level:
            self.levelUp(0)

        if self.job_xp == self.job_next_level:
            self.levelUp(1)
        
    def spawn(self, possition):
        print("Spawned")
        self.possition = possition

    def ataque(self, dano, alvo):
        alvo.hp = alvo.hp - dano

    def pulo(self):
        self.possition = 0 

    def addXp(self, Bqtd, Jqtd):
        self.base_xp += Bqtd
        self.jobe_xp += Jqtd

    def addGold(self, qtd):
        self.gold += qtd

    def levelUp(self, qual):
        if qual == 0:
            self.base_xp = 0
            self.base_level =+ 1
            #aumenta xp necessaria
        if qual == 1:
            self.job_xp = 0
            self.job_level =+ 1
            #aumenta a xp necessaria

    def die(self):
        #animação
        #tirar xp
        self.spawn()

    
        

        