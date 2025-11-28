import pytest
from src.models.usuario import Usuario
from src.services.CadastroService import CadastroService

class TestCadastroUsuario:

    def test_criar_nova_conta_com_sucesso(self):
        """Caso de teste: TC-USR-001
        """

        nome_input = "Matheus"
        email_input = "matheus@email.com"
        senha_input = "Teste@123"
        
        service = CadastroService()

        resultado = service.criar_conta(nome=nome_input, email=email_input, senha=senha_input)

        assert resultado.sucesso is True
        assert resultado.mensagem == "Conta criada com sucesso!"
        
        assert resultado.usuario.nome == "Matheus"
        assert resultado.usuario.email == "matheus@email.com"
        assert resultado.usuario.senha == "Teste@123"

    def test_alterar_senha(self):
        """Caso de teste: TC-USR-002
        """

        service = CadastroService()
        
        email_usuario = "teste@email.com"
        senha_inicial = "teste@123"
        senha_nova = "novaSenha@123"
        
        service.criar_conta(nome="Matheus", email=email_usuario, senha=senha_inicial)

        resultado = service.alterar_senha(
            email_identificador=email_usuario, 
            nova_senha=senha_nova
        )

        assert resultado.sucesso is True
        assert resultado.mensagem == "Senha alterada com sucesso."
        
        assert resultado.usuario.senha == senha_nova 
        assert resultado.usuario.senha != senha_inicial

    def test_atualizar_perfil(self):
        """Caso de teste: TC-USR-003
        """

        nome_inicial = "Matheus"
        email_inicial = "matheus@email.com"
        senha_inicial = "Teste@123"
        
        service = CadastroService()
        
        resultado_criacao = service.criar_conta(
            nome=nome_inicial, 
            email=email_inicial, 
            senha=senha_inicial
        )
        
        assert resultado_criacao.sucesso is True

        nome_novo = "Zezinho da silva"
        email_novo = "matheus@email.com"

        resultado_atualizacao = service.atualizar_dados(
            email_identificador=email_novo,
            novo_nome=nome_novo, 
            novo_email=email_novo 
        )
        
        assert resultado_atualizacao.sucesso is True
        assert resultado_atualizacao.mensagem == "Dados atualizados com sucesso."

        assert resultado_atualizacao.usuario.nome == nome_novo
        assert resultado_atualizacao.usuario.nome != nome_inicial
        assert resultado_atualizacao.usuario.email == email_novo
        
    def test_falha_login(self):
        """Caso de teste: TC-USR-004
        """
        
        email_valido = "joao@email.com"
        senha_correta = "SenhaCorreta@456"
        
        service = CadastroService()
        
        resultado_criacao = service.criar_conta(
            nome="Joao", 
            email=email_valido, 
            senha=senha_correta
        )
        
        assert resultado_criacao.sucesso is True
        
        email_input = email_valido
        senha_incorreta = "SenhaErrada"
        
        resultado_login = service.fazer_login(
            email=email_input, 
            senha=senha_incorreta
        )
        
        assert resultado_login.sucesso is False
        
        mensagem_esperada = "E-mail ou senha incorretos. Tente novamente."
        assert resultado_login.mensagem == mensagem_esperada
        
        assert resultado_login.usuario is None

    def test_logout(self):
        """Caso de teste: TC-USR-005
        """
        
        nome_valido = "Matheus"
        email_valido = "matheus@email.com"
        senha_correta = "senha@123"
        
        service = CadastroService()
        
        resultado_criacao = service.criar_conta(
            nome=nome_valido, 
            email=email_valido, 
            senha=senha_correta
        )
        assert resultado_criacao.sucesso is True

        resultado_login = service.fazer_login(
            email=email_valido,
            senha=senha_correta
        )
        
        assert resultado_login.sucesso is True

        resultado_logout = service.fazer_logout()
    
        assert resultado_logout.sucesso is True
        assert resultado_logout.mensagem == "Sessão encerrada com sucesso."  
        assert resultado_logout.usuario is None
         