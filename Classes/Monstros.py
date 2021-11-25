import pygame
import sys
import math

sys.path.append(".")
from Classes.State import State

class Monstro(pygame.sprite.Sprite):
    monstro_id = -1
    nome_monstro = ""

    level = 0
    Bxp = 0
    Jxp = 0

    gold = 0

    Vida = 0
    MVida = 0

    Mana = 0
    MMana = 0

    poder = 1
    
    dano_fisico = math.ceil((poder * 0.1))
    dano_magico = 1
    dano_critico = dano_fisico * 1

    velocidade_ataque = 0.4
    contador = 0
        
    chance_crit = 0.06

    #Stuff de controle do objeto
    Vel = -5
    pos = (800, 350)
    x, y = pos


    surface = None

    #STATES
    state = State.Andando


    def __init__(self, m_id, nome, level, Bxp, Jxp, gold, Mvida, Mmana, poder, surface, jogador):
        super().__init__()
        self.monstro_id = m_id
        self.nome_monstro = nome
        self.level = level
        self.Bxp = Bxp
        self.Jxp = Jxp
        self.gold = gold
        self.MVida = Mvida
        self.MMana = Mmana
        self.poder = poder

        self.Vida = self.MVida
        self.Mana = self.MMana

        self.surface = surface
        self.contador = self.velocidade_ataque

        self.image = pygame.Surface((50, 100))
        self.rect = self.image.get_rect()
        self.image.fill((255, 0, 0))
        
        self.jogador = jogador
        

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)

    def get_pos(self):
        return self.pos

    def update(self, surface, state):
        self.rect = pygame.Rect(self.x, self.y, 50, 100)
        
        if state == State.Andando:
            self.pos = (self.pos[0] + self.Vel), (self.pos[1])
            self.x, self.y = self.pos
        
        #self.draw(surface)

        if self.x <= 160:
            self.setState(1)

        if self.Vida == 0:
            xp = self.die()
            
        if self.rect.colliderect(self.jogador.battle_rect): #and self.jogador.state == State.Andando:
            self.jogador.change_state(2)
            dano = self.jogador.ataque()
            self.hit(dano)
        
        if self.state == State.Parado: #and (self.contador == self.velocidade_ataque)):
            self.setState(2)

        if self.state == State.Batalhando:
            if self.jogador.Vida > 0:
                dano = self.ataque()
                self.jogador.hit(dano)        

        
    def ataque(self):
        return self.dano_fisico


    def die(self):
        xp = self.Bxp
        self.jogador.addXp(xp, 0)
        self.kill()
        

    def hit(self, dano):
        self.Vida = self.Vida - dano

    def get_rect(self, rect):
        self.rect = rect
        pass

    def batalha():
        pass

    def setState(self, state):
        if state == 0:
            self.state = State.Andando
        
        if state == 1:
            self.state = State.Parado

        if state == 2:
            self.state = State.Batalhando

