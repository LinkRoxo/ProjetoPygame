import pygame
import sys
from Classes.State import State

sys.path.append(".")

class Obstaculo:
    pos (800, 350)
    x, y = pos
    
    sprite = None
    rect = pygame.Rect(x, y, 30, 100)
    
    vel = -10
    
    state = State.Andando
    
    def __init__(self):
        pass
    
    def update(self):
        draw_obstaculo()
        
        if self.state == State.Andando:
            self.pos = (self.pos[0] + self.Vel), (self.pos[1])
            self.x, self.y = self.pos
            
        if self.pos[0] == -10
            self.destroy()
        
    
    def draw_obstaculo(self):
        self.rect = pygame.Rect(self.x, self.y, 30 100)
        pygame.draw.rect(surface, (125, 204, 143), self.rect)
        pass
    
    def destroy(self):
        self.kill()
        pass