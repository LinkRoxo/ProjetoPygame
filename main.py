import pygame
import os
import sys
sys.path.append(".")
from Classes.Jogador import Jogador

VERSION = "0.1"
FPS = 60

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(f"Sport Games {VERSION}")



def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False  
    
        jogador = Jogador
        jogador.debug()
    pygame.quit()


if __name__ == "__main__":
    main()