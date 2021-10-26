import pygame
import os
import sys
sys.path.append(".")
from Classes.Jogador import Jogador

VERSION = "0.1"
FPS = 60

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(f"Jogo {VERSION}")

jogador = Jogador()

def screen_update():
    WIN.fill((0,0,0))
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    jogador.spawn((10,10))
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False  
    
        screen_update()
    
    
    pygame.quit()
    


if __name__ == "__main__":
    main()