class Catalogo:
    def __init__(self, jogos=None):
        self.jogos = jogos if jogos is not None else []

    def adicionar_jogo(self, jogo):
        self.jogos.append(jogo)

    def listar_jogos(self):
        return self.jogos