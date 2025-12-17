class CatalogoService:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def buscar_jogo_por_termo(self, termo):
        jogos_encontrados = self.repositorio.buscar_jogos_por_termo(termo)
        
        if jogos_encontrados:
            return {
                "sucesso": True, 
                "jogos": jogos_encontrados,
                "mensagem": f"{len(jogos_encontrados)} jogo(s) encontrado(s)."
            }
        else:
            return {
                "sucesso": True, 
                "jogos": [],
                "mensagem": "Nenhum jogo encontrado para sua busca."
            }
        
    def listar_todos(self):
        jogos_encontrados = self.repositorio.listar_todos_jogos()
        
        if jogos_encontrados:
            return {
                "sucesso": True,
                "jogos": jogos_encontrados,
                "mensagem": f"Catálogo carregado com {len(jogos_encontrados)} jogos."
            }
        else:
            return {
                "sucesso": True,
                "jogos": [],
                "mensagem": "O catálogo está vazio no momento."
            }