class Monstro:
    monstro_id = -1
    nome_monstro = ""

    #states monstro
    level = 0
    xp = 0

    gold = 0

    Vida = 0
    MVida = 0

    Mana = 0
    MMana = 0

    poder = 0
    
    dano_fisico = (poder * 0.1)
    dano_magico = 1
    dano_critico = dano_fisico * 1

    velocidade_ataque = 10
        
    chance_crit = 0.06

    #Sprites
    sprite = None
    rect = None

    #Stuff de controle do objeto
    Vel = 10
    pos = (800, 350)

    def __init__(self, m_id, nome, level, xp, gold, Mvida, Mmana, poder):
        self.monstro_id = m_id
        self.nome_monstro = nome
        self.level = level
        self.xp = xp
        self.gold = gold
        self.MVida = Mvida
        self.MMana = Mmana
        self.poder = poder

    def get_pos(self):
        return self.pos

    def update(self, surface):
        print("chegou update monstro")
        
        if self.Vida == 0:
            self.die()
        
        self.pos = (self.pos[0] + self.Vel), (self.pos[1])

    def ataque(self, dano, alvo):
        alvo.hp = alvo.hp - dano

    def die(self):
        #animação
        #tirar xp
        pass
