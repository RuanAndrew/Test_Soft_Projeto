class CatalogoService:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def buscar_jogo_por_termo(self, termo):
        jogos_encontrados = self.repositorio.buscar_por_termo(termo)
        
        jogos_ativos = []
        for jogo in jogos_encontrados:
            if jogo.status == "ativo":
                jogos_ativos.append(jogo)
        
        if jogos_ativos:
            return {
                "sucesso": True, 
                "jogos": jogos_ativos,
                "mensagem": f"{len(jogos_ativos)} jogo(s) encontrado(s)."
            }
        else:
            return {
                "sucesso": True, 
                "jogos": [],
                "mensagem": "Nenhum jogo encontrado para sua busca."
            }