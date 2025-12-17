class Biblioteca:
    def __init__(self, usuario_id):
        self.usuario_id = usuario_id
        self.jogos_comprados = []
        self.jogos_instalados = []
    
    def adicionar_jogo(self, jogo):
        if jogo not in self.jogos_comprados:
            self.jogos_comprados.append(jogo)
            return True
        return False
    
    def remover_jogo(self, jogo):
        if jogo in self.jogos_comprados:
            self.jogos_comprados.remove(jogo)
            if jogo in self.jogos_instalados:
                self.jogos_instalados.remove(jogo)
            return True
        return False
    
    def instalar_jogo(self, jogo):
        if jogo in self.jogos_comprados and jogo not in self.jogos_instalados:
            self.jogos_instalados.append(jogo)
            return True
        return False
    
    def desinstalar_jogo(self, jogo):
        if jogo in self.jogos_instalados:
            self.jogos_instalados.remove(jogo)
            return True
        return False
    
    def possui_jogo(self, jogo):
        return jogo in self.jogos_comprados
    
    def listar_jogos_comprados(self):
        return self.jogos_comprados
    
    def listar_jogos_instalados(self):
        return self.jogos_instalados