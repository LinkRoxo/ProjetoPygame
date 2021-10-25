import pygame

class Jogador:
    def __init__(self) -> None:
        #Stats in game do Jogador
        base_level = 1
        base_xp = 0
        base_next_level = 10

        job_level = 1
        job_xp = 0
        job_next_level = 10

        gold = 0

        Vida = 50
        MVida = 50

        Mana = 10
        MMana = 10

        dano_fisico = (self.força * 0.1)
        dano_magico = 0
        dano_critico = dano_fisico * 2

        velocidade_ataque = 10

        vigor = 0
        chance_drop = 0.01

        força = 0
        dextreza = 0
        agilidade = 0
        inteligencia = 0
        vitalidade = 0
        sorte = 0

        #Stuff de controle do objeto
        Vel = 10
        possition = pygame.math.Vector2(-1,-1)
        
        #Parametros de controle
        STATE = None
        can_walk = False
        jumping = False
        pass

    def update(self) -> None:
        if self.Vida == 0:
            self.die()

        if self.base_xp == self.base_next_level:
            self.levelUp(0)

        if self.job_xp == self.job_next_level:
            self.levelUp(1)
        
    
    def spawn(self, possition):
        self.possition = possition

    def ataque(self, dano, alvo):
        alvo.hp = alvo.hp - dano

    def pulo(self):
        self.possition = 0
        pass    

    def levelUp(self, qual):
        if qual == 0:
            base_xp = 0
            base_level =+ 1
            #aumenta xp necessaria
            pass
        if qual == 1:
            job_xp = 0
            job_level =+ 1
            #aumenta a xp necessaria
            pass
        pass

    def die(self):
        #animação
        #tirar xp
        self.spawn()
        pass

    
        

        