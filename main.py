import pygame
import sys

sys.path.append(".")
from Classes.Monstros import Monstro
from Classes.State import State
from Classes.Mapa import Mapa

VERSION = "0.7"
FPS = 60

pygame.init()
WIDTH, HEIGHT = 900, 500
global WIN 
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WIN.fill((0,0,0))
pygame.display.set_caption(f"Jogo {VERSION}")

mapa = Mapa(1, 10, WIN)

def screen_update():
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    #OBJETOS
    while run:
        clock.tick(FPS)
        #DELTA TIME
        WIN.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False  
            if event.type == pygame.KEYDOWN:
                tecla = pygame.key.get_pressed()
                if tecla[pygame.K_SPACE]:
                    mapa.botao()    
   
        mapa.update()
        screen_update()
    
    pygame.quit()
    


if __name__ == "__main__":
    main()