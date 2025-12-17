import pytest
from src.models.Jogo import Jogo
from src.services.CarrinhoService import CarrinhoService


class TestCarrinhoIntegracao:
    """Testes de Integração para o Carrinho - Teste de Caixa Preta"""

    def test_carrinho_vazio_inicialmente(self):
        """Teste de precondição: carrinho deve estar vazio ao inicializar"""
        carrinho = CarrinhoService()

        assert carrinho.listar_jogos() == []
        assert carrinho.calcular_total() == 0.0

    def test_adicionar_unico_jogo_ao_carrinho(self, catalogo_com_jogos):
        """Teste de adição de um único jogo ao carrinho (TC-CAR-001)"""
        carrinho = CarrinhoService()
        jogo = Jogo(id=5, titulo="Call of Duty: Black Ops 7", preco=349.90)

        carrinho.adicionar_jogo(jogo)

        assert len(carrinho.listar_jogos()) == 1
        assert carrinho.listar_jogos()[0].titulo == "Call of Duty: Black Ops 7"
        assert carrinho.calcular_total() == 349.90

    def test_adicionar_multiplos_jogos_ao_carrinho(self):
        """Teste de adição de múltiplos jogos ao carrinho"""
        carrinho = CarrinhoService()
        jogo1 = Jogo(id=1, titulo="The Witcher 3", preco=99.99)
        jogo2 = Jogo(id=2, titulo="Cyberpunk 2077", preco=199.90)
        jogo3 = Jogo(id=4, titulo="Hollow Knight", preco=46.99)

        carrinho.adicionar_jogo(jogo1)
        carrinho.adicionar_jogo(jogo2)
        carrinho.adicionar_jogo(jogo3)

        assert len(carrinho.listar_jogos()) == 3
        assert carrinho.calcular_total() == pytest.approx(346.88, 0.01)

    def test_remover_jogo_do_carrinho(self):
        """Teste de remoção de um jogo do carrinho"""
        carrinho = CarrinhoService()
        jogo1 = Jogo(id=1, titulo="The Witcher 3", preco=99.99)
        jogo2 = Jogo(id=2, titulo="Cyberpunk 2077", preco=199.90)

        carrinho.adicionar_jogo(jogo1)
        carrinho.adicionar_jogo(jogo2)

        # Remove o primeiro jogo
        carrinho.remover_jogo(jogo1)

        assert len(carrinho.listar_jogos()) == 1
        assert carrinho.listar_jogos()[0].titulo == "Cyberpunk 2077"
        assert carrinho.calcular_total() == 199.90

    def test_esvaziar_carrinho_completamente(self):
        """Teste de esvaziamento completo do carrinho (TC-CAR-002)"""
        carrinho = CarrinhoService()
        jogo = Jogo(id=1, titulo="The Witcher 3", preco=99.99)

        carrinho.adicionar_jogo(jogo)
        assert len(carrinho.listar_jogos()) == 1

        carrinho.remover_jogo(jogo)

        assert len(carrinho.listar_jogos()) == 0
        assert carrinho.calcular_total() == 0.0

    def test_calculo_total_dois_jogos(self):
        """Teste de cálculo do valor total com dois jogos (TC-CAR-003)"""
        carrinho = CarrinhoService()
        jogo1 = Jogo(id=5, titulo="Call of Duty: Black Ops 7", preco=349.90)
        jogo2 = Jogo(id=4, titulo="Hollow Knight", preco=46.99)

        carrinho.adicionar_jogo(jogo1)
        carrinho.adicionar_jogo(jogo2)

        total = carrinho.calcular_total()

        assert total == pytest.approx(396.89, 0.01)

    def test_remover_jogo_inexistente_no_carrinho(self):
        """Teste de tentativa de remover jogo que não está no carrinho"""
        carrinho = CarrinhoService()
        jogo1 = Jogo(id=1, titulo="The Witcher 3", preco=99.99)
        jogo2 = Jogo(id=999, titulo="Game Inexistente", preco=50.0)

        carrinho.adicionar_jogo(jogo1)
        carrinho.remover_jogo(jogo2)

        # Jogo1 deve continuar no carrinho
        assert len(carrinho.listar_jogos()) == 1
        assert carrinho.listar_jogos()[0].titulo == "The Witcher 3"

    def test_adicionar_mesmo_jogo_duas_vezes(self):
        """Teste de adição do mesmo jogo duas vezes (verifica duplicação)"""
        carrinho = CarrinhoService()
        jogo = Jogo(id=1, titulo="The Witcher 3", preco=99.99)

        carrinho.adicionar_jogo(jogo)
        carrinho.adicionar_jogo(jogo)

        # Sistema permite adicionar duas cópias (comportamento esperado)
        assert len(carrinho.listar_jogos()) == 2
        assert carrinho.calcular_total() == 199.98

    def test_calculo_total_com_preco_zero(self):
        """Teste de cálculo quando há jogo com preço zero"""
        carrinho = CarrinhoService()
        jogo_gratis = Jogo(id=99, titulo="Free Game", preco=0.0)
        jogo_pago = Jogo(id=1, titulo="The Witcher 3", preco=99.99)

        carrinho.adicionar_jogo(jogo_gratis)
        carrinho.adicionar_jogo(jogo_pago)

        assert carrinho.calcular_total() == 99.99

    def test_calculo_total_apenas_jogos_gratuitos(self):
        """Teste de cálculo quando só há jogos gratuitos (Valor Limite)"""
        carrinho = CarrinhoService()
        jogo1 = Jogo(id=1, titulo="Free Game 1", preco=0.0)
        jogo2 = Jogo(id=2, titulo="Free Game 2", preco=0.0)

        carrinho.adicionar_jogo(jogo1)
        carrinho.adicionar_jogo(jogo2)

        assert carrinho.calcular_total() == 0.0

    def test_listar_jogos_retorna_lista_correta(self):
        """Teste de que listar_jogos retorna a lista correta"""
        carrinho = CarrinhoService()
        jogo1 = Jogo(id=1, titulo="The Witcher 3", preco=99.99)
        jogo2 = Jogo(id=2, titulo="Cyberpunk 2077", preco=199.90)

        carrinho.adicionar_jogo(jogo1)
        carrinho.adicionar_jogo(jogo2)

        lista = carrinho.listar_jogos()

        assert isinstance(lista, list)
        assert len(lista) == 2
        assert jogo1 in lista
        assert jogo2 in lista

    def test_remover_todos_os_jogos_sequencialmente(self):
        """Teste de remoção de todos os itens do carrinho um por um"""
        carrinho = CarrinhoService()
        jogo1 = Jogo(id=1, titulo="The Witcher 3", preco=99.99)
        jogo2 = Jogo(id=2, titulo="Cyberpunk 2077", preco=199.90)
        jogo3 = Jogo(id=3, titulo="Elden Ring", preco=249.90)

        carrinho.adicionar_jogo(jogo1)
        carrinho.adicionar_jogo(jogo2)
        carrinho.adicionar_jogo(jogo3)

        assert len(carrinho.listar_jogos()) == 3

        carrinho.remover_jogo(jogo1)
        assert len(carrinho.listar_jogos()) == 2

        carrinho.remover_jogo(jogo2)
        assert len(carrinho.listar_jogos()) == 1

        carrinho.remover_jogo(jogo3)
        assert len(carrinho.listar_jogos()) == 0
        assert carrinho.calcular_total() == 0.0
