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

        forca = 0 #dano_fisico
        dextreza = 0 #chance_crit
        agilidade = 0 #velocidade_ataque
        inteligencia = 0 #Mana / dano_magico
        vitalidade = 0 # HP / Vigor
        sorte = 0 #chance_drop / chance_crit

        #FORMULAS
        #dano_fisico = (self.forca * 0.1)
        #dano_magico = 0
        #dano_critico = dano_fisico * 2

        #velocidade_ataque = 10

        vigor = 0
        chance_crit = 0
        chance_drop = 0.01

        #Stuff de controle do objeto
        Vel = 10
        possition = pygame.math.Vector2(10,10)
        
        #Parametros de controle
        STATE = None
        walking = False
        jumping = False

        #Sprites
        sprite = None
        rect = None


    def update(self) -> None:
        if self.Vida == 0:
            self.die()

        if self.base_xp == self.base_next_level:
            self.levelUp(0)

        if self.job_xp == self.job_next_level:
            self.levelUp(1)
        
    
    def spawn(self, possition):
        print("Spawned")
        self.possition = possition

    def ataque(self, dano, alvo):
        alvo.hp = alvo.hp - dano

    def pulo(self):
        self.possition = 0 

    def addXp(self, Bqtd, Jqtd):
        self.base_xp += Bqtd
        self.jobe_xp += Jqtd

    def addGold(self, qtd):
        self.gold += qtd

    def levelUp(self, qual):
        if qual == 0:
            base_xp = 0
            base_level =+ 1
            #aumenta xp necessaria
        if qual == 1:
            job_xp = 0
            job_level =+ 1
            #aumenta a xp necessaria

    def die(self):
        #animação
        #tirar xp
        self.spawn()

    
        

        