import pygame
from Classes.State import State

class Tesouro():
    gold = None
    vel = -5

    pos = (200,300)
    x,y = pos

    state = State.Andando

    def __init__(self, gold):
        self.gold = gold
        return self
    
    def update(self):
        if self.state == State.Andando:
            self.pos = (self.pos[0] + self.vel), (self.pos[1])
            self.x, self.y = self.pos
        pass

    def colide(self):
        pass
