import pygame
import os
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

    forca = 1 #dano_fisico
    dextreza = 1 #chance_crit
    agilidade = 1 #velocidade_ataque
    inteligencia = 1 #Mana / dano_magico
    vitalidade = 1 # HP / Vigor
    sorte = 1 #chance_drop / chance_crit

        #FORMULAS
    dano_fisico = (forca * 2)
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
    sprite = pygame.sprite.Sprite()
    sprite_group = pygame.sprite.Group()
    sprite_path = pygame.Rect(x, y, 100, 100) #pygame.transform.scale(pygame.image.load(os.path.join("Assets/Jogador/Parado", "adventurer-idle-00.png")), (50, 100))
    rect = None
    battle_rect = pygame.Rect(160, 380, 20, 20)

    def __init__(self):
        #self.rect = self.sprite_path.get_rect()
        self.rect = self.sprite_path
        self.state = State.Andando
        #self.sprite_group.add(self.sprite_path)
        pass
        
    def get_pos(self):
        return self.pos

    def draw_jogador(self, surface):
        self.rect.topleft = [self.x, self.y]
        pygame.draw.rect(surface, (255, 255, 255), self.rect)
        #self.sprite_group.draw()

        #pygame.draw.rect(surface, (255,0,255), self.battle_rect)

    def update(self, surface): 
        print(str(self.state))
        if self.Vida <= 0:
            self.die()

        if self.base_xp == self.base_next_level:
            self.levelUp(0)

        if self.job_xp == self.job_next_level:
            self.levelUp(1)

        if self.state == State.Pulando:
            self.pulando()
            self.draw_jogador(surface)  
            
        if self.state == State.Caindo:
            self.gravity()
            self.draw_jogador(surface)

        if self.state == State.Batalhando:
            self.ataque(self.dano_fisico, alvo)

        self.draw_jogador(surface)

    def pulando(self):  
        if self.pos[1] >= 200:
            self.pos = self.pos[0] , self.pos[1] - 10
            self.x, self.y = self.pos
        

    def change_state(self,state):
        if state == 0:
            self.state = State.Andando
        if state == 2:
            self.state = State.Batalhando
        if state == 3:
            self.state = State.Pulando
        if state == 4:
            self.state = State.Caindo

    def ataque(self):
        return self.dano_fisico

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

    def gravity(self):
        if self.state == State.Caindo or self.state == State.Batalhando and self.y >= 200:
            self.pos = self.pos[0] , self.pos[1] + 5
            self.x, self.y = self.pos
            if self.pos[1] == 350:
                self.change_state(0)
        pass
    
    def die(self):
        #animação
        self.base_xp -= (self.base_xp / 100) * 0.1
        self.job_xp -= (self.job_xp / 100) * 0.01
        pass



#função de debug
    def kill(self):
        self.Vida == 0
    
        