class Jogo:
    def __init__(self, id, titulo, preco=0.0, status="ativo", descricao=""):
        self.id = id
        self.titulo = titulo
        self.preco = preco
        self.status = status
        self.descricao = descricao
    
    def __repr__(self):
        return f"Jogo(id={self.id}, titulo='{self.titulo}', preco={self.preco}, status='{self.status}')"
    
    def __eq__(self, other):
        if isinstance(other, Jogo):
            return self.id == other.id
        return False