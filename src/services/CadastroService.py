class CadastroService:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def criar_conta(self, usuario):
        self.repositorio.salvar_usuario(usuario)
        return {
            "sucesso": True,
            "mensagem": "Conta criada com sucesso!",
            "usuario": {"nome": usuario.nome, "email": usuario.email, "senha": usuario.senha}
        }

    def alterar_senha(self, usuario):
        if hasattr(usuario, 'senha_nova'):
            usuario.senha = usuario.senha_nova

        self.repositorio.atualizar_usuario(usuario)
        return {
            "sucesso": True,
            "mensagem": "Senha alterada com sucesso.",
            "usuario": {"senha": usuario.senha_nova}
        }

    def atualizar_perfil(self, usuario):
        return {
            "sucesso": True,
            "mensagem": "Dados atualizados com sucesso.",
            "usuario": {
                "nome": usuario.nome_novo,
                "email": usuario.email_novo,
                "senha": usuario.senha_nova
            }
        }

    def fazer_login(self, usuario):
        usuario_banco = self.repositorio.buscar_usuario_por_email(usuario.email)

        if usuario_banco and usuario.senha == usuario_banco.senha:
            return {"sucesso": True}
            
        return {"sucesso": False, "mensagem": "E-mail ou senha incorretos. Tente novamente."}

    def fazer_logout(self):
        return {"sucesso": True, "mensagem": "Sessão encerrada com sucesso."}