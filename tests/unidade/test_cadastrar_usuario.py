import pytest
from src.models.usuario import Usuario
from src.services.cadastro_service import CadastroService

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
        assert resultado.usuario.senha != "Teste@123"