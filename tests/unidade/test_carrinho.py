import pytest
from unittest.mock import MagicMock

class TestCarrinho:
	def test_adicionar_jogo_ao_carrinho(self, carrinho_service):
		"""TC-CAR-001"""
		mock_jogo = MagicMock()
		mock_jogo.titulo = "Call of Duty"
		mock_jogo.preco = 349.90

		carrinho_service.adicionar_jogo(mock_jogo)

		jogos = carrinho_service.listar_jogos()
		total = carrinho_service.calcular_total()

		assert len(jogos) == 1
		assert jogos[0].titulo == "Call of Duty"
		assert total == 349.90

	def test_remover_jogo_do_carrinho(self, carrinho_service):
		"""TC-CAR-002"""
		mock_jogo = MagicMock()
		mock_jogo.titulo = "Call of Duty"
		mock_jogo.preco = 349.90

		carrinho_service.adicionar_jogo(mock_jogo)
		carrinho_service.remover_jogo(mock_jogo)

		assert len(carrinho_service.listar_jogos()) == 0
		assert carrinho_service.calcular_total() == 0.0

	def test_calculo_valor_total_carrinho(self, carrinho_service):
		"""TC-CAR-003"""
		mock_jogo1 = MagicMock()
		mock_jogo1.preco = 349.90
		mock_jogo2 = MagicMock()
		mock_jogo2.preco = 46.99

		carrinho_service.adicionar_jogo(mock_jogo1)
		carrinho_service.adicionar_jogo(mock_jogo2)

		total = carrinho_service.calcular_total()

		assert total == pytest.approx(396.89, 0.01)
