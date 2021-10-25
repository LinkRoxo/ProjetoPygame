import pygame

class Monstro:
    def __init__(self) -> None:
        #states monstro
        level = 3
        xp = 5

        gold = 0

        Vida = 40
        MVida = 40

        Mana = 7
        MMana = 7

        dano_fisico = (self.força * 0.1)
        dano_magico = 1
        dano_critico = dano_fisico * 1

        velocidade_ataque = 10
        
        vigor = 0.8
        chance_crit = 0.06
        chance_drop = 0.01

        força = 1 #dano_fisico

    def update(self) -> None:
        if self.Vida == 0:
            self.die()
    
    def spawn(self, possition):
        self.possition = possition

    def ataque(self, dano, alvo):
        alvo.hp = alvo.hp - dano

    def die(self):
        #animação
        #tirar xp
        self.spawn()

