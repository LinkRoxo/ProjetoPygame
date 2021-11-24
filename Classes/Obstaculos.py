import pygame
import sys
from Classes.State import State

sys.path.append(".")

class Obstaculo:
    pos = (800, 350)
    x, y = pos
    largura = 0
    altura = 0
    dano = 10
    
    sprite = None
    rect = pygame.Rect(x, y, 0, 0)
    
    vel = -10
    
    state = State.Andando
    relou = False
    
    def __init__(self,largura,altura):
        self.largura = largura
        self.altura = altura 

    def draw_obstaculo(self, surface):
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)
        pygame.draw.rect(surface, (125, 204, 143), self.rect)

    def update(self, surface, state):
        self.draw_obstaculo(surface)
        
        if state == State.Andando:
            self.pos = (self.pos[0] + self.vel), (self.pos[1])
            self.x, self.y = self.pos
            
        if self.pos[0] == -10:
            self.destroy()
        
    def ataque(self):
        dano = self.dano
        self.relou = True
        return dano    

    def destroy(self):
        pass