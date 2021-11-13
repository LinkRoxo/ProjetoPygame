import pygame
from Classes.State import State

class Jogador:
    #Stats in game do Jogador
    base_level = 1
    base_xp = 0
    base_next_level = 10
    base_pontos = 0

    job_level = 1
    job_xp = 0
    job_next_level = 10
    job_pontos = 0

    gold = 0

    Vida = 50
    MVida = 50

    Mana = 10
    MMana = 10

    forca = 0 #dano_fisico
    dextreza = 0 #chance_crit
    agilidade = 0 #velocidade_ataque
    inteligencia = 0 #Mana / dano_magico
    vitalidade = 0 # HP / Vigor
    sorte = 0 #chance_drop / chance_crit

        #FORMULAS
    dano_fisico = (forca * 0.1)
    dano_magico = 0
    dano_critico = dano_fisico * 2

    velocidade_ataque = 10

    vigor = 0
    chance_crit = 0
    chance_drop = 0.01

    #Stuff de controle do objeto
    Vel = 10
    pos = (100, 350)
    x, y = pos
        
    #Parametros de controle
    state = None
    walking = False
    jumping = False

    #Sprites
    rect = pygame.Rect(x, y, 30, 100)
    sprite = None 
    
    def __init__(self):
        pass
        
    def get_pos(self):
        return self.pos

    def update(self, surface):
        pygame.draw.rect(surface, (5, 10, 100), self.rect)
        
        if self.Vida <= 0:
            self.die(self)

        if self.base_xp == self.base_next_level:
            self.levelUp(self, 0)

        if self.job_xp == self.job_next_level:
            self.levelUp(self, 1)
        
        
    def ataque(self, dano, alvo):
        alvo.hp = alvo.hp - dano

    def pulo(self):
        self.possition = 0 

    def addXp(self, Bqtd, Jqtd):
        self.base_xp += Bqtd
        self.job_xp += Jqtd

    def addGold(self, qtd):
        self.gold += qtd

    def levelUp(self, qual):
        if qual == 0:
            self.base_xp = 0
            self.base_level += 1
            self.base_pontos += 1
        if qual == 1:
            self.job_xp = 0
            self.job_level += 1
            self.job_pontos += 1

    def addPonto(self, qual):
        if qual == 0:
            self.forca += 1
            self.base_pontos -= 1
        if qual == 1:
            self.dextreza += 1
            self.base_pontos -= 1
        if qual == 2:
            self.agilidade += 1
            self.base_pontos -= 1
        if qual == 3:
            self.inteligencia += 1
            self.base_pontos -= 1
        if qual == 4:
            self.vitalidade += 1
            self.base_pontos -= 1
        if qual == 5:
            self.sorte += 1
            self.base_pontos -= 1

    def hit(self, dano):
        self.Vida = self.Vida - dano
        print("Vida: " + str(self.Vida))

    def die(self):
        #animação
        self.base_xp -= (self.base_xp / 100) * 0.1
        self.job_xp -= (self.job_xp / 100) * 0.01
        print("morreu")
        pass

#função de debug
    def kill(self):
        self.Vida == 0
    
        