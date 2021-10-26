import pygame
import os
import sys
sys.path.append(".")
from Classes.Jogador import Jogador

VERSION = "0.1"
FPS = 60

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WIN.fill((0,0,0))
pygame.display.set_caption(f"Jogo {VERSION}")

def screen_update():
    pygame.display.update()

def spawn_player(jogador):
    x,y = jogador.get_pos(jogador)
    Prect = pygame.Rect(x, y, 100, 100)
    pygame.draw.rect(WIN, (5 , 10, 100), Prect)


def main():
    clock = pygame.time.Clock()
    run = True
    #OBJETOS
    jogador = Jogador
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False  

        spawn_player(jogador)   
        screen_update()
    
    pygame.quit()
    


if __name__ == "__main__":
    main()