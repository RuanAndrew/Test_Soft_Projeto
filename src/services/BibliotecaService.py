class BibliotecaService:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def buscar_jogo(self, usuario, jogo):
        compra = self.repositorio.buscar_compra_por_usuario(usuario.id, jogo.id)
        
        if compra and compra.get("status") == "COMPRADO":
            return {
                "sucesso": True,
                "download_disponivel": True,
                "mensagem": "Jogo disponível"
            }
        else: 
            return {
                "sucesso": False,
                "download_disponivel": False,
                "mensagem": f"Parece que este jogo ainda não é seu! Adquira {jogo.titulo} na loja.",
                "link_loja": f"/loja/jogo/{jogo.id}"
            }

    def iniciar_download(self, usuario, jogo):
        possui_jogo = self.repositorio.verificar_posse(usuario.id, jogo.titulo)
        
        if possui_jogo:
            return {
                "sucesso": True,
                "mensagem": f"Iniciando download de {jogo.titulo}..."
            }
        else:
            return {"sucesso": False, "mensagem": "Usuário não possui o jogo."}

    def desinstalar_jogo(self, usuario, jogo):
        self.repositorio.atualizar_status(usuario.id, jogo.id, "NAO_INSTALADO")
        
        return {
            "sucesso": True,
            "status_atual": "NAO_INSTALADO",
            "mensagem": "O jogo foi desinstalado com sucesso."
        }