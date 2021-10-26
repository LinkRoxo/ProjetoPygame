class Mapa:
    def __init__(self) -> None:
        map_id = -1
        
        velocidade = 10
        mobs_do_mapa = []
        lista_mob = []

        bg_img = None
        assets = []

        Boss = None

        armadilhas = []
        
        tessouro = []
        chance_tessouro = 1

        #ESTADOS
        moving = False


    def update(self):
        if self.moving == True:
            pass

    def spawn_mob(self, mob):
        #criar a variavel que vai conter o mob, passar parametros apartir do ID (pegar na lista de mob)
        #adicionar no vetor mobs_do_mapa
        pass

    def spawn_tessouro(self):
        pass

