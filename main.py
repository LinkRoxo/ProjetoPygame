import pygame
import sys

sys.path.append(".")
from Classes.Jogador import Jogador
jogador = Jogador()
from Classes.Monstros import Monstro
from Classes.State import State
from Classes.Mapa import Mapa

VERSION = "0.5"
FPS = 60

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WIN.fill((0,0,0))
pygame.display.set_caption(f"Jogo {VERSION}")

mapa = Mapa(1, 10, WIN)
mob = Monstro(1, "Slime", 1, 1, 1, 10, 10, 10, 1, WIN)

def screen_update():
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    #OBJETOS
    while run:
        clock.tick(FPS)
        WIN.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False  

        if jogador.Vida == 0:
            jogador.die(jogador)

        if mob.Vida == 0:
            mob.die(jogador)

        if mob.state == State.Batalhando:
            if jogador.Vida != 0:
                mob.ataque(jogador)
        
        jogador.update(WIN)
        mob.update(WIN)   
        
        screen_update()
    
    pygame.quit()
    


if __name__ == "__main__":
    main()