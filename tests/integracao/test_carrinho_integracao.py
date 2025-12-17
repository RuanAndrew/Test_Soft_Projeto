import pytest
from src.models.Jogo import Jogo
from src.services.CarrinhoService import CarrinhoService


class TestCarrinhoIntegracao:

    def test_carrinho_vazio_inicialmente(self):
        """Teste de precondição: carrinho deve estar vazio ao inicializar"""
        carrinho = CarrinhoService()

        assert carrinho.listar_jogos() == []
        assert carrinho.calcular_total() == 0.0

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

        carrinho.remover_jogo(jogo1)

        assert len(carrinho.listar_jogos()) == 1
        assert carrinho.listar_jogos()[0].titulo == "Cyberpunk 2077"
        assert carrinho.calcular_total() == 199.90

    def test_calculo_total_dois_jogos(self):
        """Teste de cálculo do valor total com dois jogos (TC-CAR-003)"""
        carrinho = CarrinhoService()
        jogo1 = Jogo(id=5, titulo="Call of Duty: Black Ops 7", preco=349.90)
        jogo2 = Jogo(id=4, titulo="Hollow Knight", preco=46.99)

        carrinho.adicionar_jogo(jogo1)
        carrinho.adicionar_jogo(jogo2)

        total = carrinho.calcular_total()

        assert total == pytest.approx(396.89, 0.01)

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

    def test_adicionar_jogo_ja_comprado(self, db_memory):
        carrinho = CarrinhoService()
        usuario = db_memory.buscar_usuario_por_email("teste@email.com") 
        jogo_ja_tem = db_memory.buscar_jogo_por_id(1)
        
        carrinho.adicionar_jogo(jogo_ja_tem)

        assert len(carrinho.listar_jogos()) == 0