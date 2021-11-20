import pygame
import sys
import math

sys.path.append(".")
from Classes.State import State

class Monstro:
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

    #Sprites
    sprite = None
    rect = pygame.Rect(x, y, 30, 100)

    surface = None

    #STATES
    state = State.Andando


    def __init__(self, m_id, nome, level, Bxp, Jxp, gold, Mvida, Mmana, poder, surface):
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
        
    

    def draw_mob(self, surface):
        self.rect = pygame.Rect(self.x, self.y, 30, 100)
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
        pass

    def get_pos(self):
        return self.pos

    def update(self, surface):
        if self.state == State.Andando:
            self.pos = (self.pos[0] + self.Vel), (self.pos[1])
            self.x, self.y = self.pos
        
        self.draw_mob(surface)

        if self.Vida == 0:
            self.die()

        if self.state == State.Batalhando:
            """ if jogador.Vida != 0:
                mob.ataque() """
            pass
        
        if self.x <= 140:
            self.setState(1)


        if self.state == State.Parado: #and (self.contador == self.velocidade_ataque)):
            self.setState(2)


    def ataque(self):
        #jogador.hit(self.dano_fisico)
        pass

    def die(self, alvo):
        alvo.addXp(self.Bxp, self.Jxp)
        alvo.addGold(alvo,self.gold)
        print("Monstro morreu")
        pass

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


