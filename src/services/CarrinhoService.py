class CarrinhoService:
    def __init__(self):
        self.itens = []

    def adicionar_jogo(self, jogo):
        self.itens.append(jogo)

    def remover_jogo(self, jogo):
        self.itens = [item for item in self.itens if item != jogo]

    def listar_jogos(self):
        return self.itens

    def calcular_total(self):
        return sum(getattr(jogo, 'preco', 0) for jogo in self.itens)
