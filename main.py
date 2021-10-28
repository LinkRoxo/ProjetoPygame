import pygame
import sys
sys.path.append(".")
from Classes.Jogador import Jogador
from Classes.Monstros import Monstro

VERSION = "0.3"
FPS = 60

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WIN.fill((0,0,0))
pygame.display.set_caption(f"Jogo {VERSION}")

mob = Monstro(1, "Slime", 1, 1, 10, 10, 10, 1)

def screen_update():
    #WIN.blit(mob, (mob.pos))
    pygame.display.update()

def spawn_player(jogador):
    x,y = jogador.get_pos(jogador)
    Prect = pygame.Rect(x, y, 30, 100)
    pygame.draw.rect(WIN, (5 , 10, 100), Prect)

def spawn_monstro(mob):
    x, y = mob.get_pos()
    Mrect = pygame.Rect(x, y, 30, 100)
    pygame.draw.rect(WIN, (255, 0, 0), Mrect)

def main():
    clock = pygame.time.Clock()
    run = True
    #OBJETOS
    jogador = Jogador
    
    spawn_monstro(mob)

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False  

        spawn_player(jogador)
        
        
        if jogador.Vida == 0:
            jogador.die(jogador)
        
        jogador.update(jogador)
        mob.update(WIN)   
        
        screen_update()
    
    pygame.quit()
    


if __name__ == "__main__":
    main()