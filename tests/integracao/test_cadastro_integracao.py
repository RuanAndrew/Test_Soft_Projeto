import pytest
from src.models.usuario import Usuario

class TestCadastroIntegracao:
    
    def test_criar_e_logar_novo_usuario(self, integ_cadastro_service, db_memory):
        """
        Cenário: Criar um usuário que não existe e tenta o logar.
        Valida: Se o RepositorioMemoria está persistindo novos dados.
        """
        novo_usuario = Usuario(id=None, nome="Novato", email="novo@email.com", senha="123")
        
        resp_criacao = integ_cadastro_service.criar_conta(novo_usuario)
        assert resp_criacao["sucesso"] is True
        
        usuario_login = Usuario(id=None, nome="", email="novo@email.com", senha="123")
        
        resp_login = integ_cadastro_service.fazer_login(usuario_login)
        
        assert resp_login["sucesso"] is True

    def test_alterar_senha_fluxo_real(self, integ_cadastro_service, db_memory):
        """
        Cenário: Pegar usuário padrão, trocar senha e tentar logar com a nova.
        """
        usuario = db_memory.buscar_usuario_por_email("teste@email.com")
        
        usuario.senha_nova = "NovaSenhaForte"
        integ_cadastro_service.alterar_senha(usuario)
        
        login_velho = Usuario(None, "", "teste@email.com", "123")
        assert integ_cadastro_service.fazer_login(login_velho)["sucesso"] is False
        
        login_novo = Usuario(None, "", "teste@email.com", "NovaSenhaForte")
        assert integ_cadastro_service.fazer_login(login_novo)["sucesso"] is True