import pygame
import sys
from Classes.State import State

sys.path.append(".")

class Obstaculo(pygame.sprite.Sprite):
    pos = (800, 350)
    x, y = pos
    largura = 0
    altura = 0
    dano = 10
    
    sprite = None
    
    vel = -10
    
    state = State.Andando
    relou = False
    
    def __init__(self,largura,altura):
        super().__init__()
        self.largura = largura
        self.altura = altura 
        self.image = pygame.Surface((largura, altura))
        self.rect = self.image.get_rect()
        self.image.fill((255,0,255))

    def draw(self, surface):
        pygame.draw.rect(surface, (125, 204, 143), self.rect)

    def update(self, surface, state):
        self.rect = pygame.Rect(self.x, self.y, self.largura, self.altura)
        if state == State.Andando:
            self.pos = (self.pos[0] + self.vel), (self.pos[1])
            self.x, self.y = self.pos
            
        if self.pos[0] == -100:
            self.kill()
        
    def ataque(self):
        dano = self.dano
        self.relou = True
        return dano    

    def destroy(self):
        pass