import pytest
from unittest.mock import MagicMock

class TestCadastroUsuario:

    def test_criar_nova_conta_com_sucesso(self, cadastro_service, mock_repositorio):
        """Caso de teste: TC-USR-001
        """

        mock_usuario = MagicMock()
        mock_usuario.nome = "Matheus"
        mock_usuario.email = "matheus@email.com"
        mock_usuario.senha = "Teste@123"
        
        resultado = cadastro_service.criar_conta(usuario=mock_usuario)

        assert resultado["sucesso"] is True
        assert resultado["mensagem"] == "Conta criada com sucesso!"
        
        assert resultado["usuario"]["nome"] == "Matheus"
        assert resultado["usuario"]["email"] == "matheus@email.com"
        assert resultado["usuario"]["senha"] == "Teste@123"

    def test_alterar_senha(self, cadastro_service, mock_repositorio):
        """Caso de teste: TC-USR-002
        """
    
        mock_usuario = MagicMock()
        mock_usuario.email = "teste@email.com"
        mock_usuario.senha_inicial = "teste@123"
        mock_usuario.senha_nova = "novaSenha@123"

        cadastro_service.criar_conta(usuario=mock_usuario)

        resultado = cadastro_service.alterar_senha(usuario=mock_usuario)

        assert resultado["sucesso"] is True
        assert resultado["mensagem"] == "Senha alterada com sucesso."
        
        assert resultado["usuario"]["senha"] == mock_usuario.senha_nova 
        assert resultado["usuario"]["senha"] != mock_usuario.senha_inicial

    def test_atualizar_perfil(self, cadastro_service, mock_repositorio):
        """Caso de teste: TC-USR-003
        """

        mock_usuario = MagicMock()
        mock_usuario.nome = "Matheus"
        mock_usuario.email = "matheus@email.com"
        mock_usuario.senha = "Teste@123"

        mock_usuario.nome_novo = "Zezinho da silva"
        mock_usuario.email_novo = "zezinho@email.com"
        mock_usuario.senha_nova = "NovoTeste@123"
        
        resultado = cadastro_service.atualizar_perfil(mock_usuario)

        assert resultado["sucesso"] is True
        assert resultado["mensagem"] == "Dados atualizados com sucesso."

        assert resultado["usuario"]["nome"] == mock_usuario.nome_novo
        assert resultado["usuario"]["nome"] != mock_usuario.nome

        assert resultado["usuario"]["email"] == mock_usuario.email_novo
        assert resultado["usuario"]["email"] != mock_usuario.email

        assert resultado["usuario"]["senha"] == mock_usuario.senha_nova
        assert resultado["usuario"]["senha"] != mock_usuario.senha
        
    def test_falha_login(self, cadastro_service, mock_repositorio):
        """Caso de teste: TC-USR-004
        """
    
        mock_usuario = MagicMock()
        mock_usuario.nome = "Joao"
        mock_usuario.email_valido = "joao@email.com"
        mock_usuario.senha_correta = "SenhaCorreta@456"
        
        mock_usuario.email_input = mock_usuario.email_valido
        mock_usuario.senha_input = "SenhaErrada"
        
        resultado = cadastro_service.fazer_login(mock_usuario)
        
        assert resultado["sucesso"] == False
        assert resultado["mensagem"] == "E-mail ou senha incorretos. Tente novamente."

    def test_logout(self, cadastro_service, mock_repositorio):
        """Caso de teste: TC-USR-005
        """

        resultado = cadastro_service.fazer_logout()
    
        assert resultado["sucesso"] == True
        assert resultado["mensagem"] == "Sessão encerrada com sucesso."  
         